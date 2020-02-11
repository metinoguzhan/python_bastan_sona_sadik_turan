#***********************************Sayfa 11 karakterden itibaren güncelleme
# with open("F:/Egitim/Python/SadikTuran/10_Python_Dosya_Islemleri/files/newfile.txt","r+",encoding="utf-8") as file:
#     file.seek(11)
#     file.write("deneme")
#     file.close()

# with open("F:/Egitim/Python/SadikTuran/10_Python_Dosya_Islemleri/files/newfile.txt","r+",encoding="utf-8") as file:
#     print(file.read())
#     file.close()


#***********************************Sayfa sonunda güncelleme
# with open("F:/Egitim/Python/SadikTuran/10_Python_Dosya_Islemleri/files/newfile.txt","a",encoding="utf-8") as file:
#     file.write("\nEmre Yaşar")
#     file.close()

#***********************************Sayfa başına güncelleme
# with open("F:/Egitim/Python/SadikTuran/10_Python_Dosya_Islemleri/files/newfile.txt","r+",encoding="utf-8") as file:
#     content = file.read()
#     content = "Efe Turan\n" + content
#     file.seek(0)
#     file.write(content)
#     file.close



#***********************************Sayfa ortasında güncelleme
# with open("F:/Egitim/Python/SadikTuran/10_Python_Dosya_Islemleri/files/newfile.txt","r+",encoding="utf-8") as file:
#     liste = file.readlines()
#     liste.insert(len(liste)//2,"Ersin Vergili\n")
#     file.seek(0)
#     file.writelines(liste)
#     file.close()


#***********************************Sayfa ortasında güncelleme
with open("F:/Egitim/Python/SadikTuran/10_Python_Dosya_Islemleri/files/newfile.txt","r+",encoding="utf-8") as file:
    liste = file.readlines()
    liste.insert(1,"Ali Vergili\n")
    file.seek(0)
    for i in liste:
        file.write(i)

        

# with open("F:/Egitim/Python/SadikTuran/10_Python_Dosya_Islemleri/files/newfile.txt","r+",encoding="utf-8") as file:
#     print(file.read())
#     file.close()