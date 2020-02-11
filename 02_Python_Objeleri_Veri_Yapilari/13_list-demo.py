# 1 - "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.

cars = ["Bmw", "Mercedes", "Opel", "Mazda"]
print(cars)

# 2 - Listede kaç eleman vardır.
result = len(cars)
print(result)


# 3 - Listenin ilk ve son elemanları nelerdir.
result = cars[0]
print(result)

result = cars[len(cars)-1]
print(result)


#4 - Mazda değerini toyota ile değiştirin 
cars[3] = "Toyota"    #cars[-1] = "Toyota"
print(cars)

#5 - Mercedes listenin bir elemanımıdır ?
result = 'Mercedes' in cars
print(result)

#6 - Listenin -2 indeksindeki değer nedir ?
print(cars[-2])


#7 - Listenin ilk 3 elemanını alın..
result = cars[:3]   #result = cars[0:3]
print(result)


#8 - Listenin son 2 elemanı yerine Totoya ve Renault değerlerini ekleyin 
# cars[len(cars)-2] = "Totoya"
# cars[len(cars)-1] = "Renault"
# print(cars)
cars[-2:] = ["Toyota","Renault"]
print(cars)

#9 - Listenin üzerine 'Audi' ve 'Nissan' değerlerini ekleyin
# cars.insert(len(cars),'Audi')
# cars.insert(len(cars),'Nissan')
cars += ['Audi','Nissan']
print(cars)


#10 - Listenin son elemanını silin
# cars.remove(cars[len(cars) - 1])
del cars[-1]
print(cars)

#11 - Liste elemanlarını tersten yazınız
cars.reverse()   #cars[::-1]
print(cars)

# 12 - Aşağıdaki verileri bir liste içinde saklayınız
    #studentA : Yiğit Bilgi 2010, (70,60,70)
    #studentB : Sena Turan 1999, (80,80,70)
    #studentC : Ahmet Turan 1998, (80,70,90)

studentA = ['Yiğit', 'Bilgi',2010,[70,60,70]]
studentB = ['Sena ','Turan',1999,[80,80,70]]
studentC = ['Ahmet','Turan',1998,[80,70,90]]

# 13 - Liste elemanlarını ekrana yazınız..
students = [studentA] + [studentB] + [studentC]
print(students)

notOrtalamasi = sum(studentA[3]) / len(studentA[3])
result = f"{studentA[0]} {studentA[1]} {2020-studentA[2]} yaşında ve bu kişinin not ortalaması {notOrtalamasi:3.4}"
print(result)