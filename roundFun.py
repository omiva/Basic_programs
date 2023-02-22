# round() basically rounds up a given decimal value to the closest preceding or succeeding value
while True:
    x = input('ENTER A DECIMAL NUMBER: ')
    if x == 'stop':
        break
    print(round(float(x)))
