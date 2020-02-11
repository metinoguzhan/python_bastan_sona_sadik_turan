

tuple = (1,'iki',3)     #tuple = 1,'üç',True

print(type(tuple))
print(tuple[1])
print(len(tuple))


tuple = ("damla","ayse","damla")
print(tuple)

#tuple[0] = "Mehmet"  HATA VERİR..ELEMAN DEĞİŞİKLİĞİ YAPMAMIZA İZİN VERMEZ..AMA SIFIRDAN ATAMA YAPARIZ
print(tuple)
print(tuple.count("damla"))




names = ("ali","rıza","veli") + tuple  
print(names)