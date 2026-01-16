import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

arr = np.loadtxt("x_y.txt")
x = arr[0:]
y = arr[1:]

plt.plot(arr, '-o')
plt.show()

print('Done!')
