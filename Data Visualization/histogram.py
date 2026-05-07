import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(100)

fig, ax = plt.subplots()
ax.hist(data, bins=30, color='green', alpha=0.7)
ax.set_title('Histogram of Random Data')
ax.set_xlabel('Value')
ax.set_ylabel('Frequency')
ax.grid(True)
plt.show()
