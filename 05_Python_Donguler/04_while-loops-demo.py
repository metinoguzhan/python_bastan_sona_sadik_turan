sayilar = [1, 3, 5, 7, 9, 12, 19, 21]

# 1: sayilar listesini while ile ekrana yazdırın.
i = 0
while i < len(sayilar):
    print(sayilar[i])
    i += 1

# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm
#    tek sayıları ekrana yazdırın.

baslangic = int(input("baslangic degeri : "))
bitis = int(input('bitis degeri : '))

while baslangic <= bitis:
    if baslangic % 2 == 1:
        print(baslangic)
    baslangic += 1

# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.
i = 100
while i > 0:
    print(i)
    i -= 1

# 4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde
#    yazdırın.

sayilar = []

i = 0
while i < 5:
    sayilar.append(int(input(f'{(i+1)}. sayıyı giriniz : ')))
    i += 1
sayilar.sort()
print(sayilar)


# 5: Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#    ** ürün sayısını kullanıcıya sorun.
#    ** dictionary listesi yapısı (name, price) şeklinde olsun.
#    ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

urunler = []

adet = int(input("kaç ürün eklemek istiyorsunuz: "))

i = 0
while i < adet:
    name = input("ürün ismi:")
    price = input("ürün fiyatı:")

    urunler.append({
        'name' : name,
        'price' : price
    })
    i+=1

for urun in urunler:
     print(f'ürün adı: {urun["name"]} ürün fiyatı: {urun["price"]}')