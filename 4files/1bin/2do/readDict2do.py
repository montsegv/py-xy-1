#
# read binary file (dictionary)
# and print it
#


import pickle

with open('tuple.bin','rb') as fh:
        rDict = pickle.load(fh) 

print(type(rDict))
print(rDict)

print('done...')
