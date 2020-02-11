import os 
import datetime

# result = dir(os)
# print(result)


# result = os.name
# print(result)

# result = os.getcwd()
# print(result)

# # os.mkdir('klasor')

# os.chdir('C:\\')

# os.mkdir() => dosya oluşturma
# os.mkdir('deneme')

# os.chdir => dizin değiştirme
# os.chdir('..')


# os.getcwd() => Etkin dizin öğrenme


# result = os.getcwd()
# print(result)

# os.makedirs("klasor/yeni") => klasör içine klasör oluşturma
# result = os.makedirs("klasor/yeni")
# print(result)


# listeleme
# result = os.listdir()
# print(result)


# listeleme 
# result = os.listdir('c:\\')
# print(result)



# filtreleme işlemi yapmak
# for dosya in os.listdir():
#     if dosya.endswith('.py'):
#         print(dosya)


result = os.stat('13_Python_Generators/01_generators.py')
# print(result)

# result = result.st_size/1024
# print(result)

#dosyanın oluşturulma zamanı
# result = datetime.datetime.fromtimestamp(result.st_ctime)
# print(result)

#dosya son erişilme tarihi
# result = datetime.datetime.fromtimestamp(result.st_atime)
# print(result)


#dosya değiştirilme tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime)
# print(result)



#program çalıştırma
# os.system('notepad.exe')


# klasör adını değiştirme
# os.rename('deneme','değişti')

# os.rmdir('değişti')


#klasör içindeki klasörüde siler
# os.removedirs('avs/ddd')


#path sınıfı
# result = os.path.abspath("os/demo.py")
# print(result)


# result = os.path.dirname('F:\Egitim\Python\SadikTuran\os\demo.py')
# print(result)

# result = os.path.dirname(os.path.abspath('os/demo.py'))
# print(result)

# result = os.path.exists('os/demo.py')
# print(result)

# result = os.path.exists('os')
# print(result)


# result = os.path.isdir('os')
# print(result)

# result = os.path.isfile('os')
# print(result)

# result = os.path.join('c:\\','data','sql')
# print(result)

# result = os.path.split('F:\\Egitim\\Python')
# print(result)

# result = os.path.splitext('os/demo.py')
# print(result)