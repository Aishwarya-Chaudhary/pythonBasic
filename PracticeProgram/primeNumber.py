x=int(input("Give a number to check if it is prime"))
if x<=1:
    print("Not a prime number")
else:
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
           print("Not a prime number")
           break
        else:
           print("A prime number")
