import re

def uvm_utils(f_obj,utils_type,classname):
    f_obj.write( "\t`uvm_"+utils_type+"_utils("+classname+")\n")

def class_declare(f_obj,c_class,i_inst):
    f_obj.write("\t"+c_class+"\t"+i_inst+";\n")

def port_declare(f_obj,port_type,c_in_seqitem,port_name):
    f_obj.write( "\t"+port_type+"#("+c_in_seqitem+")\t"+port_name+";\n")

def component_new(f_obj,cname):
    f_obj.write("\n");#打印换行
    f_obj.write("/"+"*"*80+"/\n")
    f_obj.write("\tfunction new(string name = \""+cname+"\",uvm_component parent);\n")
    f_obj.write("\t\tsuper.new(name);\n")
    f_obj.write("\tendfunction\n")
    f_obj.write("/"+"*"*80+"/\n")
    f_obj.write("\n")

def task_func_declare(f_obj,task_or_func,name,args):
    if task_or_func:
        f_obj.write( "\textern virtual task "+name+"("+args+");\n")
    else:
        f_obj.write( "\textern virtual function void "+name+"("+args+");\n")

def pattern_scanner(f_obj,task_or_func,name,args):
    seek(f_obj,0,0);  #回到文件开头
    while(<f_obj>)
    {   
        chomp;
        if re.match(/input.*\s+(\w+)\s*;/)  #信号位宽为1 
        {
            if re.match(/Reset|Clk/) #时钟和复位不包含在item中
            {
                continue; 
            }
            else
            {
                f_obj.write("\t\t\t$i_drv_dut_if.%-30s<=\ttr.%-30s\n",$1,$1);
            }
        }
    }
