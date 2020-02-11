# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi,dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.


# "w": (Write) yazma modu. 
#    ** Dosyayı konumda oluşturur. 
#    ** Dosya içeriğini siler ve yeniden ekleme yapar. 

# file = open('newfile.txt','w')
# file = open("F:/Egitim/Python/SadikTuran/10_Python_Dosya_Islemleri/files/newfile.txt","w")
# file.close()
# print(file)

# file = open("F:/Egitim/Python/SadikTuran/10_Python_Dosya_Islemleri/files/newfile.txt","w",encoding="utf8")
# file.write("Metin Oğuzhan\nNasılsın iyimisin")
# file.close()


# "a": (Append) ekleme. Dosya konumda yoksa oluşturur.
# file = open("F:/Egitim/Python/SadikTuran/10_Python_Dosya_Islemleri/files/newfile.txt","a",encoding="utf8")
# file.write("\nSadık Turan\nMetinOğuzhan")
# file.close()


# "x": (Create) oluşturma. Dosya zaten varsa hata verir.
# file = open("F:/Egitim/Python/SadikTuran/10_Python_Dosya_Islemleri/files/newfile_02.txt","x",encoding="utf8")


# "r": (Read) okuma. varsayılan. dosya konumda yoksa hata verir.
