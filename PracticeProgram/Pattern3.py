"""Print pattern :
1  2  3  4
2  3  4
3  4
4
"""
for i in range(1,5):
    for j in range(i,5):
      print(i," ",end="")
      i=i+1
    print()