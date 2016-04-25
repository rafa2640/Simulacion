import numpy as np

def Conmix(x0, xA,xC,xM,numax=1):
    
    numeros= []
    Xn = int(x0) 
    a = xA
    c = xC
    m = xM
    
    for iterator in range(numax):        
        Xn_1 = (a*Xn + c)% m        
        out = float(Xn_1)/float(m)    
        numeros.append(out)
        Xn = Xn_1
    return numeros