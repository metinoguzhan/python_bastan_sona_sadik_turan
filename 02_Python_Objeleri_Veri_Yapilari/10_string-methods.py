message = "Hello There. My name is Sadık Turan"

# message = message.upper()
# message = message.lower()
# message = message.title()
# message = message.capitalize()

# message = message.strip()         #trim işlemi yapılıyor..
# message = message.split()
# message = message.split('.')        #string ifadeyi diziye çevirmek

# message = message.split()
# message = ' '.join(message)

# index = message.find('Sadık')   # aranan değer yoksa -1 döner
# print(index)

#isFound = message.startswith('H')
# isFound = message.endswith('n')
# print(isFound)

message = message.replace('Sadık','Çınar')
message = message.replace(' ','*').replace('ç','c').replace('ö','o')
message = message.center(50,"/")

print(message)