"""
@Conmix
@param seed
@param numax  { generator n numbers random}
@return {array with N elements random }
"""
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
