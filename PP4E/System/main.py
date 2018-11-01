import sys
from func import getopts,interact
myargs = getopts(sys.argv)
if '-i' in myargs:
    print(myargs['-i'])
print(myargs)

interact()
