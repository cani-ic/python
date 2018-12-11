class UVMConfig():
    def __init__(self,modulename):
        self.dirname         =   './out'   
        self.c_in_seqitem    =   'input_trans_'+modulename
        self.c_out_seqitem   =   'output_trans_'+modulename
        self.c_sqr           =   'sqr_'+modulename
        self.c_drv           =   'drv_'+modulename
        self.c_mon           =   'mon_'+modulename
        self.c_agt           =   'agt_'+modulename
        self.c_mdl           =   'mdl_'+modulename
        self.c_scb           =   'scb_'+modulename
        self.c_env           =   'env_'+modulename
        self.c_base_test     =   'base_test_'+modulename
        self.c_demo_seq      =   'demo_seq_'+modulename
        self.c_demo_test     =   'demo_test_'+modulename
        self.c_drv_dut_if    =   'drv_dut_if_'+modulename
        self.c_dut_mon_if    =   'dut_mon_if_'+modulename
        
        self.fname_in_seqitem    =   'input_trans_'+modulename+'.sv'
        self.fname_out_seqitem   =   'output_trans_'+modulename+'.sv'
        self.fname_sqr           =   'sqr_'+modulename+'.sv'
        self.fname_drv           =   'drv_'+modulename+'.sv'
        self.fname_mon           =   'mon_'+modulename+'.sv'
        self.fname_agt           =   'agt_'+modulename+'.sv'
        self.fname_mdl           =   'mdl_'+modulename+'.sv'
        self.fname_scb           =   'scb_'+modulename+'.sv'
        self.fname_env           =   'env_'+modulename+'.sv'
        self.fname_base_test     =   'base_test_'+modulename+'.sv'
        self.fname_demo_seq      =   'demo_seq_'+modulename+'.sv'
        self.fname_demo_test     =   'demo_test_'+modulename+'.sv'
        
        self.m_module        =   'tb_'+modulename
        self.dir             =   'env_'+modulename
        
        self.i_in_seqitem    =   'my_item'
        self.i_sqr           =   'my_sqr'
        self.i_drv           =   'my_drv'
        self.i_mon           =   'my_mon'
        self.i_agt1          =   'my_agt_i'
        self.i_agt2          =   'my_agt_o'
        self.i_mdl           =   'my_mdl'
        self.i_scb           =   'my_scb'
        self.i_env           =   'my_env'
        self.i_drv_dut_if    =   'i_drv_dut_if'
        self.i_dut_mon_if    =   'o_dut_mon_if'
        self.i_drv_ap        =   'drv_ap'
        self.i_mon_ap        =   'mon_ap'
        self.agt_mdl_fifo    =   'agt_mdl_fifo'
        self.agt_scb_fifo    =   'agt_scb_fifo'
        self.mdl_scb_fifo    =   'mdl_scb_fifo'
        
        self.bc_seqitem      =   'uvm_sequence_item'
        self.bc_sqr          =   'uvm_sequencer'
        self.bc_drv          =   'uvm_driver'
        self.bc_mon          =   'uvm_monitor'
        self.bc_agt          =   'uvm_agent'
        self.bc_mdl          =   'uvm_component'
        self.bc_scb          =   'uvm_scoreboard'
        self.bc_base_test    =   'uvm_test'
        self.bc_demo_seq     =   'uvm_sequence'
        self.bc_demo_test    =   'base_test_'+modulename
        
        self.exp_port        =   'exp_port'
        self.exp_queue       =   'exp_queue'
        self.act_port        =   'act_port'
