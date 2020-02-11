import mysql.connector

def getProducts():
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "password",
        auth_plugin='mysql_native_password',
        database = "node-app"
    )

    cursor = connection.cursor()
    try:
        result = cursor.execute("SELECT * FROM products ORDER BY price DESC")
        result = cursor.fetchall()
        for product in result:
           print(f"id : {product[0]} name : {product[1]} price : {product[2]} description : {product[3]}")
    except mysql.connector.Error as err:
        print("hata : ",err)
    finally:
        connection.close()
        print("database bağlantısı kapandı")
   


getProducts()