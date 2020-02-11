'''
Soru: Girilen bir sayının asal olup olmadığını bulun.
** Asal Sayı 1 ve kendisi hariç tam böleni olmayan 
   sayılara denir. 
'''
sayi = int(input('sayi giriniz : '))

isPrime = True

if sayi == 1:
    isPrime = False

for i in range(2,sayi):
    if sayi % i == 0:
        isPrime = False
        break

if isPrime:
    print('sayi asaldır.')
else:
    print('sayı asal değildir.')