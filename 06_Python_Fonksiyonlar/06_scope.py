# global scope
x = 'global x'

def function():
    #local scope
    #x = 'local x'
    print(x)


function()
print(x)


#########################

#global
name = "Çınar"

def changeName(new_name):
    #local
    name = new_name
    print(name)

changeName('Metin')
print(name)


#########################
name = 'global string'

def greeting():
    #name = 'Çınar'

    def hello():
        #name = 'Ada'
        print('hello ' + name)
    
    hello()

greeting()



#########################
x = 50

def test(x):
    print(f'x : {x}')

    x = 100
    print(f'changed x to {x}')

test(x)
print(x)


#########################
a = 50

def test2():
    global a
    print(f'x : {a}')

    a = 100
    print(f'changed x to {a}')

test2()
print()