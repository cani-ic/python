from uvm_config import UVMConfig
from gen_uvm_driver import gen_uvm_driver 
from gen_uvm_agent import gen_uvm_agent 
from gen_uvm_monitor import gen_uvm_monitor 
from uvm_common import get_dut_clk
from uvm_common import get_dut_reset
import os,sys



modulename  = sys.argv[1]
designfile  = sys.argv[2]

fobj_src    =  open(designfile)


#获取dut中的clk,reset信号
clk = get_dut_clk(fobj_src)
reset = get_dut_reset(fobj_src)

uvmconfig  = UVMConfig(modulename.lower())

todir = uvmconfig.todir;
if not os.path.exists(todir):
    os.mkdir(todir)
else:
    for fname in os.listdir(todir):
        os.remove(os.path.join(todir,fname))

uvmconfig.set_fobj_src(fobj_src)
uvmconfig.set_clk(clk)
uvmconfig.set_reset(reset)

gen_uvm_agent(uvmconfig)
gen_uvm_driver(uvmconfig)
gen_uvm_monitor(uvmconfig)
