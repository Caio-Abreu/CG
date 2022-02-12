import turtle
t= turtle.Pen()
t.speed(10)

for x in range(200):
    t.pencolor("black") # Cor da espiral a ser feita
    t.width(x/100 + 1) # largura da espiral
    t.forward(x)
    t.left(59)
 
turtle.done()
