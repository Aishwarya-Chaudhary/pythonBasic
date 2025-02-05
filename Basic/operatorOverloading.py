from numpy.ma.extras import atleast_1d


class student():
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self,a,b):
        self.a=a
        self.b=b
        return a+b

s=student(4,9)
c=s.__add__(2,6)
print(c)