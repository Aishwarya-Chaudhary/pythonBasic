#A perfect number is a positive integer
# that is equal to the sum of its proper divisors, excluding the number itself.
def checkPerfect(n):
    divisors=[]
    if n>0:
        for i in range(1,n):
            if n%i==0:
                divisors.append(i)
        return sum(divisors)==n


num=int(input('Enter a Number'))
if checkPerfect(num):
    print(f'{num} is a perfect number')
else:
    print(f'{num} is a NOT perfect number')