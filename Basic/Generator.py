def topten():
    yield 4
    yield 3
    yield 2
    yield 1
val=topten()
print(val.__next__())
for i in val:
    print(i)