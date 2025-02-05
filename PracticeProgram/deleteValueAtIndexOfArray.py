#1) Create an array with 5 values & delete the value at index no. 2 without using in-built function.
from array import *

arr=array('i',[])
arr2=array('i',[])
for i in range(5):
    x=int(input("Enter value in array"))
    arr.append(x)
j=0
for e in arr:
      if j==2:
          pass
      else:
          arr2.append(e)
      j += 1

print(arr2)
