def dupVal(x):
    seen=set()
    dup=set()
    for i in x:
         if i in seen:
          dup.add(i)
         else:
          seen.add(i)

    return list(dup)

lst=input('Enter a List seperated by space: ')
In_lst=lst.split()
In_lst=list(map(int,In_lst))
print('Duplicate list Value: ',dupVal(In_lst))