def nFibonacci(n):
    if n <= 0:
        print("INPUT INVALID")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return nFibonacci(n - 1) + nFibonacci(n - 2)

global i
x = int(input("ENTER THE n'th PLACE: "))
print(nFibonacci(x + 1))

# to check if number belongs to fibonacci series
z = int(input("ENTER A NUM TO CHECK IF ITS THERE IN THE FIBONACCI SERIES: "))
n1, n2 = 0, 1
cnt = 0
a = []
b = []
while True:
    nth = n1 + n2
    n1 = n2
    n2 = nth
    cnt += 1
    a.append(nth)
    for i in range(len(a)):
        if a[i] not in b:
            b.append(a[i])
    if cnt > 1000:
        break
for i in range(len(b)):
    if z in b:
        print(b[i])
    if b[i] == z:
        break
if z in a:
    print("IT IS")
else:
    for i in range(len(b)):
        if b[i] >= z:
            break
        print(b[i])
    print("NO")
