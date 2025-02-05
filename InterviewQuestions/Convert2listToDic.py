from itertools import zip_longest

keys = ["name", "age", "city"]
values = ["Alice", 25]

# Use zip_longest to handle mismatched lengths
result = dict(zip_longest(keys, values, fillvalue=None))
print(result)  # Output: {'name': 'Alice', 'age': 25, 'city': None}
