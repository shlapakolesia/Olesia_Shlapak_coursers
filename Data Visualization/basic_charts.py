import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips.head())
# Histogram and KDE plot
sns.histplot(tips['total_bill'], kde=True)
plt.title('Distribution of Total Bill')
plt.show()

# Box plot
sns.boxplot(x='day', y='total_bill', data=tips)
plt.title('Box Plot of Total Bill by Day')
plt.show()

# Pair plot
sns.pairplot(tips, hue='day')
plt.show()

# Bar plot
sns.barplot(x='day', y='total_bill', data=tips)
plt.title('Average Total Bill by Day')
plt.show()