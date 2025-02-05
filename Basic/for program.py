#print 20 to 11 in decending oder
"""for i in range(20,10,-1):
    print(i)"""
#print all the perfect sqaure number between 1-500
from math import isqrt
for i in range(1,501):
    if isqrt(i) * isqrt(i) == i :
        print(i)