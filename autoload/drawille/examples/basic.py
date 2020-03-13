from __future__ import print_function
from drawille import Canvas
import math


canvas = Canvas()

for x in range(1800):
    canvas.set(x/10, math.sin(math.radians(x)) * 10)

print(canvas.frame())

canvas.clear()

for x in range(0, 1800, 10):
    canvas.set(x/10, 10 + math.sin(math.radians(x)) * 10)
    canvas.set(x/10, 10 + math.cos(math.radians(x)) * 10)

print(canvas.frame())

canvas.clear()

for x in range(0, 3600, 20):
    canvas.set(x/20, 4 + math.sin(math.radians(x)) * 4)

print(canvas.frame())

canvas.clear()

for x in range(0, 360, 4):
    canvas.set(x/4, 30 + math.sin(math.radians(x)) * 30)

for x in range(30):
    for y in range(30):
        canvas.set(x,y)
        canvas.toggle(x+30, y+30)
        canvas.toggle(x+60, y)

print(canvas.frame())
