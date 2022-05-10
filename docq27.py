def speed(x):
    if x<70:
        print("ok")
    elif x>=70:
        point=(x-70)//5
        print(point)
        if point>12:
            print("license suspended")
speed(int(input("enter any number")))