# try:
#     file = open("F:/Egitim/Python/SadikTuran/10_Python_Dosya_Islemleri/files/newfile.txt","r")
#     print(file)
# except FileNotFoundError as err:
#     print("Dosya okuma hatası")
# finally:
#     print("Dosya kapandı.")
#     file.close()


file = open("F:/Egitim/Python/SadikTuran/10_Python_Dosya_Islemleri/files/newfile.txt","r",encoding="utf-8")

#********************************for döngüsü 

# for i in file:
#     print(i,end="")
# file.close()


#********************************read() fonksiyonu 
# content1 = file.read()

# print('İçerik 1')
# print(content1)

# content2 = file.read()
# print("İçerik 2")
# print(content2)

# file.close()
#her bir karakter 1 bayt eşittir.
# content = file.read(5)
# print(content)
# content = file.read(3)
# print(content)
# content = file.read(3)
# print(content)




#******************************************readline() fonksiyon kullanımı
# content = file.readline()
# print(content,end="")

# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")




#******************************************readlines() fonksiyon kullanımı
# liste = file.readlines()
# print(liste)
# print(liste[0],end="")
# print(liste[1],end="")
# print(liste[2],end="")







file.close()