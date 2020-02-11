class Student:

    def __init__(self,id,studentNumber,name,surname,birthdate,gender,classId):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.studentNumber = studentNumber
        self.name = name 
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
        self.classId = classId
    
    @staticmethod
    def CreateStudent(obj):
        liste = []

        if isinstance(obj,tuple):
            liste.append(Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5],obj[6]))
        else:
            for i in obj:
                liste.append(Student(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        return liste