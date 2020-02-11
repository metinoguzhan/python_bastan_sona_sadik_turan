'''
ogrenciler = {
    '120' : {
        'ad' : 'Ali',
        'soyad' : 'Yılmaz',
        'telefon' : '532 000 00 01'
    },
    '125' : {
        'ad' : 'Can',
        'soyad' : 'Korkmaz',
        'telefon' : '532 000 00 02'
    },
    '128' : {
        'ad' : 'Volkan',
        'soyad' : 'Yükselen',
        'telefon' : '532 000 00 03'
    },
}

'''

student = {}
number = input('Öğrenci No Giriniz : ')
ad = input('İsim Giriniz : ')
soyad = input('Soyad Giriniz : ')
telefon = input('Telefon Giriniz : ')


# student[number] = {
#     'ad' : ad,
#     'soyad' : soyad,
#     'telefon' : telefon
#     }
# }

student.update({
    number:{
         'ad' : ad,
    'soyad' : soyad,
    'telefon' : telefon
    }
})


number = input('Öğrenci No Giriniz : ')
ad = input('İsim Giriniz : ')
soyad = input('Soyad Giriniz : ')
telefon = input('Telefon Giriniz : ')

student.update({
    number:{
         'ad' : ad,
    'soyad' : soyad,
    'telefon' : telefon
    }
})


number = input('Öğrenci No Giriniz : ')
ad = input('İsim Giriniz : ')
soyad = input('Soyad Giriniz : ')
telefon = input('Telefon Giriniz : ')

student.update({
    number:{
         'ad' : ad,
    'soyad' : soyad,
    'telefon' : telefon
    }
})

print('*'*50)

value = input('Öğrenci No : ')
ogrenci = student[value] 


print(f'Aradığınız {value} nolu öğrencinin adı : {ogrenci["ad"]} - öğrencinin soyad : {ogrenci["soyad"]} - öğrencinin telefon : {ogrenci["telefon"]}')
