#Write a code to find max value from an array without using in-built function
from numpy import*
arr=array([6,156,8,4,9,31,2])
max=0
for i in range(6):
      if max<arr[i]:
        max=arr[i]

print(max)


