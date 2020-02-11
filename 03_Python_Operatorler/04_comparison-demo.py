# 1 - Girilen 2 sayıdan hangisi büyüktür ?
'''
sayi1 = int(input("1. Sayı : "))
sayi2 = int(input("2. Sayı : "))

result = (sayi1 > sayi2)
print(f"sayı 1 : {sayi1} Sayi 2 : {sayi2} den büyüktür : {result}")
'''

# 2 - Kullanıcıdan 2 Vize (%60) ve Final (%40) notunu alıp ortalama hesaplayınız
    # Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın
'''
vize1 = int(input("vize 1 :"))
vize2 = int(input("vize 2 :"))
final = int(input("Final : "))

result = (((vize1 + vize2) // 2) * 0.6) + (final * 0.4)
isSuccess = result>=50
print(f"not ortalamanız : {result} ve dersten geçme durumunuz : {isSuccess}")
'''

# 3 - Girilen sayının tek mi çiftmi oldugunu yazdırın 
'''
sayi = int(input("Sayı giriniz : "))
result = (sayi % 2 == 0)
print("Girilen sayı çift mi :{}".format(result))
'''

# 4 - Girilen bir sayının negatif pozitif durumunu yazdırın
'''
sayi = int(input("Sayı giriniz : "))
result = sayi < 0
print(f"Sayının negatif durumu : {result}")
'''

# 5 - Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#       (email : email@sadikturan.com parola : abc123)
email = 'email@sadikturan.com'
password = 'abc123'

girilenEmail = input('email : ')
girilenPassword = input('password : ')

isEmail = email == girilenEmail.lower().strip()
isPasword = password == girilenPassword.lower().strip()

print(f"Girilen mail geçerlilik durumu : {isEmail} Girilen password geçerlilik durumu : {isPasword}")