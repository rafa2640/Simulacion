
import numpy as np

def Conmix(numax=1):
    nums= []
    Xn = 7
    a = 7
    c = 1
    m = 16547
    
    
    for iterator in range(numax):        
        Xn_1 = (a*Xn + c)% m        
        out = float(Xn_1)/float(m)    
        nums.append(out)
        Xn = Xn_1
    return nums


def aleatvalue(N,x,pobrax):
    
    X = []
    u =  Conmix(N)    
    P = np.cumsum(pobrax)    
    

    print "------"
    for index in range(N):
        for i in range (1,len(P)):
           
            if(u[index]<P[0] ):
                X.append(x[0])
                break
                
            if(u[index]<P[i] and u[index]>=P[i-1]  ):                
                X.append(x[i-1])
                break
            
                
    return X