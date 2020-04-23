import graph
from math import *

def rectangle_inclined(x0, y0, width, height, alpha):

    if alpha >= 0:

        x1 = x0 + width * cos(alpha)
        y1 = y0 + width * sin(alpha)

        x2 = x1 + height * sin(alpha)
        y2 = y1 - height * cos(alpha)

        x3 = x0 + height * sin(alpha)
        y3 = y0 - height * cos(alpha)

        graph.polygon([(x0, y0), (x1, y1), (x2, y2), (x3, y3)])

    else:
        alpha = - alpha

        x1 = x0 - width * cos(alpha)
        y1 = y0 + width * sin(alpha)

        x2 = x1 - height * sin(alpha)
        y2 = y1 - height * cos(alpha)

        x3 = x0 - height * sin(alpha)
        y3 = y0 - height * cos(alpha)

        graph.polygon([(x0, y0), (x1, y1), (x2, y2), (x3, y3)])

def window(x0, y0, width, indent, small_indent):
    graph.penColor(215, 255, 230)
    graph.brushColor(215, 255, 230)

    x1 = x0 - indent
    y1 = y0 - indent
    x2 = x0 - indent - width
    y2 = indent

    graph.rectangle(x1, y1, x2, y2)

    graph.penColor(135, 205, 225)
    graph.brushColor(135, 205, 225)
    graph.rectangle(x2 + small_indent, y2 + small_indent, x2 + width / 2 - small_indent,
                    y2 + (y1 - y2) / 2 - small_indent)
    graph.rectangle(x2 + small_indent, y2 + (y1 - y2) / 2 + small_indent, x2 + width / 2 - small_indent,
                    y2 + (y1 - y2) - small_indent)
    graph.rectangle(x2 + width / 2 + small_indent, y2 + small_indent, x2 + width - small_indent,
                    y2 + (y1 - y2) / 2 - small_indent)
    graph.rectangle(x2 + width / 2 + small_indent, y2 + (y1 - y2) / 2 + small_indent, x2 + width - small_indent,
                    y2 + (y1 - y2) - small_indent)

def oval(x0, y0, radius, compression, alpha):
    t = 0
    points = []
    while t < 2 * pi:
        x = radius * cos(t)
        y = radius * sin(t) / compression
        xe = x0 + x * cos(alpha) - y * sin(alpha)
        ye = y0 + x * sin(alpha) + y * cos(alpha)
        points.append((xe, ye))
        t += pi / 180

    graph.polygon(points)

def sector(x0, y0, radius, start, end, compression, alpha):
    t = start
    points = []
    while t < end:
        x = radius * cos(t)
        y = radius * sin(t) / compression
        xe = x0 + x * cos(alpha) - y * sin(alpha)
        ye = y0 + x * sin(alpha) + y * cos(alpha)
        points.append((xe, ye))
        t += pi / 180

    graph.polyline(points)
