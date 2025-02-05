nam1=input('Enter first name')
nam2=input('Enter second name')
print(nam1)
print(nam2)
length=len(nam1+nam2)
for i in range(length):
    for j in range(i):
     print(nam1[i]+nam2[length-i])
