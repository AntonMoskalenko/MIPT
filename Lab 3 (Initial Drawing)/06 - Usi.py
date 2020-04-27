import graph
import MyLib
from math import *

graph.windowSize(1000, 1000)
graph.canvasSize(1000, 1000)



x0 = 500
y0 = 500
size = 200

k = 1
mult = 1
h = 0.02
ymin = 0; ymax = 12
y = ymin
points = []
while y < ymax:
    x = - mult * y * y
    xe = x0 + k * x
    ye = y0 - k * y
    points.append((xe, ye))
    y += h
graph.polyline(points)



points.clear()
k = 2
mult = 1
h = 0.02
ymin = 0; ymax = 12
y = ymin
points = []
while y < ymax:
    x = - mult * y * y
    xe = x0 + k * x
    ye = y0 - k * y
    points.append((xe, ye))
    y += h
graph.polyline(points)


points.clear()
k = 3
mult = 1
h = 0.02
ymin = 0; ymax = 12
y = ymin
points = []
while y < ymax:
    x = - (mult ** 2) * y * y
    xe = x0 + k * x
    ye = y0 - k * y
    points.append((xe, ye))
    y += h
graph.polyline(points)

points.clear()
graph.penColor('red')
k = 1
mult = 2
h = 0.02
ymin = 0; ymax = 100
y = ymin

size = 300

points = []
while y < ymax:
    x = - (mult ** 2) * y * y
    xe = x0 + k * x
    ye = y0 - k * y
    if x <= - 0.5 and x>= - size/2:
        points.append((xe, ye))
    y += h
graph.polyline(points)


graph.run()