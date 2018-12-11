from driver import Driver

def gen_uvm_driver(uvmconfig):

    my_driver = Driver(
    uvmconfig.dirname,
    uvmconfig.fname_drv,
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

    my_driver.open_file()
    my_driver.draw_class_head()
    my_driver.draw_utils()
    my_driver.if_drvdut_declare()
    my_driver.ap_declare()
    my_driver.driver_new()
    my_driver.build_phase_declare()
    my_driver.main_phase_declare()
    my_driver.drive_one_item_declare()
    my_driver.draw_class_end()
    my_driver.draw_build_phase()
    my_driver.draw_main_phase()
    my_driver.drive_one_item()
