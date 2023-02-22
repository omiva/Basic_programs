# convert msg to list then count
from collections import Counter

x = input("ENTER STRING: ")
y = x.split()
o = []
print(y)
for i in range(len(y)):
    z = y[i]
    a = Counter(y)
    if z not in o:
        print(z, "has occured ", a[z], " times")
    if a[z] == 1:
        o.append(z)
print(o)
