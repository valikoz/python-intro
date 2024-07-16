import turtle
import math

# Create a turtle instance
turtle.shape('turtle')

# Set the number of sides of the polygon (the more sides, the closer to a circle)
num_sides = 50
side_length = 10  # Length of each side

# Calculate the angle for turning
angle = 360 / num_sides

# Calculate the radius of circle
radius = side_length / (2 * math.sin(math.pi / num_sides))

# Set speed to make turtle slower
turtle.speed(2)
# Set start position
turtle.penup()
turtle.goto(radius, 0)
turtle.left(90)
turtle.pendown()

# Draw the polygon
for _ in range(num_sides):
    turtle.left(angle)
    turtle.forward(side_length)

turtle.done()
