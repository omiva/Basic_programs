ini = int(input("ENTER THE INITIAL VALUE: "))
fin = int(input("ENTER THE FINAL VALUE: "))

for num in range(ini, fin + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
