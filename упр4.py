import numpy as np
import matplotlib.pyplot as plt
with plt.xkcd():
    f = input()
    g = "np." + f
    x = np.arange(-10, 10, 0.01)
    plt.figure(figsize=(9, 6))
    plt.plot(x, eval(g))
    sp = plt.subplot(111)
    sp.spines['left'].set_position('center')
    sp.spines['bottom'].set_position('center')
    sp.spines['top'].set_position('center')
    sp.spines['right'].set_position('center')
    plt.axis('equal')
    plt.xlabel(r'$f(x)$', labelpad=-215)
    plt.ylabel(r'$x$', labelpad=-290, rotation=0)
    plt.show()