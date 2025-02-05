num=[6,8,5,3]
it=iter(num)
print(it.__next__())
print(next(it))
for i in num:
    print(i)
print('*************')
"""To create your own iterator"""
class topten:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration

values =topten()
print(next(values))
for i in values:
    print(i)

