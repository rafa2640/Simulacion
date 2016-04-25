def MidSquare(semilla, numax=1):

    numeros= []
    semillautil = semilla
    for iterator in range(numax):

        if(len(semillautil)%2==0):

            n = int(semillautil)
            semilla2 = n**2
            stringc =  str(semilla2)
            if len(stringc)%2!=0:
                stringc = "0"+ stringc


            border = len(semillautil)/2

            semillanueva = stringc[border:len(stringc)-border]            
            output = "0."+ semillanueva
            numeros.append(float(output))
            semillautil = semillanueva
        else:
            print "error"
        

    return numeros

def Conmix(x0, numax=1):
    numeros= []
    Xn = int(x0)    
    
    a = 5
    c = 7
    m = 1277    
    
    for iterator in range(numax):        
        Xn_1 = (a*Xn + c)% m
        numeros.append(Xn_1)
        Xn = Xn_1
    return numeros