import numpy as np
import matplotlib.pyplot as plt
xx, yy = np.meshgrid(np.arange(10), np.arange(10), indexing='ij')

plt.scatter(xx,yy)
plt.show()