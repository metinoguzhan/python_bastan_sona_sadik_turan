from mysql.connector import Error
from datetime import datetime
from Uygulama_connection import connection


# 1- Workbench IDE ile schooldb isminde bir database oluşturup Student tablosunu ekleyiniz.
# Id,StudentNumber,Name,Surname,Birthdate,Gender

"""
        CREATE TABLE `node-app`.`Student`(  
        `Id` INT NOT NULL AUTO_INCREMENT,
        `StudentNumber` VARCHAR(5) NOT NULL,
        `Name` VARCHAR(45) NOT NULL,
        `Surname` VARCHAR(50) NOT NULL,
        `BirthDate` DATETIME,
        `Gender` CHAR(1),
        PRIMARY KEY (`Id`),
        UNIQUE INDEX `StudentNumber_UNIQUE` (`StudentNumber` ASC) VISIBLE
        );
"""


# 2- Database bağlantısını oluşturunuz. (Uygulama_connection.py)

# Uygulama_connection.py içerisinde oluşturuldu

# 3- Aşağıdaki bilgiler için insert sorguları oluşturup kayıtları ekleyiniz.

# ("301","Ahmet","Yılmaz",datetime(2005, 5, 17),"E"),
# ("302","Ali","Can",datetime(2005, 6, 17),"E"),
# ("303","Canan","Tan",datetime(2005, 7, 7),"K"),
# ("304","Ayşe","Taner",datetime(2005, 9, 23),"K"),
# ("305","Bahadır","Toksöz",datetime(2004, 7, 27),"E"),
# ("306","Ali","Cenk",datetime(2003, 8, 25),"E")

# 4- Aşağıdaki sorguları yazınız.
#   a- Tüm öğrenci kayıtlarını alınız.
#   b- Tüm öğrencilerin sadece öğrenci no, ad ve soyad bilgilerini alınız.
#   c- Sadece kız öğrencilerin ad ve soyadlarını alınız.
#   d- 2003 doğumlu öğrenci bilgilerini alınız.
#   e- İsmi Ali ve doğum tarihi 2005 olan öğrenci bilgilerini alınız.
#   f- ad veya soyadı içinde 'an' ifadesi geçen kayıtları alınız.
#   g- Kaç erkek öğrenci vardır ?
#   h- Kız öğrencileri harf sırasına göre getiriniz.

# 5- Aşağıdaki güncelleme sorularını yapınız.
#   a- id' e göre aldığınız bir öğrencinin bilgilerini güncelleyiniz.
#   b- cinsiyet' e göre aldığınız bir öğrencinin bilgilerini güncelleyiniz.


class Student:
    connection = connection
    mycursor = connection.cursor()

    def __init__(self, id , studentNumber, name, surname, birthdate, gender):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    def saveStudent(self):
        sql = 'INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES(%s,%s,%s,%s,%s)'
        value = (self.studentNumber, self.name,
                 self.surname, self.birthdate, self.gender)

        try:
            Student.mycursor.execute(sql, value)
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt eklendi.")
        except errors.Error as err:
            print("hata bilgisi oluştu : ", err)
        finally:
            Student.connection.close()
            print("Database bağlantısı kapandı...")

    @staticmethod
    def saveStudents(students):
        sql = 'INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES(%s,%s,%s,%s,%s)'
        values = students

        try:
            Student.mycursor.executemany(sql, values)
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt eklendi.")
        except Error as err:
            print("hata bilgisi oluştu : ", err)
        finally:
            Student.connection.close()
            print("Database bağlantısı kapandı...")

    @staticmethod
    def studentInfo():
        # sql = "SELECT * FROM student LIMIT 5"
        # sql = "SELECT studentNumber,name,surname FROM student"
        # sql = "SELECT studentNumber,name,surname FROM student where gender ='K'"
        # sql = "SELECT studentNumber,name,surname FROM student where YEAR(BirthDate) = 2003"
        # sql = "SELECT studentNumber,name,surname FROM student where YEAR(BirthDate) = 2005 and name = 'Ali'"
        # sql = "SELECT studentNumber,name,surname FROM student where name LIKE '%an%' or surname LIKE '%an%'"
        # sql = "SELECT COUNT(*) FROM student where gender = 'K'"
        sql = "SELECT studentNumber,name,surname FROM student where gender = 'K' ORDER BY name,surname DESC"

        try:
            Student.mycursor.execute(sql)
            result = Student.mycursor.fetchall()
            for student in result:
                print(f"{student[0]} {student[1]} {student[2]}")
                # print(f"{student[0]}")
        except Error as err:
            print("Hata : ", err)
        finally:
            Student.connection.close()
            print("Database bağlantısı kapandı...")

    @staticmethod
    def getStudentById(id):
        sql ="SELECT * FROM student WHERE Id = %s"
        value = (id,)
        

        try:
            Student.mycursor.execute(sql,value)
            obj = Student.mycursor.fetchone()
            return Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5])
        except Error as err:
            print("hata : ",err)
        
    def updateStudent(self):
        sql = "Update Student set StudentNumber = %s, Name = %s, Surname = %s, BirthDate = %s, gender = %s WHERE Id = %s"
        values = (self.studentNumber,self.name,self.surname,self.birthdate,self.gender,self.id)

        Student.mycursor.execute(sql,values)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt güncellendi.")
        except Error as err:
            print("hata",err)
    
    @staticmethod
    def getStudentGender(gender):
        sql ="SELECT * FROM student WHERE Gender = %s"
        value = (gender,)
        

        try:
            Student.mycursor.execute(sql,value)
            return Student.mycursor.fetchall()
             
        except Error as err:
            print("hata : ",err)   
    
    @staticmethod
    def updateStudents(liste):
        sql = "Update Student set StudentNumber = %s, Name = %s, Surname = %s, BirthDate = %s, gender = %s WHERE Id = %s"
        values = []
        order = [1,2,3,4,5,0]

        for item in liste:
            item = [item[i] for i in order]
            values.append(item)

        Student.mycursor.executemany(sql,values)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt güncellendi.")
        except Error as err:
            print("hata",err)



# students = Student.getStudentGender('E')
# print(students)

# liste = []
# for std in students:
#     std = list(std)
#     std[2] = 'Mr ' + std[2]
#     liste.append(std)

# Student.updateStudents(liste)



# student = Student.getStudentById(8)
# student.name = "Metin"
# student.surname = "Oguzhan"
# student.updateStudent() 



# Student.studentInfo()




# ahmet = Student("603","Ahmet","Yılmaz",datetime(2005, 5, 17),"E")
# ahmet.saveStudent()



# ogrenciler = [
#         ("701","Ahmet","Yılmaz",datetime(2005, 5, 17),"E"),
#         ("702","Ali","Can",datetime(2005, 6, 17),"E"),
#         ("703","Canan","Tan",datetime(2005, 7, 7),"K"),
#         ("704","Ayşe","Taner",datetime(2005, 9, 23),"K"),
#         ("705","Bahadır","Toksöz",datetime(2004, 7, 27),"E"),
#         ("706","Ali","Cenk",datetime(2003, 8, 25),"E")
# ]
# Student.saveStudents(ogrenciler)

