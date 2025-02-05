x='ABCD'
y='PQR'
for i in range(4):
    print(x[:i+1]+y[i:] ,end="")
    print()