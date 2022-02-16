import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 10, 0.01)
plt.figure(figsize=(7,7))
a= 1+np.tan(1/(1+(np.sin(x))**2))
b=(x**2+1)*np.exp(-np.abs(x)/10)
c=np.log(b)/np.log(a)
plt.plot(x, c)
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.grid(True)
plt.show()
