import pandas as pd

data = {
    'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
    'last_name': ['Miller', 'Jacobson', '.', 'Milner', 'Cooze'],
    'age': [42, 52, 36, 24, 73],
    'preTestScore': [4, 24, 31, ".", "."],
    'postTestScore': ["25,000", "94,000", 57, 62, 70]
}

df = pd.DataFrame(data)
print("--- 1. DataFrame створено: ---")
print(df)
print("\n")

df.to_csv('example.csv', index=False)
print("--- 2. DataFrame збережено як 'example.csv' ---")
print("\n")

df_read = pd.read_csv('example.csv')
print("--- 3. Дані, прочитані з 'example.csv': ---")
print(df_read)
print("\n")

df_no_header = pd.read_csv('example.csv', header=None)
print("--- 4. Дані, прочитані без заголовків: ---")
print(df_no_header)
print("\n")

df_custom_index = pd.read_csv('example.csv', index_col=['first_name', 'last_name'])
print("--- 5. DataFrame з кастомним індексом: ---")
print(df_custom_index)
print("\n")

df_first_3_rows = pd.read_csv('example.csv').head(3)
print("--- 6. Перші 3 рядки DataFrame: ---")
print(df_first_3_rows)
print("\n")

df['postTestScore'] = df['postTestScore'].astype(str).replace({',': ''}, regex=True).astype(float)
print("--- 7. DataFrame після очищення стовпця 'postTestScore': ---")
print(df)