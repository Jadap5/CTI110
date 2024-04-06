import turtle

# Create a turtle screen
screen = turtle.Screen()

# Create a turtle
t = turtle.Turtle()

# Function to draw a square
def draw_square():
    for _ in range(4):
        t.forward(100)
        t.right(90)

# Function to draw a triangle
def draw_triangle():
    for _ in range(3):
        t.forward(100)
        t.right(120)

# Draw square
draw_square()

# Move turtle to a new position for triangle
t.penup()
t.goto(150, 0)
t.pendown()

# Draw triangle
draw_triangle()

# Keep the window open until it's closed by the user
screen.mainloop()
