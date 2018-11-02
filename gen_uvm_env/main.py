import sys
import os 
import re 
from gen_uvm_func import sort_patt_line
from gen_uvm_func import print_separate_line

i_file = 'MCDF/mcdf.v'
o_file = 'env_mcdf.v'

patt_in = 'input\s*(\[.*\])?\s*\w+'
patt_out = 'output\s*(\[.*\])?\s*\w+'

sort_patt_line(i_file,o_file,patt_in,'w')
print_separate_line(o_file)
sort_patt_line(i_file,o_file,patt_out,'a')  # append mode
