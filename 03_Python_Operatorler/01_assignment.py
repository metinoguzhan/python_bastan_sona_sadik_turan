# x = 5
# y = 10
# z = 20

x, y, z = 5, 10, 20

x, y = y, x

x = x + 5
x += 5
x -= 5
x *= 5
x /= 5
x %= 5
z //= 6   #VİRGÜLDEN SONRASINI GÖRMEZDEN GELMEK İÇİN 
y **= 5   #ÜSSÜNÜ ALMA 

print(x, y, z)



values = 1,2,3   #tuple liste
a, b, c = values
print(values)
print(type(values))


print(a)
print(b)
print(c)


# a, b, c, d = values  HATALI KULLANIM

values = 1,2,3,4,5
x,y,*z = values

print(x,y,z)

print(x,y,z[0],z[1])