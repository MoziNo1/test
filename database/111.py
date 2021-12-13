from collections import Iterable
data = {"name": "张梓涵", "age": "35"}
data1 = data.items()
data2 = data.keys()
print(type(data1))

for i in data1:
    print(i)
    print(type(i))


for i in data2:
    print(i)
    print(type(i))

print(isinstance(range(100), Iterable))

