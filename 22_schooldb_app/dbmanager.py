import mysql.connector
from datetime import datetime
from connection import connection
from Models.Student import Student
from Models.Teacher import Teacher
from Models.Class import Class

class DbManager:

    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()
    
    def getStudentById(self,id):
        sql = "SELECT * FROM student WHERE Id = %s"
        value = (id,)

        self.cursor.execute(sql,value)

        try:
            obj = self.cursor.fetchone()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print("Error : ",err)

    def getStudentsByClassId(self,classId):
        sql = "SELECT * FROM student WHERE ClassId = %s"
        value = (classId,)

        self.cursor.execute(sql,value)

        try:
            obj = self.cursor.fetchall()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print("Error : ",err)

    def addorEditStudent(self,student:Student):
        if student.id == 0:
            sql = """
                 INSERT INTO student (
                    StudentNumber,
                    Name,
                    Surname,
                    BirthDate,
                    Gender,
                    ClassId
                )VALUES(%s,%s,%s,%s,%s,%s)
            """
            values = (student.studentNumber,student.name,student.surname,student.birthdate,student.gender,student.classId)
        else:
            sql = """
                UPDATE
                    student
                SET
                    StudentNumber = %s,
                    Name = %s,
                    Surname = %s,
                    BirthDate = %s,
                    Gender = %s,
                    ClassId = %s
                WHERE Id = %s
            """
            values = (student.studentNumber,student.name,student.surname,student.birthdate,student.gender,student.classId,student.id)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt eklendi veya güncellendi..")
        except mysql.connector.Error as err:
            print("Hata oluştu : ",err)    
    
    def addStudent(self,student:Student):
        sql = """
            INSERT INTO student (
                StudentNumber,
                Name,
                Surname,
                BirthDate,
                Gender,
                ClassId
                )VALUES(%s,%s,%s,%s,%s,%s)
        """
        values = (student.studentNumber,student.name,student.surname,student.birthdate,student.gender,student.classId)
        self.cursor.execute(sql,values)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt eklendi")
        except mysql.connector.Error as err:
            print("hata : " , err)

    def getClasses(self):
        sql = "SELECT * FROM class"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Class.CreateClass(obj)
        except mysql.connector.Error as err:
            print("Error : ",err)

    def editStudent(self,student:Student):
        sql = """
            UPDATE
                student
            SET
                StudentNumber = %s,
                Name = %s,
                Surname = %s,
                BirthDate = %s,
                Gender = %s,
                ClassId = %s
            WHERE Id = %s
        """
        values = (student.studentNumber,student.name,student.surname,student.birthdate,student.gender,student.classId,student.id)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt güncellendi.")
        except mysql.connector.Error as err:
            print("hata oluştu : ",err)
    
    def deleteStudent(self,student:Student):
        sql = "DELETE FROM student WHERE id = %s"
        values = (student.id,)

        self.cursor.execute(sql,values)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt silindi")
        except mysql.connector.connect as err:
            print("Hata oluştu : " , err)

    def addTeacher(self,teacher:Teacher):
        pass

    def editTeacher(self,teacher:Teacher):
        pass
    
    def __del__(self):
        self.connection.close()
        print("db silindi...")


db = DbManager()


# student = db.getStudentById(7)
# print(student[0].name)
# print(student[0].surname)
#################################################
# students = db.getStudentsByClassId(1)
# for student in students:
#     print(student.name,student.surname)
#################################################

# std = Student(None,"3265","Metin","Oğuzhan",datetime(1986,3,16),'E',1)
# db.addStudent(std)

#################################################
# student = db.getStudentById(7)
# student[0].name = "Emre"
# student[0].surname = "Yaşar"

# db.editStudent(student[0])



#################################################
# student = db.getStudentById(8)
# student[0].name = "Mehmet"
# student[0].surname = "Öztürk"
# db.addorEditStudent(student[0])

#################################################
# student = Student(None,"123622541","Ersin","Vergili",datetime(1987,1,1),'E',1)
# db.addorEditStudent(student)

#################################################