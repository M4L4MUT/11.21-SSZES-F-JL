def derekszogu_e():
    print("A C oldal legyen a leghosszabb!")
    a = int(input("Az A oldal hossza:"))
    b = int(input("Az B oldal hossza:"))
    c = int(input("Az C oldal hossza:"))
    if c<b or c<a:
        print("Nem a harmadik oldal a leghosszabb.")
        return
    elif (c*c)==(a*a)+(b*b):
        print("True")
    else: 
        print("False")
derekszogu_e()
