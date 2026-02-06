import pickle
import random as rd
global V 
V = [1,1,1,1,1,1,5,5,5,5,5,5,]
L = [0, 2, 2, 3, 3, 3, 2, 3, 3, 5, 6, 4, 4, 4, 4, 4, 3, 3, 7, 3, 3, 3, 3, 3, 3, 3]

def makF(x,y):
    L = [0, 
         5, 5, 5, 2, 2, 
         5, 5, 2, 2, 2,
         5, 2, "jfkdisndheisldhe", 5, "fujendhsjienghwi", 
         2, 2, 2, 5, 5, 
         2, 5, 5, "pxyztxchipzymxnv", 5]
    q = str(y)+";"+str(x)+".dat"
    fh = open(q,"wb")
    pickle.dump(L,fh)
    fh.close()

makF(1,1)

'''for i in range(42,51):
    #for j in range(19,26):
        makF(i,8)'''
