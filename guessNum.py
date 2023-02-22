import random
y = random.randint(1, 20)
for i in range(1, 20):
    x = int(input("GUESS A NUMBER BETWEEN 1 TO 20: "))
    if x > 20 or x < 0:
        print("OUT OF BOUNDS!")
    elif y == x:
        print('YOUR GUESS IS RIGHT, THE NUMBER IS: '+str(y))
        break
    elif y > x:
        print("TRY GUESSING HIGHER!")
    elif y < x:
        print("TRY GUESSING LOWER!")
