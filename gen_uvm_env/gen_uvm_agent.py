from agent import Agent
import os

def gen_uvm_agent(uvmconfig):

    my_agent = Agent(
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

    fobj_agt = open(uvmconfig.todir+os.sep+uvmconfig.fn_agt,'w')
    my_agent.draw_class_head(fobj_agt)
    my_agent.draw_utils(fobj_agt)
    my_agent.draw_sqr_declare(fobj_agt)
    my_agent.draw_drv_declare(fobj_agt)
    my_agent.draw_mon_declare(fobj_agt)
    my_agent.draw_drv_ap_declare(fobj_agt)
    my_agent.draw_mon_ap_declare(fobj_agt)
    my_agent.draw_mon_ap_declare(fobj_agt)
    my_agent.draw_agent_new(fobj_agt)
    my_agent.draw_build_phase_declare(fobj_agt)
    my_agent.draw_connect_phase_declare(fobj_agt)
    my_agent.draw_class_end(fobj_agt)
    my_agent.draw_build_phase(fobj_agt)
    my_agent.draw_connect_phase(fobj_agt)
