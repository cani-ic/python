import re

####################################################################################################
#m = re.match('foo','foolish')      # Y
#m = re.match('foo','food is good') # Y 
#m = re.match('foo','seafood')      # N

#m = re.search('foo','seafood')      # Y
if m is not None:
   print(m.group())


