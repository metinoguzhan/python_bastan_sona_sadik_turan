import mysql.connector


def getProductInfo():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        auth_plugin='mysql_native_password',
        database = "node-app"
    )

    cursor = connection.cursor()
    # sql = "SELECT COUNT(*) FROM products"
    # sql = "SELECT AVG(Price) FROM products"
    # sql = "SELECT SUM(Price) FROM products"
    # sql = "SELECT MIN(Price) FROM products"
    # sql = "SELECT MAX(Price) FROM products"
    # sql = "SELECT name FROM products WHERE price = (SELECT MAX(Price) FROM products)"



    cursor.execute(sql)

    result = cursor.fetchone()

    print(f"result : {result[0]}")

getProductInfo()