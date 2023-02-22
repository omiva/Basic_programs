while True:
    x = int(input("ENTER A NUMBER: "))
    if x > 1:
        for j in range(2, x):
            if x % j == 0:
                print(x, "IS A COMPOSITE NUMBER")
                break
        else:
            print(x, " IS A PRIME NUMBER")
    else:
        break