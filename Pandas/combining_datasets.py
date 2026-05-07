import pandas as pd

data1_dict = {
    'PatientID': [1, 2, 3, 4, 5],
    'Pregnancies': [6, 1, 8, 1, 0],
    'Glucose': [148, 85, 183, 89, 137]
}
df1 = pd.DataFrame(data1_dict).set_index('PatientID')

data2_dict = {
    'PatientID': [6, 7, 8],
    'Pregnancies': [5, 3, 10],
    'Glucose': [116, 78, 115]
}
df2 = pd.DataFrame(data2_dict).set_index('PatientID')

data3_dict = {
    'PatientID': [1, 2, 3, 6, 10], 
    'BMI': [33.6, 26.6, 23.3, 25.8, 30.0],
    'Age': [50, 31, 32, 21, 33]
}
df3 = pd.DataFrame(data3_dict)

data1 = pd.concat([df1, df2])
print("Shape after concat:", data1.shape)
print(data1)

df_left = pd.merge(data1, df3, on='PatientID', how='left')
df_outer = pd.merge(data1, df3, on='PatientID', how='outer')
df_inner = pd.merge(data1, df3, on='PatientID', how='inner')

print("\nInner join shape:", df_inner.shape)
print("Результат Inner Join (тільки спільні ID):")
print(df_inner)

print("\nOuter join shape:", df_outer.shape)
print("Результат Outer Join (всі ID з обох таблиць):")
print(df_outer)
