from uvm_common import uvm_utils
from uvm_common import class_instantize
class Agent():
    
    def __init__(self,
        fname,bc_agt,c_agt,i_drv_ap,i_mon_ap,i_sqr,c_sqr,i_drv,c_drv,i_mon,c_mon):
        self.f_obj      =  ''   
        self.fname      =  fname   
        self.bc_agt     =  bc_agt   
        self.c_agt      =  c_agt    
        self.i_drv_ap   =  i_drv_ap 
        self.i_mon_ap   =  i_mon_ap 
        self.i_sqr      =  i_sqr 
        self.c_sqr      =  c_sqr 
        self.i_drv      =  i_drv 
        self.c_drv      =  c_drv 
        self.i_mon      =  i_mon 
        self.c_mon      =  c_mon 

    def open_file(self):
        self.f_obj = open(self.fname,'w')

    def write_class_head(self):
        self.f_obj.write("class "+self.c_agt+" extends "+self.bc_agt+";\n")#打印换行
        self.f_obj.write("\n")#打印换行

    def write_class_end(self):
        self.f_obj.write("\n")#打印换行
        self.f_obj.write("endclass\n")

    def write_utils(self):
        uvm_utils(self.f_obj,'component',self.c_agt)

    def write_class_instantize(self):
        class_instantize(self.f_obj,self.c_sqr,self.i_sqr)
        class_instantize(self.f_obj,self.c_drv,self.i_drv)
        class_instantize(self.f_obj,self.c_mon,self.i_mon)

    def write_build_phase(self):
        self.f_obj.write("\n")#打印换行
        self.f_obj.write("/"+"*"*80+"/\n")#打印分隔符
        self.f_obj.write("\tfunction void " + self.c_agt + "::build_phase(uvm_phase phase);\n")
        self.f_obj.write("\t\tsuper.build_phase(phase);\n")
        self.f_obj.write("\t\t"+self.i_drv_ap+"=new(\""+self.i_drv_ap+"\",this);\n")
        self.f_obj.write("\t\t"+self.i_mon_ap+"=new(\""+self.i_mon_ap+"\",this);\n")
        self.f_obj.write("\t\tif(is_active==UVM_ACTIVE)\n")
        self.f_obj.write("\t\tbegin\n")
        self.f_obj.write("\t\t\t"+self.i_sqr+" = "+self.c_sqr+"::type_id::create(\""+self.i_sqr+"\",this);\n")
        self.f_obj.write("\t\t\t"+self.i_drv+" = "+self.c_drv+"::type_id::create(\""+self.i_drv+"\",this);\n")
        self.f_obj.write("\t\tend\n")
        self.f_obj.write("\t\telse\n")
        self.f_obj.write("\t\tbegin\n")
        self.f_obj.write("\t\t\t"+self.i_mon+" = "+self.c_mon+"::type_id::create(\""+self.i_mon+"\",this);\n")
        self.f_obj.write("\t\tend\n")
        self.f_obj.write("\tendfunction\n")
        self.f_obj.write("/"+"*"*80+"/\n")#打印分隔符
        self.f_obj.write("\n");#打印换行

    def write_connect_phase(self):
        self.f_obj.write("\n");#打印换行
        self.f_obj.write("/"+"*"*80+"/\n")#打印分隔符
        self.f_obj.write("\tfunction void "+self.c_agt+"::connect_phase(uvm_phase phase);\n");
        self.f_obj.write("\t\tsuper.connect_phase(phase);\n");
        self.f_obj.write("\t\tif(is_active==UVM_ACTIVE)\n");
        self.f_obj.write("\t\tbegin\n");
        self.f_obj.write("\t\t\t"+self.i_drv+".seq_item_port.connect("+self.i_sqr+".seq_item_export);\n");
        self.f_obj.write("\t\t\t"+self.i_drv_ap+" = "+self.i_drv+".ap;\n");
        self.f_obj.write("\t\tend\n");
        self.f_obj.write("\t\telse\n");
        self.f_obj.write("\t\tbegin\n");
        self.f_obj.write("\t\t\t"+self.i_mon_ap+" = "+self.i_mon+".ap;\n");
        self.f_obj.write("\t\tend\n");
        self.f_obj.write("\tendfunction\n");
        self.f_obj.write("/"+"*"*80+"/\n")#打印分隔符
        self.f_obj.write("\n");#打印换行
