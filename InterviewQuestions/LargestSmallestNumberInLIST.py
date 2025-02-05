lst=input('Enter a List seperated by space: ')
In_lst=lst.split()
In_lst=list(map(int,In_lst))
print('Max Value: ',max(In_lst))
print('Min Value: ',min(In_lst))

def maxiVal(x):
    max=0
    for i in x:
      if i>=max:
          max=i
      else:
          continue
    return max
def miniVal(x):
    min=0
    for i in x:
      if i<=min:
          min=i
      else:
          continue
    return min


print('By def Max Value: ',maxiVal(In_lst))
print('By def Min Value: ',miniVal(In_lst))

