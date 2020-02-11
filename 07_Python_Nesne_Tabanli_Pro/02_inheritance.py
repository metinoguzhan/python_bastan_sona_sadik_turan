#Inheritance (Kalıtım) : Miras alma


#Person => name, lastName, age, eat(), run(), drink()


#Student(Person) Teacher(Person)

#Animal => Dog(), Cat()

class Person:
    def __init__(self,firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        print('Person Created')
    
    def who_am_i(self):
        print("I am a person")
    
    def eat(self):
        print('I am eating')

class Student(Person):
    def __init__(self,firstName, lastName,number):
        Person.__init__(self,firstName, lastName)
        self.number = number
        print('Student Created')
   
    #override
    def who_am_i(self):
        print("I am a student")
    
    #override
    def eat(self):
        print('I am eating (student)')

    def sayHello(self):
        print('Hello I am a student')


class Teacher(Person):
    def __init__(self,firstName,lastName,branch):
        super().__init__(firstName,lastName)
        self.branch = branch
    
    def who_am_i(self):
        print(f"I am a {self.branch} teacher ")



p1 = Person('metin','oğuzhan')
s1 = Student('emre','yasar',1450)

print(p1.firstName + " " + p1.lastName)
print(s1.firstName + " " + s1.lastName + " " + str(s1.number))

p1.who_am_i()
s1.who_am_i()

p1.eat()
s1.eat()

s1.sayHello()


t1 = Teacher('İsmail','Sertkaya','Chemistry')
print(t1.firstName + " " + t1.lastName + " " + t1.branch)
t1.who_am_i()