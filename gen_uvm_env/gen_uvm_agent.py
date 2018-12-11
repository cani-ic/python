from agent import Agent

def gen_uvm_agent(uvmconfig):
    my_agent = Agent(uvmconfig.fname_agt,
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
    my_agent.write_class_head()
    my_agent.write_utils()
    my_agent.write_class_instantize()
#            &port_declare($fh_dst,"uvm_analysis_port",$c_in_seqitem,$i_drv_ap);
#            &port_declare($fh_dst,"uvm_analysis_port",$c_out_seqitem,$i_mon_ap);
#            &component_new($fh_dst,$c_agt);
#            &task_func_declare($fh_dst,'function void','build_phase','uvm_phase phase');
#            &task_func_declare($fh_dst,'function void','connect_phase','uvm_phase phase');
    my_agent.write_class_end()
    my_agent.write_build_phase()
    my_agent.write_connect_phase()

