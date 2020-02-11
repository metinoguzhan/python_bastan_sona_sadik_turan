website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

#1 - ' Hello World   ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
result = '    Hello World     '
print(result.strip())

#lstrip()
#rstrip() kullanılabilir...

#2 - "www.sadikturan.com" içindeki sadikturan bilgisi haricindeki her karakteri silin
result = website.replace('http://www.','').replace('.com','')
print(result)

teacher = 'www.sadikturan.com'.strip('w.com')
print("Teahcer : " + teacher)

#3 - 'course' karakter dizisinin tüm karakterlerini küçük harf yapın
result = course.lower()
print(result)


#4 - 'website' içinde kaç tane a karakteri vardır..
#  website.count('a',0,10) 0 ile 10 karakter arasında ara demek
result = website.count('a')
print(result)


#5 - 'website' www ile başlayıp com ile bitiyor mu ?
result = website.startswith('www')
print(result)
result = website.endswith('.com')
print(result)

#6 - 'website' içinde .com ifadesi var mı ?
result = website.find('.com')
print(result)
result = course.rfind("Python")  # aramaya sondan başlar
print(str(result) + " değeri")

# index eğere aranan değer yoksa hata fırlatır..
result = website.index('.com')
result = website.rindex('.com')
print(result)

#7 - 'course' içindeki karakterlerin hepsi alfabetik mi ? (isalpha,isdigit) 
result = course.isalpha()
print(result)

#8 - 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyin
result = 'Contents'.center(50,'*')
print(result)
result = 'Contents'.ljust(50,'*')
print(result)
result = 'Contents'.rjust(50,'*')
print(result)

#9 - 'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin
result = course.replace(' ','-')
print(result)
result = course.replace(' ','-',3)
print(result)

#10 - 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
result = 'Hello World'.replace('World','There')
print(result)


#11 - 'course' karakter dizisinin boşluk karakterlerinden ayırın
result = course.split(' ')
print(result)