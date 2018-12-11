from uvm_config import UVMConfig
from gen_uvm_driver import gen_uvm_driver 
from gen_uvm_agent import gen_uvm_agent 
import sys

modulename = sys.argv[1]
uvmconfig  = UVMConfig(modulename.lower())
gen_uvm_agent(uvmconfig)
gen_uvm_driver(uvmconfig)
