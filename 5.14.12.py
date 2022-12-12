def derekszogu_e():
    a = int(input("Az A oldal hossza:"))
    b = int(input("Az B oldal hossza:"))
    c = int(input("Az C oldal hossza:"))
    if c>b and c>a:
        if(c*c)==(a*a)+(b*b):
            print("True")
        else: 
            print("False")
    elif a>b and a>c:
        if(a*a)==(c*c)+(b*b):
            print("True")
        else: 
            print("False")
    elif b>c and b>a:
        if(b*b)==(a*a)+(c*c):
            print("True")
        else: 
            print("False")


        
    
derekszogu_e()
