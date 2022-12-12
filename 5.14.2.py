def nyaralas():
    x = int(input("Melyik napon indulsz nyaralni?"))
    y = int(input("Hány napot fogsz ott tölteni?"))
    x = (x + y) % 7
    if x==0:
        print("Hétfőn érsz haza.")
    elif x==1:
        print("Kedden érsz haza.")
    elif x==2:
        print("Szerdán érsz haza.")
    elif x==3:
        print("Csütörtökön érsz haza.")
    elif x==4:
        print("Pénteken érsz haza.")
    elif x==5:
        print("Szombaton érsz haza.")
    elif x==6:
        print("Vasárnap érsz haza.")
    
    

    
nyaralas()