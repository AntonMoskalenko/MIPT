import graph
import MyLib
from math import *

graph.windowSize(500, 700)
graph.canvasSize(500, 700)

graph.brushColor(85, 70, 0)
graph.rectangle(0, 0, 500, 300)
graph.brushColor(125, 100, 0)
graph.rectangle(0, 300, 500, 700)

x0 = 500
y0 = 300
window_width = 180
window_indent = 20
while x0 >= 0:
    MyLib.window(x0, y0, window_width, window_indent, 5)
    x0 -= (window_width + window_indent)

MyLib.clew(200, 640, 50, 1)
MyLib.clew(400, 600, 30, - 1)
MyLib.clew(300, 500, 30, - 1)
MyLib.clew(150, 370, 15, 1)
MyLib.clew(70, 600, 15, 1)
MyLib.clew(425, 400, 15, - 1)

MyLib.cat(350, 300, 80, 1, 'brown')
MyLib.cat(150, 450, 80, -1, 'grey')

MyLib.cat(100, 350, 30, -1, 'brown')
MyLib.cat(450, 500, 30, -1, 'brown')
MyLib.cat(100, 650, 30, -1, 'grey')
MyLib.cat(400, 650, 30, 1, 'grey')
MyLib.cat(350, 550, 30, 1, 'brown')

graph.run()
