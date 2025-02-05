def fac(n):
 fac=1
 while n>0:
    fac=n*fac
    n-=1
def recursionFac(n):
    if n==0:
        return 1
    return n*recursionFac(n-1)
num=int(input('Enter a number'))
print(recursionFac(num))