import turtle

turtle.shape("turtle")

# Define the initial size of the square
side_width = 20

# Draw 10 nested squares
for i in range(10):
    # Draw a square
    for _ in range(4):
        turtle.forward(side_width * (i + 1))
        turtle.left(90)

    # First method
    new_start = -(i + 1) * (side_width / 2)
    turtle.penup()
    turtle.goto(new_start, new_start)
    turtle.pendown()

    # Second method
    # turtle.right(135)
    # turtle.penup()
    # turtle.forward((2 * side_width**2) ** 0.5 / 2)
    # turtle.left(135)
    # turtle.pendown()
