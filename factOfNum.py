def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)


x = int(input('ENTER A NUMBER: '))
print('FACTORIAL OF THE NUMBER IS: ', fact(x))
