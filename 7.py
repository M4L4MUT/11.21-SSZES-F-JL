import turtle
ablak=turtle.Screen()
ablak.bgcolor("lightgreen")
Kalóz=turtle.Turtle()
Kalóz.shape("turtle")
Kalóz.color("brown")
Kalóz.speed(1)

nezesirany=0
szogek = [160, -43, 270, -97, -43, 200, -940, 17,-86]
for x in szogek:
    nezesirany=nezesirany+x
    print("A kalóz most ennyit fordul:", x)
    if x>0:
        Kalóz.left(x)
    else:
        Kalóz.right(x)
    Kalóz.forward(100)
print("A kalóz nézésének iránya: ",nezesirany)