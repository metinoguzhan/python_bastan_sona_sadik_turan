numbers = [1,2,3,4,5]

for num in numbers:
    print(num)


names = ['çınar','sadık','sena']

for name in names:
    print(f"My name is {name}")


name = "Sadık Turan"

for n in name:
    print(n)


tuple = (1,2,3,4,5)

for t in tuple:
    print(t)


tuple = [(1,2),(3,4),(4,5),(9,10)]

for t in tuple:
    print(t)

for a,b in tuple:
    print(a,b)

d = {
    'k1' : 1,
    'k2' : 2,
    'k3' : 3
}

for key,value in d.items():
    print(key,value)