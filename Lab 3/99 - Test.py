import graph
import MyLib
from math import *

graph.windowSize(1000, 1000)
graph.canvasSize(1000, 1000)



x0 = 500
y0 = 300
size = 200
# Body
graph.penColor(0, 0, 0)
graph.brushColor(200, 115, 55)
MyLib.oval(x0 + 1.2 * size, y0 + size / 6, size * 2 / 3, 5, pi / 6)
MyLib.oval(x0, y0, size, 2, 0)
MyLib.oval(x0 + 0.8 * size, y0 + size / 4, size / 4, 1, 0)
MyLib.oval(x0 - 0.8 * size, y0 + size / 3, size / 4, 2, 0)
MyLib.oval(x0 + 0.8 * size + size/5, y0 + size / 4 + size/3, size / 4, 3, pi /2)

# Head
x1 = x0 - size
y1 = y0
head = size / 3

MyLib.oval(x1 - head * sin(pi / 4), y1 + head * cos(pi / 4) / 1.5, size/4, 3, pi / 2)
graph.circle(x1, y1, head)

graph.brushColor(135, 170, 0)
graph.circle(x1 - head / 2, y1, head / 4)
graph.circle(x1 + head / 2, y1, head / 4)

graph.brushColor(0, 0, 0)
MyLib.oval(x1 - head / 2 + head/10, y1, head / 4 - head / 30, 4, pi / 2)
MyLib.oval(x1 + head / 2 + head/10, y1, head / 4 - head / 30, 4, pi / 2)

graph.penColor(250, 250, 250)
graph.brushColor(250, 250, 250)
MyLib.oval(x1 - head / 2 - head/14, y1 - head / 12, head / 4 - head / 9, 4, pi / 4)
MyLib.oval(x1 + head / 2 - head/14, y1 - head / 12, head / 4 - head / 9, 4, pi / 4)

graph.penColor(0, 0, 0)
graph.brushColor(225, 170, 135)
nose = [(x1 + head / 15, y1 + head / 3), (x1 - head / 15, y1 + head / 3), (x1, y1 + head / 3 + head / 10)]
graph.polygon(nose)

graph.line(x1, y1 + head / 3 + head / 10, x1, y1 + head / 2)
MyLib.sector(x1 - head / 8, y1 + head / 2, head / 8, 0, pi / 2 + pi / 6, 1, 0)
MyLib.sector(x1 + head / 8, y1 + head / 2, head / 8, pi /2 - pi / 6, pi, 1, 0)

# Ears
indent = head / 10
x2 = x1 + head * 0.9 * sin(pi / 12)
y2 = y1 - head * 0.9 * cos(pi / 12)
x3 = x1 + head * 0.9 * sin(pi / 3 - pi / 12)
y3 = y1 - head * 0.9 * cos(pi / 3 - pi / 12)
x4 = x3 + head / 10
y4 = y3 - head / 2


ear = [(x2, y2), (x3, y3), (x4, y4)]
graph.brushColor(200, 115, 55)
graph.polygon(ear)

ear = [(x2 + indent, y2), (x3 - indent / 2, y3 - indent / 2), (x4 - indent / 2, y4 + indent / 2)]
graph.brushColor(225, 170, 135)
graph.polygon(ear)

x2 = x1 - head * 0.9 * sin(pi / 12)
y2 = y1 - head * 0.9 * cos(pi / 12)
x3 = x1 - head * 0.9 * sin(pi / 3 - pi / 12)
y3 = y1 - head * 0.9 * cos(pi / 3 - pi / 12)
x4 = x3 - head / 10
y4 = y3 - head / 2

ear = [(x2, y2), (x3, y3), (x4, y4)]
graph.brushColor(200, 115, 55)
graph.polygon(ear)
ear = [(x2 - indent, y2), (x3 + indent / 2, y3 - indent / 2), (x4 + indent / 2, y4 + indent / 2)]
graph.brushColor(225, 170, 135)
graph.polygon(ear)


# Mustache

k = size / 30
ymin = 0; ymax = 500
h = 0.02
mult = 1.5

for i in range(3):
    x0 = x1 - head / 8 + k / 2
    y0 = y1 + head / 2 + i * indent / 2

    mult *= 2
    y = ymin

    points = []
    while y < ymax:
        x = - mult * y * y
        xe = x0 + k * x
        ye = y0 - k * y
        if x >= - head / 4 and x <= - 0.5:
            points.append((xe, ye))
        y += h
    graph.polyline(points)
    points.clear()

graph.run()