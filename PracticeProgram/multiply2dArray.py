from numpy import *
arr1=array([
[1,2,3],
[4,5,6]])
arr2=arr1.reshape(3,2)
arr3=ones((2,2))
for i in range(2):
    for j in range(2):
        c=0
        for k in range(3):
            f=arr1[i][k]*arr2[k][j]
            c=c+f
        arr3[i][j]=c
print(arr3)

#using numpy matrix
m1=matrix('1 2 3;4 5 6')
m2=matrix('1 2;3 4;5 6')
m3=m1*m2
print(m3)