def uvm_utils(f_obj,utils_type,classname):
    f_obj.write( "\t`uvm_"+utils_type+"_utils("+classname+")\n")

def class_instantize(f_obj,c_class,i_inst):
    f_obj.write("\t"+c_class+"\t"+i_inst+";\n")

#            &class_declare($fh_dst,$c_sqr,$i_sqr);
#            &class_declare($fh_dst,$c_drv,$i_drv);
#            &class_declare($fh_dst,$c_mon,$i_mon);
#            &port_declare($fh_dst,"uvm_analysis_port",$c_in_seqitem,$i_drv_ap);
#            &port_declare($fh_dst,"uvm_analysis_port",$c_out_seqitem,$i_mon_ap);
#            &component_new($fh_dst,$c_agt);
#            &task_func_declare($fh_dst,'function void','build_phase','uvm_phase phase');
#            &task_func_declare($fh_dst,'function void','connect_phase','uvm_phase phase');
