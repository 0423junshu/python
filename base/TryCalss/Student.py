class Student:

    def __init__(self,age,name):
        self.age=age
        self.name=name

    def getAge(self):
        print(self.age)

    def getName(self):
        print(self.name)



class MathStudent(Student):
    pass
