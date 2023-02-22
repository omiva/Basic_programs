temp = num = int(input("ENTER A NUMBER: "))
order = len(str(num))
s = 0
while temp > 0:
    digit = temp % 10
    s = s + (digit ** order)
    temp //= 10
if num == s:
    print(num, "IS AN ARMSTRONG NUMBER!")
else:
    print(num, "ISN'T AN ARMSTRONG NUMBER!")
