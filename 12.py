import turtle
ablak=turtle.Screen()
ablak.bgcolor("lightgreen")
Teki=turtle.Turtle()
Teki.shape("turtle")
Teki.color("brown")
Teki.pencolor("blue")
Teki.speed(10)


Teki.stamp()
for i in range(1,13):
    
    Teki.penup()
    Teki.forward(100)
    Teki.pendown()
    Teki.forward(20)
    Teki.penup()
    Teki.forward(15)
    Teki.stamp()
    Teki.backward(135)
    Teki.right(30)
ablak.mainloop()