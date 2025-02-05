class Teacher:
    def showResult(self):
        print('Teacher showing result')
class Student(Teacher):
    def showResult(self):
        print('Student showing result')

s1=Student()
s1.showResult()