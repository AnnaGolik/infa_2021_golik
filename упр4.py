import numpy as np
import matplotlib.pyplot as plt
with plt.xkcd():
    x = np.arange(-10, 10, 0.1)
    plt.figure(figsize=(9, 6))
    plt.plot(x, eval(input()))
    plt.show()
