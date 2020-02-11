import sqlite3

connection = sqlite3.connect("21_Python_MySql_SqLite/chinook/chinook.db")

cursor = connection.cursor()
cursor.execute("SELECT * FROM customers")
result = cursor.fetchall()

for i in result:
    print(i)


connection.close()