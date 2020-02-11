import numpy as np

result = np.array([1,3,5,7,9])
print(result)

result = np.arange(1,10) # 1'den başla 10 kadar ama 10 dahil DEĞİL
print(result)

result = np.arange(10,100,3) #10'dan başla 100' e kadar ama 100 dahil DEĞİL arttırma 3' er 3' er
print(result)


result = np.zeros(10)
print(result)

result = np.ones(10)
print(result)

result = np.linspace(0,100,5)
print(result)

result = np.linspace(0,5,5)
print(result)

result = np.random.randint(0,10)  # 0 ile 10 arasında ama 10 dahil DEĞİL
print(result)

result = np.random.randint(20)   # 0 ile 20 arasında ama 20 dahil DEĞİL
print(result)

result = np.random.randint(1,10,3)  # 1 ile 10 arasında tabiki 10 dahil DEĞİL rastgele 3 tane sayı
print(result)


result = np.random.rand(5)  # 0 ile 1 arasında 5 tane sayı 
print(result)

result = np.random.randn(5) # negatif sayılarda işin içine katılır
print(result)


np_array = np.arange(50)
np_multi = np_array.reshape(5,10)
print(np_multi)
print(np_multi.sum(axis=1))  # np_multi'nin satırlarının toplamını verir.
print(np_multi.sum(axis=0))  # np_multi'nin sütunlarının toplamını verir.



print("****************")
print("****************")
rnd_numbers = np.random.randint(1,100,10)
print(rnd_numbers)
result = rnd_numbers.max()    # en büyük
print(result)
result = rnd_numbers.min()    # en küçük
print(result)
result = rnd_numbers.mean()   # ortalama
print(result)

#en büyük sayının indeks numarası
result = rnd_numbers.argmax()
print(result)
#en küçük sayının indeks numarası
result = rnd_numbers.argmin()
print(result)