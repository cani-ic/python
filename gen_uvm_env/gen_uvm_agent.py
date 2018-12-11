from agent import Agent

def gen_uvm_agent(uvmconfig):

    my_agent = Agent(
    uvmconfig.dirname,
    uvmconfig.fname_agt,
    uvmconfig.c_in_seqitem,
    uvmconfig.c_out_seqitem ,
    uvmconfig.bc_agt,
    uvmconfig.c_agt,
    uvmconfig.i_drv_ap,
    uvmconfig.i_mon_ap,
    uvmconfig.i_sqr,
    uvmconfig.c_sqr,
    uvmconfig.i_drv,
    uvmconfig.c_drv,
    uvmconfig.i_mon,
    uvmconfig.c_mon)    

    my_agent.open_file()
    my_agent.draw_class_head()
    my_agent.draw_utils()
    my_agent.sqr_declare()
    my_agent.drv_declare()
    my_agent.mon_declare()
    my_agent.drv_ap_declare()
    my_agent.mon_ap_declare()
    my_agent.mon_ap_declare()
    my_agent.agent_new()
    my_agent.build_phase_declare()
    my_agent.connect_phase_declare()
    my_agent.draw_class_end()
    my_agent.draw_build_phase()
    my_agent.draw_connect_phase()
