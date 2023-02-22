x = int(input())
k = []
for i in range(0, x + 1):
    y = bin(i).replace('0b', '')
    z = [y]
    m = [y[::-1]]
    if m == z:
        k.append(i)
n = k[1:]
o = []
s = []
print(n, " huh", o)

for j in range(0, x ):
    if x not in k:
        p = n[j] + o[j]
        s.append(p)
        print(s)
