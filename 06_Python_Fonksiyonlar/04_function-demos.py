# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.
'''
word = input('word : ')
count = int(input('count : ')) 

def yazdir(word,count):
    for n in range(0,count):
        print(word)

yazdir(word,count)

def yazdir2(word,count):
    print(word*count)

yazdir2(word+'\n',count)
'''
# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazınız.
'''
def listeyeCevir(*params):
    liste = params
    return liste

print(listeyeCevir('meti','oguzhan',1986,'metinoguzhan@gmail.com'))
    
def listeyeCevir2(*params):
    liste = []
    for n in params:
        liste.append(n)
    return liste    
print(listeyeCevir2(10,20,30,40,50,60,'Merhaba'))
'''

# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.

'''
def asalSayiBulma(baslangic, bitis):
    asalSayiListesi = []
    isPrime = True


    for n in range(baslangic, bitis+1):
        if(baslangic>1):
            for bolen in range(2, n):
                if n % bolen == 0:
                    isPrime = False
                    break
                else:
                    isPrime = True
            else:
                isPrime = True
            if isPrime:
                asalSayiListesi.append(n)

    return asalSayiListesi


print(asalSayiBulma(2, 19))


def asalSayilariBul(sayi1, sayi2):
    for sayi in range(sayi1, sayi2+1):
        if(sayi1>1):
            for i in range(2,sayi):
                if sayi % i == 0:
                    break
            else:
                print(sayi)
                
sayi1 = int(input('sayı 1 : '))
sayi2 = int(input('sayı 2 : '))

asalSayilariBul(sayi1,sayi2)
'''
# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürünüz.



def tamBolenListesi(sayi):
    for n in range(1,sayi + 1):
        if(sayi % n == 0):
            print(n)
        else:
            continue

sayi = int(input('sayı : '))
tamBolenListesi(sayi)


def tamBolenleriBul(sayi):
    tamBolenler = []

    for i in range(2,sayi):
        if(sayi % i == 0):
            tamBolenler.append(i)
    return tamBolenler

print(tamBolenleriBul(90))