from uvm_common import uvm_utils
from uvm_common import class_declare
from uvm_common import port_declare
from uvm_common import component_new
from uvm_common import task_func_declare
import os,re

class Monitor():
    
    def __init__(self,clk,c_out_seqitem,c_mon,bc_mon,c_dut_mon_if,i_dut_mon_if):
        self.clk                =   clk
        self.c_out_seqitem      =   c_out_seqitem
        self.c_mon              =   c_mon
        self.bc_mon             =   bc_mon
        self.c_dut_mon_if       =   c_dut_mon_if
        self.i_dut_mon_if       =   i_dut_mon_if

    def draw_class_head(self,f_dst):
        f_dst.write("class "+self.c_mon+" extends "+self.bc_mon+";\n")#打印换行
        f_dst.write("\n")#打印换行

    def draw_class_end(self,f_dst):
        f_dst.write("\n")#打印换行
        f_dst.write("endclass\n")

    def draw_utils(self,f_dst):
        uvm_utils(f_dst,'component',self.c_mon)

    def draw_if_dutmon_declare(self,f_dst):
        class_declare(f_dst,'virtual '+self.c_dut_mon_if,self.i_dut_mon_if)

    def draw_ap_declare(self,f_dst):
        port_declare(f_dst,'uvm_analysis_port',self.c_out_seqitem,'ap')

    def draw_monitor_new(self,f_dst):
        component_new(f_dst,self.c_mon)

    def draw_build_phase_declare(self,f_dst):
        task_func_declare(f_dst,0,'build_phase','uvm_phase phase')

    def draw_main_phase_declare(self,f_dst):
        task_func_declare(f_dst,1,'main_phase','uvm_phase phase')

    def draw_collect_one_item_declare(self,f_dst):
        task_func_declare(f_dst,1,'collect_one_item',self.c_out_seqitem+'tr')

    def draw_build_phase(self,f_dst):
        f_dst.write("\n")#打印换行
        f_dst.write("/"+"*"*80+"/\n")#打印分隔符
        f_dst.write("\tfunction void " + self.c_mon + "::build_phase(uvm_phase phase);\n")
        f_dst.write("\t\tap=new(\"ap\",this);\n")
        f_dst.write("\t\tsuper.build_phase(phase);\n")
        f_dst.write("\t\tif(!uvm_config_db#(virtual "+self.c_dut_mon_if+")::get(this,\"\",\"vif\","+self.i_dut_mon_if+"))\n")
        f_dst.write("\t\t\t`uvm_fatal(\""+self.c_mon+"\",\"cannot get vif !!!\")\n")
        f_dst.write("\t\t`uvm_info(\""+self.c_mon+"\",\""+self.c_mon+" is called\",UVM_LOW)\n")
        f_dst.write("\tendfunction\n")
        f_dst.write("/"+"*"*80+"/\n")#打印分隔符
        f_dst.write("\n");#打印换行

    def draw_main_phase(self,f_dst):
        f_dst.write("\n");#打印换行
        f_dst.write("/"+"*"*80+"/\n")#打印分隔符
        f_dst.write("\ttask "+self.c_mon+"::main_phase(uvm_phase phase);\n");
        f_dst.write("\t\t"+self.c_out_seqitem+" tr;\n");
        f_dst.write("\t\tforever;\n");
        f_dst.write("\t\tbegin\n");
        f_dst.write("\t\t\ttr=new(\"tr\");\n");
        f_dst.write("\t\t\tcollect_one_item(tr);\n");
        f_dst.write("\t\t\tap.write.(tr);\n");
        f_dst.write("\t\tend\n");
        f_dst.write("\tendtask\n");
        f_dst.write("/"+"*"*80+"/\n")
        f_dst.write("\n")

    def draw_collect_one_item(self,f_dst,fobj_src):
        f_dst.write("\n")#打印换行
        f_dst.write("/"+"*"*80+"/\n");#打印分隔符
        f_dst.write("\ttask "+self.c_mon+"::collect_one_item("+self.c_out_seqitem+" tr);\n")
        f_dst.write("\t@(posedge "+self.i_dut_mon_if+"."+self.clk+")\n")
        f_dst.write("\t`uvm_info(\""+self.c_mon+"\",\"begin to collect one item\",UVM_LOW)\n")
        fobj_src.seek(0,0)  #回到文件开头
        p1 = re.compile('^\s*\/\/') #注释
        p2 = re.compile('output.*\s+(\w+)\s*[,;]')
        for line in fobj_src:
            line = line.strip()
            m1 = p1.search(line) #信号位宽为1 
            m2 = p2.search(line) #时钟和复位不包含在item中
            if m1: #注释
                continue
            elif m2: #时钟和复位不包含在item中
                f_dst.write("\t\t\ttr.%-25s<=\t%s.%-25s;\n" % (m2.group(1),self.i_dut_mon_if,m2.group(1)))
        f_dst.write("\t`uvm_info(\""+self.c_mon+"\",\"item_collecting finish,print it:\",UVM_LOW)\n")
        f_dst.write("\ttr.print();\n");
        f_dst.write("\tendtask\n")
        f_dst.write("/"+"*"*80+"/\n")
        f_dst.write("\n")
