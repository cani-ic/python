import sys
from func import getopts
myargs = getopts(sys.argv)
if '-i' in myargs:
    print(myargs['-i'])
print(myargs)

