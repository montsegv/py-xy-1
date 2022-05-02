#
# read binary file (tuple)
# and print it
#


import pickle

with open('tuple.bin','rb') as fh:
        tup = pickle.load(fh) 

print(type(tup))
print(tup)
