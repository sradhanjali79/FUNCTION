def people(age):
    if age<=14:
        print("drink toddy")
    elif age>=14 and age<18:
        print("drink coke")
    elif age>=18 and age<21:
        print("drink beer")
    elif age>=21:
        print("drink whisky")
people(int(input("enter any number"))) 