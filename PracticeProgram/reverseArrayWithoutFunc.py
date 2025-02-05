#2) write a code to reverse an array without using in-built function.
from array import *
arr=array('i',[])
n=int(input("Enter length of array"))
for i in range(n):
    x=int(input("Enter value in array"))
    arr.append(x)
print("before reverse ",arr)
for i in range(n):
    for j in range(n):
        if arr[i]>arr[j]:
             arr[i],arr[j]=arr[j],arr[i]
print("after reverse ",arr)