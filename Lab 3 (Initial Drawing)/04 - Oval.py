import graph
import MyLib
from math import *




x0 = 150
y0 = 250

R = 100
t = 0
m = 4
alpha = pi / 2

points = []
while t < 2 * pi:
    x = R * cos(t)
    y = R * sin(t) / m
    print(x, y)
    xe = x0 + x * cos(alpha) - y * sin(alpha)
    ye = y0 + x * sin(alpha) + y * cos(alpha)
    points.append((xe, ye))
    t += pi / 180

graph.penColor('red')
graph.polyline(points)

graph.run()