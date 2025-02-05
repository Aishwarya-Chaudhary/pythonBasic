from abc import ABC,abstractmethod
class student:
    @abstractmethod
    def show(self):
       pass
class teacher(student):
    def show(self):
        print('show teacher')
t1=teacher()
t1.show()