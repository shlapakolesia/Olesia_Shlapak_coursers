import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips.head())

sns.scatterplot(x='total_bill', y='tip', data=tips, hue='day')
plt.title('Scatter Plot of Tip vs Total Bill')
plt.show()

sns.lineplot(x='total_bill', y='tip', data=tips)
plt.title('Line Plot of Tip vs Total Bill')
plt.show()
