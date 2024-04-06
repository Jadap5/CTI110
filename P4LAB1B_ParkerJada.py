import turtle

# Create a turtle screen
screen = turtle.Screen()

# Create a turtle
t = turtle.Turtle()

# Set pen color and size
t.color("pink")
t.pensize(40)

# Draw first initial (J)
t.forward(100)
t.backward(200)
t.forward(100)
t.right(90)
t.forward(120)
t.circle(-60, 200)

# Move to draw second initial (P)
t.penup()
t.goto(150, 0)
t.pendown()
t.circle(80, 180)
t.left(90)
t.forward(250)

# Keep the window open until it's closed by the user
screen.mainloop()
