import turtle

def oszlop(t, magassag):
    t.pendown()
    t.begin_fill()
    t.left(90)
    t.forward(magassag)
    t.write(" "+ str(magassag))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(magassag)
    t.left(90)
    t.end_fill()
    t.penup()
    t.forward(10)

ablak = turtle.Screen()
ablak.bgcolor("lightgreen")

Eszti = turtle.Turtle()



xs = [-48,117,200,-240,160,-260,220]

for m in xs:
    if m>=200:
        Eszti.color("blue", "red")
        Eszti.pensize(3)
    elif m<=200 and m>=100:
        Eszti.color("blue", "yellow")
        Eszti.pensize(3)
    elif m<100:
        Eszti.color("blue", "green")
        Eszti.pensize(3)
    oszlop(Eszti, m)

ablak.mainloop()