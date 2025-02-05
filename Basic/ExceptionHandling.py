from pkgutil import find_loader

a=3
b=0
try:
    print(a/b)
except ZeroDivisionError as e:
    print('you can not do this operation:',e)
finally:
    print('ye to hona hi tha')