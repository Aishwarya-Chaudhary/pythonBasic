def merge(l1,l2):
     In_lst1 = list(map(int, l1.split()))
     In_lst2 = list(map(int, l2.split()))
     s1=sorted(In_lst1)
     s2=sorted(In_lst2)
     l3=sorted(s1+s2)
     return l3

lst1=input('enter list 1 give space in between')
lst2=input('enter list 2 give space in between')
print(merge(lst1,lst2))
