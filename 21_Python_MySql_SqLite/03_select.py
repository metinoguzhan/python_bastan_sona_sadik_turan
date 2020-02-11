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

    cursor.execute("SELECT id,name,price,description FROM products")

    # result = cursor.fetchone()
    # print(f"id : {result[0]} name : {result[1]} price : {result[2]} description : {result[3]}")
   
    result = cursor.fetchall()
    
    for product in result:
        print(f"id : {product[0]} name : {product[1]} price : {product[2]} description : {product[3]}")
    connection.close()

getProducts()