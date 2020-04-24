import graph
import MyLib
from math import *

graph.windowSize(1000, 1000)
graph.canvasSize(1000, 1000)

x0 = 600
y0 = 300
r = 50

graph.penColor(0, 0, 0)
graph.penSize(0.05)
graph.brushColor(155, 155, 155)

graph.circle(x0, y0, r)

indent = r/10

MyLib.sector(x0 - r / 5, y0 + r / 5, r, (3 / 2) * pi, 2 * pi, 1, 0)
MyLib.sector(x0 - r / 5 - indent, y0 + r / 5 + indent, r, (3 / 2) * pi, 2 * pi, 1, 0)
MyLib.sector(x0 - r / 5 - 2.5 * indent, y0 + r / 5 + 2.5 * indent, r, (3 / 2) * pi, 2 * pi, 1, 0)

MyLib.sector(x0 + r / 4, y0 + r / 2, r, pi, (3 / 2) * pi - pi / 6, 1, 0)
MyLib.sector(x0 + r / 4 + 2 * indent, y0 + r / 2 + 2 * indent, r, pi, (3 / 2) * pi - pi / 6, 1, 0)
MyLib.sector(x0 + r / 4 + 4 * indent, y0 + r / 2 + 4 * indent, r, pi + pi / 10, (3 / 2) * pi - pi / 6, 1, 0)

#graph.penColor(255, 255, 255)

smr = r / 2
x1 = x0 - r * sin(pi/4) - smr * sin(pi/4)
y1 = y0 + r * sin(pi/4) - smr * sin(pi/4)
MyLib.sector(x1, y1, smr, pi / 3, pi, 2, 0)
MyLib.sector(x1 - 2 * smr, y1, smr, pi, 2 * pi, 2, 0)
MyLib.sector(x1 - 2 * smr - (3 / 2) * smr, y1, smr / 2, 0, pi, 2, 0)


x0 = 300
y0 = 600
r = 50
d = - 1

graph.penColor(0, 0, 0)
graph.penSize(0.05)
graph.brushColor(155, 155, 155)

graph.circle(x0, y0, r)

indent = r/10

MyLib.sector(x0 - d * r / 5, y0 + r / 5, r, pi, (3 / 2) * pi, 1, 0)
MyLib.sector(x0 - d * (r / 5 + indent), y0 + r / 5 + indent, r, pi, (3 / 2) * pi, 1, 0)
MyLib.sector(x0 - d * (r / 5 + 2.5 * indent), y0 + r / 5 + 2.5 * indent, r, pi, (3 / 2) * pi, 1, 0)

MyLib.sector(x0 + d * r / 4, y0 + r / 2, r, (3 / 2) * pi + pi / 6, 2 * pi, 1, 0)
MyLib.sector(x0 + d * (r / 4 + 2 * indent), y0 + r / 2 + 2 * indent, r, (3 / 2) * pi + pi / 6, 2 * pi, 1, 0)
MyLib.sector(x0 + d * (r / 4 + 4 * indent), y0 + r / 2 + 4 * indent, r, (3 / 2) * pi + pi / 6, 2 * pi - pi / 10, 1, 0)

graph.penColor(255, 255, 255)

smr = r / 2
x1 = x0 - d * (r * sin(pi/4) + smr * sin(pi/4))
y1 = y0 + r * sin(pi/4) - smr * sin(pi/4)
MyLib.sector(x1, y1, smr, 0, pi - pi / 3, 2, 0)
MyLib.sector(x1 - d * 2 * smr, y1, smr, pi, 2 * pi, 2, 0)
MyLib.sector(x1 - d * (2 * smr + (3 / 2) * smr), y1, smr / 2, 0, pi, 2, 0)

graph.run()