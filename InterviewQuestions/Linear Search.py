pos=-1
def search(lst,n):
    for i in range(len(lst)):
        if lst[i]==n:
            globals()['pos']=i
            return True
    return False
lst=list(map(int,input("Enter the array elements separated by space: ").split()))
n=int(input('Enter a number to search'))

if search(lst,n):
    print('found at position: ',pos+1)
else:
    print('Not found')