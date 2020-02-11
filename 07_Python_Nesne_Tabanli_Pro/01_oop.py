# Object Oriented Programming (OOP)
# class => Person(name,yearOfBirth,job,calculateAge())


class Person:
    # class attribute
    address = 'no information'

    # constructor (yapıcı metod)
    def __init__(self, name, year):
        # object attributes
        self.name = name
        self.year = year
        print('init metodu çalıştı..')

    # instance methods
    def intro(self):
        print('hello there, I am ' + self.name)
    # instance methods

    def calculateAge(self):
        return 2020-self.year


#instance (object)
p1 = Person(name='metin', year=1986)
p2 = Person('emre', 1987)
p2.address = 'Bağcılar'

# updating
p1.name = 'Mustafa'
p1.year = 1970

# accessing object attributes
print(f'name : {p1.name}  year : {p1.year} address : {p1.address}')
print(f'name : {p2.name}  year : {p2.year} address : {p2.address}')


p1.intro()
p2.intro()

print("adım : {} ve yaşım : {}".format(p1.name, p1.calculateAge()))
print("adım : {} ve yaşım : {}".format(p2.name, p2.calculateAge()))


print(type(p1))
print(type(p2))
print(p1 == p2)


class Circle:
    # Class object attribute
    pi = 3.14

    def __init__(self, yaricap=1):
        self.yaricap = yaricap

    def cevreHesapla(self):
        return 2 * self.pi * self.yaricap
    
    def alanHesapla(self):
        return self.pi * (self.yaricap**2)

c1 = Circle() #yaricap = 1
c2 = Circle(5)


print(f"c1 alan : {c1.alanHesapla()} c1 cevre : {c1.cevreHesapla()}")
print(f"c2 alan : {c2.alanHesapla()} c2 cevre : {c2.cevreHesapla()}")