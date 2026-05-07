import pyodbc
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER=your_server;'
                      'DATABASE=your_database;'
                      'UID=your_username;'
                      'PWD=your_password')

cursor = conn.cursor()
cursor.execute('''
CREATE TABLE Employees (
    EmpID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Department VARCHAR(50)
)
''')
conn.commit()

cursor.execute('''
INSERT INTO Employees (EmpID, FirstName, LastName, Department)
VALUES (1, 'Some', 'Name', 'DA')
''')
conn.commit()

cursor.execute('SELECT * FROM Employees')
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute('''
UPDATE Employees
SET Department = 'Finance'
WHERE EmpID = 1
''')
conn.commit()

cursor.execute('''
DELETE FROM Employees
WHERE EmpID = 1
''')
conn.commit()
