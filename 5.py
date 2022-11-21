xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
print("A,")
for x in xs:
    print(x)
print("B,")
for x in xs:
    print(x,x*x)
print("C,")
összeg=0
for x in xs:
    összeg=összeg+x
print(összeg)
print("D,")
szorzat=1
for x in xs:
    szorzat=szorzat*x
    print(szorzat)