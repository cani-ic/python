from uvm_common import uvm_utils
from uvm_common import class_declare
from uvm_common import port_declare
from uvm_common import component_new
from uvm_common import task_func_declare
import os

class Driver():
    
    def __init__(self,dirname,fname,c_in_seqitem,bc_drv,
                i_drv_ap,i_mon_ap,i_sqr,c_sqr,i_drv,c_drv,i_mon,c_mon,c_drv_dut_if,i_drv_dut_if):
        self.f_obj          =  ''   
        self.dirname        =  dirname   
        self.fname          =  fname   
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

    def open_file(self):
        if not os.path.exists(self.dirname):
            os.mkdir(self.dirname)
#        else:
#            for fname in os.listdir(self.dirname):
#                os.remove(os.path.join(self.dirname,fname))
        self.f_obj = open(self.dirname +os.sep+ self.fname,'w')

    def draw_class_head(self):
        self.f_obj.write("class "+self.c_drv+" extends "+self.bc_drv+";\n")#打印换行
        self.f_obj.write("\n")#打印换行

    def draw_class_end(self):
        self.f_obj.write("\n")#打印换行
        self.f_obj.write("endclass\n")

    def draw_utils(self):
        uvm_utils(self.f_obj,'component',self.c_drv)

    def if_drvdut_declare(self):
        class_declare(self.f_obj,'virtual '+self.c_drv_dut_if,self.i_drv_dut_if)

    def ap_declare(self):
        port_declare(self.f_obj,'uvm_analysis_port',self.c_in_seqitem,'ap')

    def driver_new(self):
        component_new(self.f_obj,self.c_drv)

    def build_phase_declare(self):
        task_func_declare(self.f_obj,0,'build_phase','uvm_phase phase')

    def main_phase_declare(self):
        task_func_declare(self.f_obj,0,'main_phase','uvm_phase phase')

    def drive_one_item_declare(self):
        task_func_declare(self.f_obj,1,'drive_one_item',self.c_in_seqitem+'tr')

    def draw_build_phase(self):
        self.f_obj.write("\n")#打印换行
        self.f_obj.write("/"+"*"*80+"/\n")#打印分隔符
        self.f_obj.write("\tfunction void " + self.c_drv + "::build_phase(uvm_phase phase);\n")
        self.f_obj.write("\t\tap=new(\"ap\",this);\n");
        self.f_obj.write("\t\tsuper.build_phase(phase);\n")
        self.f_obj.write("\t\tif(!uvm_config_db#(virtual "+c_drv_dut_if+")::get(this,\"\",\"vif\","+i_drv_dut_if+"))\n")
        self.f_obj.write("\t\t\t`uvm_info(\"GETVIF\",\"cannot get "+i_drv_dut_if+" !!!\",UVM_LOW)\n")
        self.f_obj.write("\tendfunction\n")
        self.f_obj.write("/"+"*"*80+"/\n")#打印分隔符
        self.f_obj.write("\n");#打印换行

    def draw_main_phase(self):
        self.f_obj.write("\n");#打印换行
        self.f_obj.write("/"+"*"*80+"/\n")#打印分隔符
        self.f_obj.write("\ttask "+c_drv+"\:\:main_phase(uvm_phase phase);\n")
        self.f_obj.write("\t\tREQ tmp;\n")                                 
        self.f_obj.write("\t\t"+c_in_seqitem+" exp_item\n")                  
        self.f_obj.write("\t\tforever\n")                                 
        self.f_obj.write("\t\tbegin\n")                                    
        self.f_obj.write("\t\t\tseq_item_port.get_next_item(tmp)\n")      
        self.f_obj.write("\t\t\t\$cast(exp_item,tmp)\n")                  
        self.f_obj.write("\t\t\tdrive_one_item(exp_item)\n")              
        self.f_obj.write("\t\t\tseq_item_port.item_done()\n")             
        self.f_obj.write("\t\t\tap.write.(exp_item)\n")                   
        self.f_obj.write("\t\tend\n")                                      
        self.f_obj.write("\tendtask\n")                                    
        self.f_obj.write("/"+"*"*80+"/\n")
        self.f_obj.write("\n")

    def drive_one_item(self):
        print ($fh_dst "\n");#打印换行
        print ($fh_dst "/","*" x 80,"\n");#打印分隔符
        print ($fh_dst "\ttask $c_drv\:\:drive_one_item($c_in_seqitem tr);\n");
        print ($fh_dst "\t\t@(posedge $i_drv_dut_if.$clk)\n");
        print ($fh_dst "\t\tbegin\n");

        print $fh_dst "\t\tend\n");
        print ($fh_dst "\tendtask\n");
        print ($fh_dst "/","*" x 80,"\n");#打印分隔符
        print ($fh_dst "\n");#打印换行
        self.f_obj.write("\n");#打印换行
        self.f_obj.write("/"+"*"*80+"/\n")#打印分隔符
        self.f_obj.write("\tfunction void "+self.c_drv+"::main_phase(uvm_phase phase);\n")
        self.f_obj.write("\t\tsuper.main_phase(phase);\n")
        self.f_obj.write("\t\tif(is_active==UVM_ACTIVE)\n")
        self.f_obj.write("\t\tbegin\n")
        self.f_obj.write("\t\t\t"+self.i_drv+".seq_item_port.main("+self.i_sqr+".seq_item_export);\n")
        self.f_obj.write("\t\t\t"+self.i_drv_ap+" = "+self.i_drv+".ap;\n")
        self.f_obj.write("\t\tend\n")
        self.f_obj.write("\t\telse\n")
        self.f_obj.write("\t\tbegin\n")
        self.f_obj.write("\t\t\t"+self.i_mon_ap+" = "+self.i_mon+".ap;\n")
        self.f_obj.write("\t\tend\n")
        self.f_obj.write("\tendfunction\n")
        self.f_obj.write("/"+"*"*80+"/\n")
        self.f_obj.write("\n")
