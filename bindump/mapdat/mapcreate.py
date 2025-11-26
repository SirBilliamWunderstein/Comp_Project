import pickle
L = [0, 1, 1, 1, 1, 1, 1, 2, 1, 3, 1, 1, 3, 1, 1, 2, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1]
fh = open("1;1.dat","wb")
pickle.dump(L,fh)
fh.close()