################################################################################
def getopts(argv):
    opts={}
    while argv:
        if argv[0][0] == '-':
            opts[argv[0]] = argv[1]
            argv=argv[2:]
      # else   # Error: don't forget the ':'
        else:
            argv=argv[1:]
    return opts

################################################################################
def interact():
    print('hello stream world')
    while True:
        try:
            reply = input('Enter a Number >> ')
      # except: # must specify exception name !!!
        except EOFError: 
            break
        else:
            num = int(reply)
        print("%d squared is %d" % (num,num**2) ) # pay attention to the third "%" in this line !!!
