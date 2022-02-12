import turtle

def form_tri(side):
    for i in range(3):
        my_pen.fd(side)
        my_pen.left(120)
        side -= 10
 
tut = turtle.Screen()
tut.bgcolor("black")
tut.title("Turtle")
 
my_pen = turtle.Turtle()
my_pen.color("white")
 
tut = turtle.Screen()          

side = 300
for i in range(10):
    form_tri(side)
    side -= 30

turtle.done()