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
