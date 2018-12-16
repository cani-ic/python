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

def get_dut_clk(f_obj):
    p_clk   = re.compile('([gc]?clk)',re.I)              #不区分大小写
    for line in f_obj:
        line = line.strip()
        m_clk = p_clk.search(line)
        if m_clk:
            break
    return m_clk.group()

def get_dut_reset(f_obj):
    p_reset = re.compile('(reset_n|rstn_i|rst_n)',re.I)     #不区分大小写
    for line in f_obj:
        line = line.strip()
        m_reset =   p_reset.search(line)
        if m_reset:
            break
    return m_reset.group()

