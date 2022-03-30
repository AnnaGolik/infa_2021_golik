import numpy as np
import matplotlib.pyplot as plt
with plt.xkcd():
    x = np.arange(-10, 10, 0.4)
    plt.figure(figsize=(9, 6))
    sp = plt.subplot(111)
    sp.spines['left'].set_position('center')
    sp.spines['bottom'].set_position('center')
    sp.spines['top'].set_position('center')
    sp.spines['right'].set_position('center')
    plt.plot(x, eval(input()))
    plt.show()
