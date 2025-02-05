#Write a code to add 2  arrays using for loop
from array import*
arr1=([1,4,3,6])
arr2=([2,-1,1,-2])
arr3=([0,0,0,0])
for i in range(4):
     arr3[i]= arr1[i]+arr2[i]
print(arr3)


