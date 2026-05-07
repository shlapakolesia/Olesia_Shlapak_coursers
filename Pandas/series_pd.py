import pandas as pd
import numpy as np

x = [42, -10, 8, 25] 
series_from_list = pd.Series(x)
print("Series from list:")
print(series_from_list)

array = np.array([15, 4.5, 9, 12]) 
series_from_array = pd.Series(array, index=['A', 'B', 'C', 'D'])
print("\nSeries from array:")
print(series_from_array)

values = series_from_array.values
index = series_from_array.index
print("\nValues:", values)
print("Index:", index)

print("\nElement 'B':", series_from_array['B'])

series_from_array['C'] = 99
print("After modification:")
print(series_from_array)

names = ['Anna', 'Peter', 'olesya', 'Max']
series_names = pd.Series(names)
print("\nNames Series:")
print(series_names)
