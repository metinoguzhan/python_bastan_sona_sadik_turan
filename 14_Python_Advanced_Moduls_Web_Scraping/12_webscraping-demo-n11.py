import requests
from bs4 import BeautifulSoup

url = 'https://www.n11.com/bilgisayar/dizustu-bilgisayar'
html = requests.get(url).content

soup = BeautifulSoup(html,"html.parser")

# lists = soup.find('div',{"class":"listView"}).find("ul").find_all("li",{"class","column"})
# for li in lists:
#     title = li.find('h3',{"class":"productName"}).text.strip()
#     print(title)

lists = soup.find_all("li",{"class":"column"},limit = 10)

for li in lists:
    name = li.div.a.h3.text.strip()
    link = li.div.a.get("href")
    oldPrice = li.find("div",{"class":"proDetail"}).find_all("a")[0].text.strip().strip('TL')
    newPrice = li.find("div",{"class":"proDetail"}).find_all("a")[1].text.strip().strip('TL')
    
    print(f"1. name: {name}\n2. link: {link}\n3. old price: {oldPrice}\n4. new price: {newPrice}")
