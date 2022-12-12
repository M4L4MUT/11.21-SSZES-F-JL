def vizsga():
    x=int(input("Pontszám:"))
    if x < 60:
        print("Elégtelen")
    elif x>=60 and x<70:
        print("Elégséges")
    elif x>=70 and x<80:
        print("Közepes")
    elif x>=80 and x<90:
        print("Jó")
    elif x>=90:
        print("Jeles")
vizsga()
