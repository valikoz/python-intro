import math
import turtle

turtle.shape("circle")
turtle.shapesize(.2)

coef_k = 1
param_t = 0

while param_t <= 16 * math.pi:
    x = coef_k * param_t * math.cos(param_t)
    y = coef_k * param_t * math.sin(param_t)
    turtle.goto(x, y)
    param_t += 0.1
