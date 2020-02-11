website = "http://www.sadikturan.com"
course = 'Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)'

# 1 'course' karakter dizisinde kaç karakter bulunmaktadır ?
print(f'Course dizisinde toplam {len(course)} karakter vardır.')

# 2 'website' içinden www karakterlerini alın
print(website[7:10])

# 3 'website' içinden com karakterlerini alın
print(website[-3:])


#4 'course' içinden ilk 15 ve son 15 karakterlerini alın.
print(course[0:15])
print(course[:15])
print(course[-15:])


#5 'course' ifadesindeki karakterleri tersten yazdırın.
print(course[len(course)::-1])
print(course[::-1])


#6 Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#   'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis.'
name,surname,age,job = 'Bora','Yılmaz',32,'mühendis'

print("Benim adım {n} {s}, Yaşım {a} ve mesleğim {j}.".format(n=name,s=surname,a=age,j=job))


#7 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
print('Hello world'.replace('w','W'))
s = 'Hello world'
s = s[0:6] + 'W' + s[-4:]
print(f"s değişkenin değeri : {s}")
#8 'abc' ifadesini yan yana 3 defa yazdırın.  
print('abc'*3)




## NOT
s = '12345' * 5  # adım sayısı örneği
print(s[::5])    #1234512345123451234512345 = Her 5 karakterde bir almak sonuc : 1111 