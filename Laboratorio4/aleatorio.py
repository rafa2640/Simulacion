import numpy as np

def Conmix(numax=1):
    numeros= []
    Xn = 7
    a = 7
    c = 1
    m = 16547
    
    
    for iterator in range(numax):        
        Xn_1 = (a*Xn + c)% m        
        out = float(Xn_1)/float(m)    
        numeros.append(out)
        Xn = Xn_1
    return numeros