# turtle_ex1.py

import turtle

p = turtle.Pen()
p.shape("turtle")

for x in range(1, 100, 1):
    p.forward(x)
    p.left(40)
