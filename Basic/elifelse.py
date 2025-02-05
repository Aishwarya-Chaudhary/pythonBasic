#x=int(input('Enter a number to check its even/odd'))
#y=x%2
#if y==0:
#    print("Number %d is even" %(x))
#else:
#    print("Number %d is odd" %(x))
x=float(input("Enter first number"))
y=float(input("Enter second number"))
z=float(input("Enter third number"))
if(x>y):
    if(x>z):
        print("Number %d is greatest number" %(x))
    else:
        print("Number %d is greatest number" %(z))
elif (y > x):
    if (y > z):
        print("Number %d is greatest number" % (y))
    else:
        print("Number %d is greatest number" % (z))
else:
    print("none")