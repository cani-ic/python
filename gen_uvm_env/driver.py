from uvm_common import uvm_utils
from uvm_common import class_declare
from uvm_common import port_declare
from uvm_common import component_new
from uvm_common import task_func_declare
import os,re

class Driver():
    
    def __init__(self,clk,c_in_seqitem,bc_drv,
                i_drv_ap,i_mon_ap,i_sqr,c_sqr,i_drv,c_drv,i_mon,c_mon,c_drv_dut_if,i_drv_dut_if):
        self.clk            =  clk   
        self.c_in_seqitem   =  c_in_seqitem   
        self.bc_drv         =  bc_drv   
        self.i_drv_ap       =  i_drv_ap 
        self.i_mon_ap       =  i_mon_ap 
        self.i_sqr          =  i_sqr 
        self.c_sqr          =  c_sqr 
        self.i_drv          =  i_drv 
        self.c_drv          =  c_drv 
        self.i_mon          =  i_mon 
        self.c_mon          =  c_mon 
        self.c_drv_dut_if   =  c_drv_dut_if 
        self.i_drv_dut_if   =  i_drv_dut_if 

    def draw_class_head(self,f_dst):
        f_dst.write("class "+self.c_drv+" extends "+self.bc_drv+";\n")#打印换行
        f_dst.write("\n")#打印换行

    def draw_class_end(self,f_dst):
        f_dst.write("\n")#打印换行
        f_dst.write("endclass\n")

    def draw_utils(self,f_dst):
        uvm_utils(f_dst,'component',self.c_drv)

    def draw_if_drvdut_declare(self,f_dst):
        class_declare(f_dst,'virtual '+self.c_drv_dut_if,self.i_drv_dut_if)

    def draw_ap_declare(self,f_dst):
        port_declare(f_dst,'uvm_analysis_port',self.c_in_seqitem,'ap')

    def draw_driver_new(self,f_dst):
        component_new(f_dst,self.c_drv)

    def draw_build_phase_declare(self,f_dst):
        task_func_declare(f_dst,0,'build_phase','uvm_phase phase')

    def draw_main_phase_declare(self,f_dst):
        task_func_declare(f_dst,1,'main_phase','uvm_phase phase')

    def draw_drive_one_item_declare(self,f_dst):
        task_func_declare(f_dst,1,'drive_one_item',self.c_in_seqitem+'tr')

    def draw_build_phase(self,f_dst):
        f_dst.write("\n")#打印换行
        f_dst.write("/"+"*"*80+"/\n")#打印分隔符
        f_dst.write("\tfunction void " + self.c_drv + "::build_phase(uvm_phase phase);\n")
        f_dst.write("\t\tap=new(\"ap\",this);\n");
        f_dst.write("\t\tsuper.build_phase(phase);\n")
        f_dst.write("\t\tif(!uvm_config_db#(virtual "+self.c_drv_dut_if+")::get(this,\"\",\"vif\","+self.i_drv_dut_if+"))\n")
        f_dst.write("\t\t\t`uvm_info(\"GETVIF\",\"cannot get "+self.i_drv_dut_if+" !!!\",UVM_LOW)\n")
        f_dst.write("\tendfunction\n")
        f_dst.write("/"+"*"*80+"/\n")#打印分隔符
        f_dst.write("\n");#打印换行

    def draw_main_phase(self,f_dst):
        f_dst.write("\n");#打印换行
        f_dst.write("/"+"*"*80+"/\n")#打印分隔符
        f_dst.write("\ttask "+self.c_drv+"::main_phase(uvm_phase phase);\n")
        f_dst.write("\t\tREQ tmp;\n")                                 
        f_dst.write("\t\t"+self.c_in_seqitem+" exp_item;\n")                  
        f_dst.write("\t\tforever\n")                                 
        f_dst.write("\t\tbegin\n")                                    
        f_dst.write("\t\t\tseq_item_port.get_next_item(tmp);\n")      
        f_dst.write("\t\t\t$cast(exp_item,tmp);\n")                  
        f_dst.write("\t\t\tdrive_one_item(exp_item);\n")              
        f_dst.write("\t\t\tseq_item_port.item_done();\n")             
        f_dst.write("\t\t\tap.write.(exp_item);\n")                   
        f_dst.write("\t\tend\n")                                      
        f_dst.write("\tendtask\n")                                    
        f_dst.write("/"+"*"*80+"/\n")
        f_dst.write("\n")

    def draw_drive_one_item(self,f_dst,fobj_src):
        f_dst.write("\n")#打印换行
        f_dst.write("/"+"*"*80+"/\n");#打印分隔符
        f_dst.write("\ttask "+self.c_drv+"::drive_one_item("+self.c_in_seqitem+" tr);\n")
        f_dst.write("\t\t@(posedge "+self.i_drv_dut_if+"."+self.clk+")\n")
        f_dst.write("\t\tbegin\n")
        fobj_src.seek(0,0)  #回到文件开头
        p1 = re.compile('input.*\s+(\w+)\s*[,;]')
        p2 = re.compile('(Reset|Clk)')
        for line in fobj_src:
            line = line.strip()
            m1 = p1.search(line) #信号位宽为1 
            m2 = p2.search(line) #时钟和复位不包含在item中
            if m1: #信号位宽为1 
                if m2: #时钟和复位不包含在item中
                    continue 
                else:
                    f_dst.write("\t\t\t"+self.i_drv_dut_if+".%-25s<=\ttr.%-25s;\n" % (m1.group(1),m1.group(1)))
        f_dst.write("\t\tend\n")
        f_dst.write("\tendtask\n")
        f_dst.write("/"+"*"*80+"/\n")
        f_dst.write("\n")
