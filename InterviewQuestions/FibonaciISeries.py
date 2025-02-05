def fib(n):
  first=0
  second=1
  if n==1:
    print(first)
  else:
    print(first)
    print(second)
    for i in range(2,n):
      nex = first+second
      first=second
      second=nex
      print(nex)

fib(int(input('Enter Fibonaci series lenght')))

