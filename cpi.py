def cpi(p, r, t):
    amt = p * (pow((1 + r / 100), t))
    CI = amt - p
    print("THE CI is: ", CI)


p = float(input("ENTER THE PRINCIPLE: "))
r = float(input("ENTER THE RATE: "))
t = float(input("ENTER THE TIME: "))
cpi(p, r, t)
