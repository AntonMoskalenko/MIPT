import graph
from math import *
import MyLib

graph.windowSize(500, 500)
graph.canvasSize(500, 500)

graph.penSize(1)
graph.penColor('black')
graph.brushColor('yellow')

graph.circle(250, 250, 150)

graph.brushColor('red')
graph.circle(200, 200, 25)
graph.circle(300, 200, 25)

graph.brushColor('black')
graph.circle(200, 200, 10)
graph.circle(300, 200, 10)

graph.rectangle(200, 325, 300, 350)
MyLib.rectangle_inclined(132, 132, 130, 15, pi / 6)
MyLib.rectangle_inclined(350, 115, 110, 10, - pi / 4)

graph.run()