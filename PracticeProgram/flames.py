name1= list(input("Enter first name: "))
name2= list(input("Enter second name: "))
str="FLAMES"
Flames={'F':'Friend','L':'Love','A':'Affair','M':'Marriage','E':'Enemy','S':'Sister'}
i = 0
while i < len(name1):
    j = 0
    while j < len(name2):
        if name1[i] == name2[j]:
            name1.pop(i)  # Remove the element at index i
            name2.pop(j)  # Remove the element at index j
            # Reset index because lists have changed
            i = -1  # Reset i to start over
            break  # Exit inner loop
        else:
            j += 1
    i += 1
finalString = name1 + name2
n=len(finalString)
resultIndex=(n-1)%len(str)
keyValue=str[resultIndex]
print(Flames.get(keyValue))










