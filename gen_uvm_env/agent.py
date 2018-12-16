from uvm_common import uvm_utils
from uvm_common import class_declare
from uvm_common import port_declare
from uvm_common import component_new
from uvm_common import task_func_declare
import os,sys
class Agent():
    
    def __init__(self,c_in_seqitem,c_out_seqitem,bc_agt,
                c_agt,i_drv_ap,i_mon_ap,i_sqr,c_sqr,i_drv,c_drv,i_mon,c_mon):
        self.c_in_seqitem   =  c_in_seqitem   
        self.c_out_seqitem  =  c_out_seqitem   
        self.bc_agt         =  bc_agt   
        self.c_agt          =  c_agt    
        self.i_drv_ap       =  i_drv_ap 
        self.i_mon_ap       =  i_mon_ap 
        self.i_sqr          =  i_sqr 
        self.c_sqr          =  c_sqr 
        self.i_drv          =  i_drv 
        self.c_drv          =  c_drv 
        self.i_mon          =  i_mon 
        self.c_mon          =  c_mon 

#    def open_file(self,f_dst):
#        if not os.path.exists(self.dirname):
#            os.mkdir(self.dirname)
#        else:
#            for fname in os.listdir(self.dirname):
#                os.remove(os.path.join(self.dirname,fname))
#        f_dst = open(self.dirname +os.sep+ self.fname,'w')

    def draw_class_head(self,f_dst):
        f_dst.write("class "+self.c_agt+" extends "+self.bc_agt+";\n")#打印换行
        f_dst.write("\n")#打印换行

    def draw_class_end(self,f_dst):
        f_dst.write("\n")#打印换行
        f_dst.write("endclass\n")

    def draw_utils(self,f_dst):
        uvm_utils(f_dst,'component',self.c_agt)

    def draw_sqr_declare(self,f_dst):
        class_declare(f_dst,self.c_sqr,self.i_sqr)

    def draw_drv_declare(self,f_dst):
        class_declare(f_dst,self.c_drv,self.i_drv)

    def draw_mon_declare(self,f_dst):
        class_declare(f_dst,self.c_mon,self.i_mon)

    def draw_drv_ap_declare(self,f_dst):
        port_declare(f_dst,'uvm_analysis_port',self.c_in_seqitem,self.i_drv_ap)

    def draw_mon_ap_declare(self,f_dst):
        port_declare(f_dst,'uvm_analysis_port',self.c_out_seqitem,self.i_mon_ap)

    def draw_agent_new(self,f_dst):
        component_new(f_dst,self.c_agt)

    def draw_build_phase_declare(self,f_dst):
        task_func_declare(f_dst,0,'build_phase','uvm_phase phase')

    def draw_connect_phase_declare(self,f_dst):
        task_func_declare(f_dst,0,'connect_phase','uvm_phase phase')

    def draw_build_phase(self,f_dst):
        f_dst.write("\n")#打印换行
        f_dst.write("/"+"*"*80+"/\n")#打印分隔符
        f_dst.write("\tfunction void " + self.c_agt + "::build_phase(uvm_phase phase);\n")
        f_dst.write("\t\tsuper.build_phase(phase);\n")
        f_dst.write("\t\t"+self.i_drv_ap+"=new(\""+self.i_drv_ap+"\",this);\n")
        f_dst.write("\t\t"+self.i_mon_ap+"=new(\""+self.i_mon_ap+"\",this);\n")
        f_dst.write("\t\tif(is_active==UVM_ACTIVE)\n")
        f_dst.write("\t\tbegin\n")
        f_dst.write("\t\t\t"+self.i_sqr+" = "+self.c_sqr+"::type_id::create(\""+self.i_sqr+"\",this);\n")
        f_dst.write("\t\t\t"+self.i_drv+" = "+self.c_drv+"::type_id::create(\""+self.i_drv+"\",this);\n")
        f_dst.write("\t\tend\n")
        f_dst.write("\t\telse\n")
        f_dst.write("\t\tbegin\n")
        f_dst.write("\t\t\t"+self.i_mon+" = "+self.c_mon+"::type_id::create(\""+self.i_mon+"\",this);\n")
        f_dst.write("\t\tend\n")
        f_dst.write("\tendfunction\n")
        f_dst.write("/"+"*"*80+"/\n")#打印分隔符
        f_dst.write("\n");#打印换行

    def draw_connect_phase(self,f_dst):
        f_dst.write("\n");#打印换行
        f_dst.write("/"+"*"*80+"/\n")#打印分隔符
        f_dst.write("\tfunction void "+self.c_agt+"::connect_phase(uvm_phase phase);\n")
        f_dst.write("\t\tsuper.connect_phase(phase);\n")
        f_dst.write("\t\tif(is_active==UVM_ACTIVE)\n")
        f_dst.write("\t\tbegin\n")
        f_dst.write("\t\t\t"+self.i_drv+".seq_item_port.connect("+self.i_sqr+".seq_item_export);\n")
        f_dst.write("\t\t\t"+self.i_drv_ap+" = "+self.i_drv+".ap;\n")
        f_dst.write("\t\tend\n")
        f_dst.write("\t\telse\n")
        f_dst.write("\t\tbegin\n")
        f_dst.write("\t\t\t"+self.i_mon_ap+" = "+self.i_mon+".ap;\n")
        f_dst.write("\t\tend\n")
        f_dst.write("\tendfunction\n")
        f_dst.write("/"+"*"*80+"/\n")
        f_dst.write("\n")
