import numpy as np
import matplotlib.pyplot as plt

data = [np.random.normal(0, std, 100) for std in range(1, 4)]

fig, ax = plt.subplots()
ax.boxplot(data, vert=True, patch_artist=True)
ax.set_title('Box Plot Example')
ax.set_xlabel('Dataset')
ax.set_ylabel('Value')
ax.set_xticklabels(['Std 1', 'Std 2', 'Std 3'])
plt.show()
