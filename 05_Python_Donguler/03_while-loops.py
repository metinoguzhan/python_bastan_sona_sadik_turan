# 1-100 e kadar

x = 1
while x <= 100:
    if x % 2 == 0:
        print("Çift Sayı : ",x)
    else:
        print("Tek Sayı : ",x)
    x += 1
print('bitti...')



name = ''   #False

while not name.strip():
    name = input('isminizi giriniz : ')

print("Merhaba, ",name)