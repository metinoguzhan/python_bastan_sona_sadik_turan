from dbmanager import DbManager
from datetime import datetime
from Models.Student import Student
class App:
    def __init__(self):
        self.db = DbManager()

    def initApp(self):
        msg = "*****\n1-Öğrenci Listesi\n2-Öğrenci Ekle\n3-Öğrenci Güncelle\n4-Öğrenci Sil\n5-Öğretmen Ekle\n6-Sınıflara Göre Dersler\n7-Çıkış(E/Ç)"
        while True:
            print(msg)
            islem = input("Seçim : ")
            if islem == '1':
                self.displayStudents()
            elif islem == '2':
                self.addStudent()
            elif islem == '3':
                self.editStudent()
            elif islem == '4':
                self.deleteStudent()    
            elif islem == 'E' or islem == 'Ç':
                break
            else:
                print("yanlış seçim")

    def displayClasses(self):
        classes = self.db.getClasses()
        for sinif in classes:
            print(f'{sinif.id} : {sinif.name}')

    def displayStudents(self):
        self.displayClasses()
        classid = int(input("hangi sınıf :"))
        students = self.db.getStudentsByClassId(classId=classid)
        print("\n\nÖĞRENCİ LİSTESİ\n")
        for index,std in enumerate(students):
            print(f'{std.id}- {std.name} {std.surname}')
        return classid

    def addStudent(self):
        self.displayClasses()
        classid = int(input("hangi sınıf :"))
        studentNumber = input("Numara: ")
        name = input("Ad: ")
        surname = input("Soyad: ")
        
        year = int(input("Doğum Tarihi Yılı: "))
        month = int(input("Doğum Tarihi Ay: "))
        day = int(input("Doğum Tarihi Gün: "))
        birthdate = datetime(year,month,day) 


        gender = input("Cinsiyet (E/K): ")

        student = Student(None,studentNumber,name,surname,birthdate,gender,classid)
        self.db.addStudent(student)

    def editStudent(self):
        classid = self.displayStudents()
        studentid = int(input("Öğrenci id : "))
        student = self.db.getStudentById(studentid)
        
        student[0].name = input('adı : ') or student[0].name
        student[0].surname = input('soyadı : ') or student[0].surname
        student[0].gender = input('cinsiyet (E/K) : ') or student[0].gender
        student[0].classId = input('Sınıf : ') or student[0].classId

        year = input("Doğum Tarihi Yılı: ") or student[0].birthdate.year 
        month = input("Doğum Tarihi Ay: ") or student[0].birthdate.month
        day = input("Doğum Tarihi Gün: ") or student[0].birthdate.day

        birthdate = datetime(year,month,day) 

        student[0].birthdate = datetime(year,month,day)
        self.db.editStudent(student[0])

    def deleteStudent(self):
        classid = self.displayStudents()
        studentid = int(input("öğrenci no : "))

        student = self.db.getStudentById(studentid)
        self.db.deleteStudent(student[0])


app = App()
app.initApp()