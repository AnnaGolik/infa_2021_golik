import numpy as np

def sentence(x):
    for i in range(3):
        a = (np.log((1/np.e**(np.sin(x[i])+1))/(5/4+1/x[i]**15))/np.log(1 + x[i]**2))
        print(a)
    return a

x = [1, 10, 1000]
y=sentence(x)
