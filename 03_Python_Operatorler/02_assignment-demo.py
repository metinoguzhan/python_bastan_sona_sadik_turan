x, y, z = 2, 5, 10
numbers = 1, 5, 7, 10, 6


# 1 - Kullanıcıdan aldınız 2 sayının carpimi ile (x,y,z) toplamının fark nedir.

sayi1 = int(input('Sayı 1 : '))
sayi2 = int(input('Sayı 2 : '))

result = (sayi1 * sayi2) - (x + y + z)
print(result)


# 2 - y' nin x ' e kalansız bölümünü hesaplayınız.
result = y // x
print(result)


# 3 - (x,y,z) toplamının mod 3' ü nedir ?
result = (x+y+z) % 3
print(result)


# 4 - y' nin x. kuvvetini hesaplayınız ?
result = y ** x
print(result)


# 5   x, *y, z = numbers işlemine göre z' nin küpü kaçtır ?
x, *y, z = numbers
result = z ** 3
print(result)

# 6   x, *y, z = numbers işlemine göre y değerleri toplamı kaçtır ?
x, *y, z = numbers
result = sum(y)
print(result)
