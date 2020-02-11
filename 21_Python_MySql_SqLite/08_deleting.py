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
        print("database bağlantısı kapandı..")    

def deleteProduct(id):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="node-app",
        auth_plugin="mysql_native_password"
    )
    
    try:
        cursor = connection.cursor()
        sql="DELETE FROM products WHERE id = %s"
        params = (id,)
        cursor.execute(sql,params)
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt silindi")
    except mysql.connector.Error as err:
        print("hata : ",err)
    finally:
        connection.close()
        print("database bağlantısı kapandı..") 

deleteProduct(8)
getProducts()