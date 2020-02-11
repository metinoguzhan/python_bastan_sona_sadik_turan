html_doc = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>İlk Web Sayfam</title>
</head>
<body>
    <h1 id="header">
        Python Kursu
    </h1>
    <div class="group1">
        <h2>Programlama</h2>
        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>
    <div class="group2">
        <h2>Modüller</h2>
        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>
    <div class="group3">
        <h2>Django</h2>
        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>
    <img src="https://upload.wikimedia.org/wikipedia/tr/b/bb/Fred_%C3%87akmakta%C5%9F.jpg" alt="Fred Çakmaktaş">
    
    <a class="sister" href="http://example1.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example2.com/lacie" id="link2">Lacie</a>
    <a class="sister" href="http://example3.com/tillie" id="link3">Tillie</a>

</body>
</html>
 """

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc,'html.parser')
result = soup.prettify()
# print(result)

# result = soup.title
# print(result)

# result = soup.head
# print(result)

# result = soup.body
# print(result)

# result = soup.title.string
# print(result)

# result = soup.h1
# print(result)

# result = soup.h1.string
# print(result)


# result = soup.h2    #ilk h2 yi bulur
# print(result)

# result = soup.h2.name
# print(result)

# result = soup.h2.string
# print(result)


# result = soup.find_all('h2')
# print(result)
# print(result[0])
# print(result[1])


# result = soup.div
# print(result)

# result = soup.find_all('div')
# print(result)
# print(result[0])
# print(result[1])

# result = soup.find_all('div')[1].ul.li.string


# result = soup.find_all('div')[1].ul.find_all('li')
# # print(result)


# for item in result:
#     print(item.string)

# result = soup.div.findChildren()
# print(result)


# result = soup.div.findNextSibling().findNextSibling().findPreviousSibling()
# print(result)

result = soup.find_all('a')
# print(result)
for link in result:
    print(link.get('href'))

for link in result:
    print(link.get('id'))
