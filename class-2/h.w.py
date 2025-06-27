import turtle

turtle.Screen().bgcolor("green")
sc = turtle.Turtle()
turtle.title("shapes")

# star start #
sc.goto(-50, 0)

sc.forward(100)
sc.left(120)
sc.forward(100)
sc.left(120)
sc.forward(100)

sc.penup()
sc.right(150)
sc.forward(50)


sc.pendown()
sc.right(90)
sc.forward(100)
sc.right(120)
sc.forward(100)
sc.right(120)
sc.forward(100)

# star end #

# square start #
sc.penup()
sc.goto(100, 0)
sc.pendown()
sc.right(180)
sc.forward(100)
sc.right(90)
sc.forward(100)
sc.right(90)
sc.forward(100)
sc.right(90)
sc.forward(100)
sc.right(90)

# square end #

# triangle start #
sc.penup()
sc.goto(0, -100)
sc.pendown()

sc.forward(100)
sc.left(120)
sc.forward(100)
sc.left(120)
sc.forward(100)




turtle.done()