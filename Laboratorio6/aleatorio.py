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


def dados(N,x,px):
    
    X = []
    u =  Conmix(N)    
    Probx = np.cumsum(px)    
    

    print "*****************************************************************************************************************************"
    for inicio in range(N):
        for i in range (1,len(Probx)):
           
            if(u[inicio]<Probx[0] ):
                X.append(x[0])
                break
                
            if(u[inicio]<Probx[i] and u[inicio]>=Probx[i-1]  ):                
                X.append(x[i-1])
                break
            
                
    return X