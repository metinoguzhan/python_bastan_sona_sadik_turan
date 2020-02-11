print(5000 - (5000 *0.27))
print(4000 - (4000 *0.27))


maasAli = 5000
maasAhmet = 4000
vergi = 0.27

print("Net Ali Maası : " + str(maasAli - (maasAli * vergi)))
print("Net Ahmet Maası : " + str(maasAhmet - (maasAhmet * vergi)))


# Değişken Tanımlama Kuralları

#sayısal ile başlayamaz
#buyuk kucuk harf duyarlılıgı vardır.
#türkce karakter kullanmayalım.

number1 = 10
print(number1)
number1 = 20
print(number1)

number1 += 30
print(number1)


age = 10
AGE = 20
print(age)
print(AGE)


x = 1   #int
y = 2.3 #float
name = "Çınar"  #string
isStudent = True #bool


a = '10'
b = '20'
print(a + b)

firstName = "Metin"
lastName = " Oğuzhan"
print(firstName + lastName)


x,y,name,isStudent = (1,2,"Mustafa",False)
print(x)
print(y)
print(name)
print(isStudent)