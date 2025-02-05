def removeDupes(s):
    result=''
    seen=set()
    for i in s:
        if i not in seen:
            result+=i
            seen.add(i)
    return result
Inputstr1=input('Enter a string: ')
output1=removeDupes(Inputstr1)
print(f'When we remove duplicate character from {Inputstr1} then it becomes {output1}')