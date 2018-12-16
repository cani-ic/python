from monitor import Monitor
import os 

def gen_uvm_monitor(uvmconfig):

    my_monitor = Monitor(
    uvmconfig.clk,
    uvmconfig.c_out_seqitem,
    uvmconfig.c_mon,
    uvmconfig.bc_mon,
    uvmconfig.c_dut_mon_if,
    uvmconfig.i_dut_mon_if
    )    

    fobj_mon = open(uvmconfig.todir+os.sep+uvmconfig.fn_mon,'w')

    my_monitor.draw_class_head(fobj_mon)
    my_monitor.draw_utils(fobj_mon)
    my_monitor.draw_if_dutmon_declare(fobj_mon)
    my_monitor.draw_ap_declare(fobj_mon)
    my_monitor.draw_monitor_new(fobj_mon)
    my_monitor.draw_build_phase_declare(fobj_mon)
    my_monitor.draw_main_phase_declare(fobj_mon)
    my_monitor.draw_collect_one_item_declare(fobj_mon)
    my_monitor.draw_class_end(fobj_mon)
    my_monitor.draw_build_phase(fobj_mon)
    my_monitor.draw_main_phase(fobj_mon)
    my_monitor.draw_collect_one_item(fobj_mon,uvmconfig.fobj_src)
