from driver import Driver
import os 

def gen_uvm_driver(uvmconfig):

    my_driver = Driver(
    uvmconfig.clk,
    uvmconfig.c_in_seqitem,
    uvmconfig.bc_drv,
    uvmconfig.c_drv,
    uvmconfig.i_drv_ap,
    uvmconfig.i_mon_ap,
    uvmconfig.i_sqr,
    uvmconfig.c_sqr,
    uvmconfig.i_drv,
    uvmconfig.i_mon,
    uvmconfig.c_mon,
    uvmconfig.c_drv_dut_if,
    uvmconfig.i_drv_dut_if
    )    

    fobj_drv = open(uvmconfig.todir+os.sep+uvmconfig.fn_drv,'w')

    my_driver.draw_class_head(fobj_drv)
    my_driver.draw_utils(fobj_drv)
    my_driver.draw_if_drvdut_declare(fobj_drv)
    my_driver.draw_ap_declare(fobj_drv)
    my_driver.draw_driver_new(fobj_drv)
    my_driver.draw_build_phase_declare(fobj_drv)
    my_driver.draw_main_phase_declare(fobj_drv)
    my_driver.draw_drive_one_item_declare(fobj_drv)
    my_driver.draw_class_end(fobj_drv)
    my_driver.draw_build_phase(fobj_drv)
    my_driver.draw_main_phase(fobj_drv)
    my_driver.draw_drive_one_item(fobj_drv,uvmconfig.fobj_src)
