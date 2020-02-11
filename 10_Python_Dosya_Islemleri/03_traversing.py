with open("F:/Egitim/Python/SadikTuran/10_Python_Dosya_Islemleri/files/newfile_02.txt","r",encoding="utf-8") as file:
    content = file.read()
    print(content)
    file.seek(10)    # seek() => cursoru istediğimiz yere göndeririz. 
    print(file.tell())   # tell() => cursor nerede bilgisini verir
    content2 = file.read()
    print(content2)
    file.close()

