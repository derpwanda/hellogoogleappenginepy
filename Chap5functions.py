import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square with sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("hotpink")
alex.pensize(3)


size = 20
for i in range(5):
	drawSquare(alex, size)
	size = size + 20
	
	alex.forward(size + 20)
	alex.penup()
	
	alex.pendown()

wn.exitonclick()

