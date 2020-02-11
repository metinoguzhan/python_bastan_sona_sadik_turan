import mysql.connector


def getProductById(id):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "password",
        auth_plugin='mysql_native_password',
        database = "node-app"
    )

    cursor = connection.cursor()
    sql = "SELECT * FROM products WHERE id=%s"
    params = (id,)
    cursor.execute(sql,params)

    result = cursor.fetchone()
    print(f"id : {result[0]} name : {result[1]} price : {result[2]} description : {result[3]}")
    connection.close()

getProductById(1)
getProductById(2)



def getProducts():
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "password",
        auth_plugin='mysql_native_password',
        database = "node-app"
    )

    cursor = connection.cursor()

    # cursor.execute("SELECT id,name,price,description FROM products WHERE id = 1")
    # cursor.execute("SELECT id,name,price,description FROM products WHERE name = 'Samsung S6'")
    # cursor.execute("SELECT id,name,price,description FROM products WHERE name = 'Samsung S8'")
    # cursor.execute("SELECT id,name,price,description FROM products WHERE name = 'Samsung S7' and price>2999")
    # cursor.execute("SELECT id,name,price,description FROM products WHERE name = 'Huawei' or price>5000")
    # cursor.execute("SELECT id,name,price,description FROM products WHERE name LIKE '%Samsung%'")
    # cursor.execute("SELECT id,name,price,description FROM products WHERE name LIKE 'Samsung%'")
    # cursor.execute("SELECT id,name,price,description FROM products WHERE name LIKE '%Samsung'")
    cursor.execute("SELECT id,name,price,description FROM products WHERE name LIKE '%Samsung%' and price=3000")
    
    
    # cursor.execute("SELECT id,name,price,description FROM products WHERE id = 1")
    # result = cursor.fetchone()
    # print(f"id : {result[0]} name : {result[1]} price : {result[2]} description : {result[3]}")



    result = cursor.fetchall()

    for product in result:
        print(f"id : {product[0]} name : {product[1]} price : {product[2]} description : {product[3]}")
    
    connection.close()

# getProducts()