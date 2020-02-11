import json
import os

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}

        # load users from .json file
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists('14_Python_Advanced_Moduls_Web_Scraping/data/users.json'):
            with open('14_Python_Advanced_Moduls_Web_Scraping/data/users.json','r',encoding='utf-8') as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username=user["username"],password=user["password"],email=user["email"])
                    self.users.append(newUser)
            for user in self.users:
                print(user.username,user.email)
    

    def register(self, user: User):
        self.users.append(user)
        self.savetoFile()
        print("Kullanıcı oluşturuldu.")

    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print("Çıkış Yapıldı.")

    def identity(self):
        if self.isLoggedIn:
            print(f'username: {self.currentUser.username}')
        else:
            print('giriş yapılmadı.')

    def login(self,username,password):
       
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print('login yapıldı..')
                break

    def savetoFile(self):
        liste = []

        for user in self.users:
            liste.append(json.dumps(user.__dict__))

        with open('14_Python_Advanced_Moduls_Web_Scraping/data/users.json', 'w',encoding='utf-8') as file:
            json.dump(liste, file)


repository = UserRepository()

while True:
    print("Menü".center(50, "*"))
    secim = input(
        "1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\nSeçiminiz: ")
    if secim == '5':
        break
    else:
        if secim == '1':
            # register
            username = input("username: ")
            password = input("password: ")
            email = input("email: ")

            user = User(username=username, password=password, email=email)
            repository.register(user)

        elif secim == '2':
            # login
            if repository.isLoggedIn:
                print("Zaten login oldunuz..")
            else:
                username = input('username: ')
                password = input('password: ')
                repository.login(username,password)
        elif secim == '3':
            # logout
            repository.logout()
        elif secim == '4':
            # display user name
            repository.identity()
        else:
            print('yanlış seçim')
