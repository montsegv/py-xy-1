#
# 2do
#


import pickle

t=12,True,3.1,'aCat'


with open('tuple.bin', "rb") as fh:
    pickle.dump(tup, fh)

print("done...")

