import mysql.connector


def getProducts():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        auth_plugin="mysql_native_password",
        database="node-app"
    )
    cursor = connection.cursor()
    # sql = "SELECT * FROM products"
    # sql = "SELECT * FROM categories"
    # sql = "SELECT * FROM products INNER JOIN categories ON categories.id = products.categoryid"
    # sql = "SELECT products.name,products.price,categories.name FROM products INNER JOIN categories ON categories.id = products.categoryid"
    sql = """SELECT products.name,products.price,categories.name 
        FROM products INNER JOIN categories ON categories.id = products.categoryid
        WHERE categories.name = 'Telefon'
        """
    sql = """SELECT products.name,products.price,categories.name 
        FROM products INNER JOIN categories ON categories.id = products.categoryid
        WHERE products.name = 'samsung s8'
        """
    sql = """SELECT p.name,p.price,c.name 
        FROM products AS p INNER JOIN categories AS c ON c.id = p.categoryid
        WHERE p.name = 'samsung s8'
        """

    cursor.execute(sql)
    try:

        result = cursor.fetchall()
        for product in result:
            print(product)
    except mysql.connector.Error as err:
        print("Hata : ", err)
    finally:
        connection.close()
        print("database bağlantısı kapandı..")


getProducts()
