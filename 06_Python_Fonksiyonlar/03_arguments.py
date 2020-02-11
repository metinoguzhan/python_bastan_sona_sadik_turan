#value types
def changeName(n):
    n = 'ada'

name = 'yiğit'


print(name)
changeName('Metin')
print(name)



#reference types
def change(n):
    n[0] = 'İstanbul'


sehirler = ['Ankara','İzmir']

change(sehirler)
print(sehirler)


n = sehirler
n[0] = 'Van'
print(sehirler)


#dizi elemanlarını kopylama işlemi yapılır
n = sehirler[:]
n[1] = "Muş"
print(sehirler)
print(n)


change(sehirler[:])
print(sehirler)
print(n)




def add(a, b, c = 0, d = 0, e = 0):
    return sum((a,b,c))

print(add(10,20,30))
print(add(10,20))



def sumToplam(*params):
    print(params)
    print(params[0])
    print(params[1])
    print(params[2])
    return sum((params))

print(sumToplam(10,20,30))



def sumTopla2 (*params):
    sum = 0 
    for n in params:
        sum += n
    return sum
    
print(sumTopla2(10,20,30))


def displayUser(**args):
    for key,value in args.items():
        print('{} is {}'.format(key,value))



displayUser(name = 'Çınar', age = 2, city = 'istanbul')
displayUser(name = 'Ada', age = 12, city = 'kocaeli')
displayUser(name = 'Yiğit', age = 14, city = 'ankara',email = 'yigit@gmail.com')


def myFunc(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,60,70,key1 = 'value 1',key2 = 'value 2')
