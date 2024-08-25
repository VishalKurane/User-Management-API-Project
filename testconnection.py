import pyodbc

server = 'localhost\\SQLEXPRESS'
database = '________________' 
username = '________________'
password = '________________'

connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# print(connection_string)

try:
    with pyodbc.connect(connection_string) as conn:
        print("Connection successful!")
except Exception as e:
    print("Connection failed: ", e)
