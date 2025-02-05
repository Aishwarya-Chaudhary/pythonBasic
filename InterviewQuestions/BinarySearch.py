pos=-1
def search(lst,n):
    l=0
    u=len(lst)-1
    while l<=u:
        mid=(u+l)//2
        if lst[mid]==n:
            globals() ['pos']=mid
            return True
        else:
            if lst[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return False


lst=list(map(int,input('Please enter the values seperated by space').split()))
n=int(input('Enter the value to search in the list'))

if search(lst,n):
    print('found at: ',pos)
else:
    print('Not found')