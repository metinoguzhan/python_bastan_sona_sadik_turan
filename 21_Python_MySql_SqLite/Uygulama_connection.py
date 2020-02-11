import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    auth_plugin='mysql_native_password',
    database = "node-app"
)


