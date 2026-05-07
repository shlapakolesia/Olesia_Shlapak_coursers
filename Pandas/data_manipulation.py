import pandas as pd

df = pd.read_csv('diabetes_sample.csv')

print(df.isnull())
print(df.Insulin.isnull())

df.Insulin = df.Insulin.fillna(df.Insulin.mean())

df.duplicated()

df.duplicated(['PatientID'])
