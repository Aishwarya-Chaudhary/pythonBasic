#print first 50 fibonaci numbers
firstValue=0
secondValue=1
print(firstValue)
print(secondValue)
i=1
while i<=50-2:
    x=firstValue + secondValue
    print(x)
    firstValue=secondValue
    secondValue=x
    i+=1


