import mysql.connector


def getProducts():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        auth_plugin="mysql_native_password",
        database="node-app"
    )
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM products")
        result = cursor.fetchall()

    for product in result:
        print(product)
    except mysql.connector.Error as err:
        print("Hata : ",err)
    finally:
        connection.close()
        print("database bağlantısı kapandı...")
    


        

def updateProduct(id,name,price):
    connection = mysql.connector.connect(
        host='localhost',
        user="root",
        password="password",
        auth_plugin='mysql_native_password',
        database="node-app"
    )

    cursor = connection.cursor()

    sql = "UPDATE products SET name = %s, price = %s WHERE id = %s"
    params = (name,price,id,)
    cursor.execute(sql,params)

    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt güncellendi")
    except mysql.connector.Error as err:
        print("hata: " + err)
    finally:
        connection.close()
        print("database bağlantısı kapandı..")


updateProduct(1,"IPHONE 5",10000)
getProducts()
