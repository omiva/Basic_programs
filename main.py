import sys
import random

while True:
    print("enter rock, paper or scissor")
    response = input()
    s = (random.randint(1, 3))  # 1=rock 2=paper 3= scissor
    if response == 'rock':
        if s == 1:
            print("DRAW")
        elif s == 2:
            print("LOSS")
        elif s == 3:
            print("WIN")
    if response == 'paper':
        if s == 1:
            print("WIN")
        elif s == 2:
            print("DRAW")
        elif s == 3:
            print("LOSS")
    if response == 'scissor':
        if s == 1:
            print("LOSS")
        elif s == 2:
            print("WIN")
        elif s == 3:
            print("LOSS")
    if response=='exit':
        sys.exit()
