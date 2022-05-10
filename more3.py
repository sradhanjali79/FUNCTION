def strong_password():
    x=input("enter your password")
    if (x>="A" and x<="Z") or (x>="a" and x<="z") or (x>=0 and x<=9) or (x>="@" and x<="#"):
        if len(x)>=8 and len(x)<=20:
            print("strong password")
        else:
            print("wrong")
strong_password()
