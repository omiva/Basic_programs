import re


def password_check():
    global Pass
    while True:
        pw = input("ENTER A STRONG PASSWORD: ")
        if not 15 >= len(pw) >= 7:
            flag = -1
            break
        elif not re.search("[a-z]", pw, re.I):
            flag = -1
            break
        # elif not re.search("[A-Z]", pw):
        #     flag = -1
        #     break
        elif not re.search("[0-9]", pw):
            flag = -1
            break
        elif not re.search("[_@$!#%^&*]", pw):
            flag = -1
            break
        else:
            flag = 0
            print("Valid Password")
            Pass = input("RE-ENTER THE PASSWORD: ")
            if Pass == pw:
                print("\nPASSWORD ACCEPTED")
            else:
                print("THE PASSWORD DOESN'T MATCH! TRY AGAIN")
                password_check()
            break
    if flag == -1:
        print("Not a Valid Password"
              "\nTHE PASSWORD MUST CONTAIN: "
              "\n* PASSWORD LENGTH OF (7-15)"
              "\n* A LOWER CASE CHARACTER"
              "\n* AN UPPERCASE CHARACTER"
              "\n* A NUMBER"
              "\n* A SPECIAL CASE CHARACTER")
        password_check()


password_check()

