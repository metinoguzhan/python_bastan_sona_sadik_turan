import mysql.connector


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    auth_plugin='mysql_native_password',
    database = "node-app"
)

# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE mydatabase")

# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)

# print(mydb)

# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE customers(name VARCHAR(255),address VARCHAR(255))")