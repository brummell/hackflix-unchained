import math as m
from pprint import pprint

def euc(user_1, user_2):
    simvec = []
            
    for i in range(len(user_1)):
        simvec.append((user_2[i] - user_1[i])**2)
    pprint(simvec)
    print (1 / (1 + m.sqrt(sum(simvec))))
