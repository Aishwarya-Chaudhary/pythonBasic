import math
def isArmStrong(n):
    str_n=str(n)
    Len_n=len(str_n)
    total=0
    for i in str_n:
      total = total+(math.pow(int(i),Len_n))
    return total == n # n is compared here since n is int and total is int but str_n is a string

num=int(input('Enter a number to check if its a armstrong number or not?'))
if isArmStrong(num):
    print(f'{num} is a Armstrong Number')
else:
    print(f'{num} is not a Armstrong Number')