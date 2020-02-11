#function 
'''
def sayHello():
    print('Hello')
'''

'''
def sayHello(name='user'):
    print(f'Hello, {name}')

sayHello("Metin")
sayHello('Emre')
sayHello('Ersin')
sayHello()
'''

'''
def sayHello(name = 'user'):
    return 'hello ' + name

msg = sayHello('Emre')

print(msg)
print(sayHello('Metin'))
print(sayHello())
'''

'''
def total(num1,num2):
    return num1 + num2

result = total(3,5)
print('Total is ' + str(result))
'''


import datetime

def yasHesapla(dogumYili):
    return datetime.datetime.now().year - dogumYili

metin = yasHesapla(1986)
print(f'Metin Yaşınız : {metin}')

emre = yasHesapla(1987)
print(f'Emre Yaşınız : {emre}')




def emekliligeKacYilKaldi(dogumYili,isim):
    '''
        DOCSTRING : Dogum yiliniza gore emekliliginize kaç yil kaldi
        INPUT : Dogum yili, isim
        OUTPUT : Hesaplanan yil bilgisi
    '''
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f'Emekliliğinize {emeklilik} yıl kaldı')
    else:
        print('Zaten Emeklisiniz..')

emekliligeKacYilKaldi(1950,'mehmet')
emekliligeKacYilKaldi(1955,'rıfat')
emekliligeKacYilKaldi(1956,'rıfat')

print(help(emekliligeKacYilKaldi))



print(help(list.append))