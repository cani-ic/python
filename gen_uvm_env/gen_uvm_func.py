import re
def sort_patt_line(i_file,o_file,pattern,o_mode):
    if_obj = open(i_file,'r')
    of_obj = open(o_file,o_mode)
    while True:
        line = if_obj.readline()
        if not line:break
        if re.search(pattern,line):
            of_obj.write(line)
    if_obj.close()
    of_obj.close()


def print_separate_line(o_file):
    fs = '' # separator
    str_list = ('\n#','-'*80 ,'#\n\n') 
    separate_line = fs.join(str_list)   # str.join
    of_obj = open(o_file,'a')   # append mode
    of_obj.write(separate_line)
    of_obj.close()
