import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 10, 0.01)
plt.figure(figsize=(10,7))
plt.plot(x, x*x - x - 6)
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.grid(True)
plt.show()