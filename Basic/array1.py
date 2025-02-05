from array import *
arr=array('i',[])
n=int(input("Enter size of array"))
for i in range(n):
    x=int(input("Enter value in array"))
    arr.append(x)
    i+=1
print(arr)
#search for value comes on which index
num=int(input("Enter the number you want to search"))
k=0
for e in arr:
    if e==num:
     print(k)
     break
    k += 1
print(arr.index(num))
#check change
print('testing git')
