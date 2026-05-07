import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y, label='sin(x)', color='blue')
ax.set_title('Sine Function')
ax.set_xlabel('X values')
ax.set_ylabel('sin(x)')
ax.legend()
ax.grid(True)
plt.show()

np.random.seed(0)
x = np.random.rand(50)
y = np.random.rand(50)

fig, ax = plt.subplots()
ax.scatter(x, y, color='red')
ax.set_title('Random Scatter Plot')
ax.set_xlabel('X values')
ax.set_ylabel('Y values')
ax.grid(True)
plt.show()

categories = ['A', 'B', 'C', 'D']
values = [3, 7, 2, 5]

fig, ax = plt.subplots()
ax.bar(categories, values, color='purple')
ax.set_title('Bar Plot Example')
ax.set_xlabel('Categories')
ax.set_ylabel('Values')
plt.show()
