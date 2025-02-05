class A:
    def __init__(self):
        print('in a init')

    def f1(self):
        print('in a f1')
class B:
    def __init__(self):
        print('in B init')

    def f2(self):
        print('in a f2')
class C(A,B):
    def __init__(self):
        super().__init__()
        print('in C init')

    def f3(self):
            print('in a f3')
c1=C()
c1.f1()