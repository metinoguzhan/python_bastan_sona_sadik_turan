import mysql.connector

def insertProduct(name,price,imageUrl,description):
    connection = mysql.connector.connect(
        host="localhost",
        user = "root",
        password = "password",
        auth_plugin='mysql_native_password',
        database = "node-app"
    )
    cursor = connection.cursor()

    sql = "INSERT INTO products (name,price,imageUrl,description) VALUES(%s,%s,%s,%s)"
    values = (name,price,imageUrl,description)
    cursor.execute(sql,values)
    
    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi")
        print(f"son eklenen kaydın id numarası : {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata: ", err)
    finally:
        connection.close()
        print("Database bağlantısı kapandı...")


def insertProducts(liste):
    connection = mysql.connector.connect(
        host="localhost",
        user = "root",
        password = "Metin!4532",
        auth_plugin='mysql_native_password',
        database = "node-app"
    )
    cursor = connection.cursor()

    sql = "INSERT INTO products (name,price,imageUrl,description) VALUES(%s,%s,%s,%s)"
    values = liste
    cursor.executemany(sql,values)
    
    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi")
        print(f"son eklenen kaydın id numarası : {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata: ", err)
    finally:
        connection.close()
        print("Database bağlantısı kapandı...")


liste = []
while True:
    name = input("Name : ")
    price = input("Price : ")
    imageUrl = input("Image Url : ")
    description = input("Description : ")
    # insertProduct(name,price,imageUrl,description)
    
    
    liste.append((name,price,imageUrl,description))

    result = input("devam etmek istiyor musunuz? (e/h)")
    if result == 'h':
        print("Kayıtlarınız veri tabanına aktarılıyor...")
        print(liste)
        insertProducts(liste)
        break
  
    
