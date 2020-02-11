names = ["Ali", "Yağmur", "Hakan", "Deniz"]
years = [1998, 2000, 1998, 1987]

# 1 - "Cenk" ismini listenin sonuna ekleyiniz. 
names.append('Cenk')
# 2 - "Sena" değerini listenin başına ekleyiniz.
names.insert(0,'Sena')
# 3 - "Deniz" ismini listeden siliniz.
names.remove('Deniz')
# 4 - "Hakan" isminin indexi nedir
result = names.index("Hakan")
print(result)
# 5 - "Ali" listenin bir elemanımıdır
result = 'Ali' in names
print(result)
# 6 - Liste elemanlarını ters çevirin
names.reverse()
# 7 - Liste elemanlarını alfabetik olarak sıralayınız
names.sort()
# 8 - years listesini rakamsal büyüklüğe göre sıralayınız
years.sort()
print(years)
# 9 - str = 'Chevrolet,Dacia' karakter dizisini listeye çeviriniz.
str = 'Chevrolet,Dacia'
result = str.split(',')
print(result)
# 10 - years dizisinin en büyük ve en küçük elemanı nedir ?
minYear = min(years)
maxYear = max(years)
print(f'{minYear} - {maxYear}')
print(minYear,maxYear)
# 11 - years dizisinde kaç tane 1998 değeri vardır
print(years.count(1998))
# 12 - years dizisinin tüm elemanlarını siliniz.
years.clear()
# 13 - kullanıcıdan alacağınız 3 tane marka bilgisini listede saklayınız.



markalar = []

marka = input("marka : ")
markalar.append(marka)

marka = input("marka : ")
markalar.append(marka)

marka = input("marka : ")
markalar.append(marka)

print(markalar)


# print(names)

