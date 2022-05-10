def mass(weight,height):
    bwi=weight/(height**2)
    if bwi<=18.5:
        print("under weight")
    elif bwi>18.5 and bwi<=25.0:
        print("normal")
    elif bwi>25.0 and bwi<=30:
        print("over weight")
    elif bwi>30:
        print("obese")
mass(100,2)