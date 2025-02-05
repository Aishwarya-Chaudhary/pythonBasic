#A prime number is a number greater than 1 that has no divisors other than 1 and itself.
num=int(input('Enter a Number to find its prime or not? '))
if num<=1:
    print('Not a prime')
for i in range(2,int(num**0.5)+1):
        if(num%i==0):
            print('Not a Prime Number')
            break
else:
 print('Prime number')


