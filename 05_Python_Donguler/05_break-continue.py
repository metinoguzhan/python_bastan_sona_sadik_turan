'''
name = 'Sadık Turan'

for letter in name:
    if letter == 'ı':
        break
    print(letter)

for letter in name:
    if letter == 'a':
        continue
    print(letter)
'''
'''
x = 0

while x <= 5:
    if x == 2:
        break
    print(x)
    x += 1
'''

'''
number = 0

while number<5:
    number += 1
    if number == 3:
        continue
    print(number)
'''

number = 0 
sum = 0
while number<=100:
    number+=1
    if number % 2 == 0:
        continue
    sum += number
        

print(f"1'den 100'e kadar tek sayıların toplamı : {sum}")