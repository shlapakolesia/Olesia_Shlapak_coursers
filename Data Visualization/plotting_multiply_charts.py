import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)
categories = ['A', 'B', 'C', 'D']
values = [15, 30, 45, 10]
data1 = np.random.randn(1000)
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Line plot
axs[0, 0].plot(x, y, label='sin(x)', color='blue')
axs[0, 0].set_title('Sine Function')
axs[0, 0].legend()

# Scatter plot
axs[0, 1].scatter(x, y, color='red')
axs[0, 1].set_title('Random Scatter Plot')

# Bar plot
axs[1, 0].bar(categories, values, color='purple')
axs[1, 0].set_title('Bar Plot Example')

# Histogram
axs[1, 1].hist(data1, bins=30, color='green', alpha=0.7)
axs[1, 1].set_title('Histogram of Random Data')

plt.tight_layout()

plt.savefig('my_plot.png', dpi=300, bbox_inches='tight')

plt.show()
