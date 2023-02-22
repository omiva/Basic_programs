x = int(input("ENTER THE n'th NUMBER: "))
c = s = 0
for i in range(0, x):
    s = s + i**2
    c = c + i**3
print("SUM OF SQUARE OF FIRST "+str(x)+" NUMBERS IS: ", s)
print("SUM OF CUBE OF FIRST "+str(x)+" NUMBERS IS: ", c)
