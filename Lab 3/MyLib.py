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

def cat (x0, y0, size, d, color):

    graph.penColor(0, 0, 0)
    graph.penSize(0.05)
    # Body
    if color == 'brown':
        graph.brushColor(200, 115, 55)
    else:
        graph.brushColor(110, 95, 85)
    oval(x0 + d * 1.2 * size, y0 + size / 6, size * 2 / 3, 5, d * pi / 6)
    oval(x0, y0, size, 2, 0)
    oval(x0 + d * 0.8 * size, y0 + size / 4, size / 4, 1, 0)
    oval(x0 - d * 0.8 * size, y0 + size / 3, size / 4, 2, 0)
    oval(x0 + d * (0.8 * size + size / 5), y0 + size / 4 + size / 3, size / 4, 3, pi / 2)

    # Head
    x1 = x0 - d * size
    y1 = y0
    head = size / 3

    oval(x1 - d * head * sin(pi / 4), y1 + head * cos(pi / 4) / 1.5, size / 4, 3, pi / 2)
    graph.circle(x1, y1, head)

    if color == 'brown':
        graph.brushColor(135, 170, 0)
    else:
        graph.brushColor(40, 215, 255)
    graph.circle(x1 - head / 2, y1, head / 4)
    graph.circle(x1 + head / 2, y1, head / 4)

    graph.brushColor(0, 0, 0)
    oval(x1 - head / 2 + head / 10, y1, head / 4 - head / 30, 4, pi / 2)
    oval(x1 + head / 2 + head / 10, y1, head / 4 - head / 30, 4, pi / 2)

    graph.penColor(250, 250, 250)
    graph.brushColor(250, 250, 250)
    oval(x1 - head / 2 - head / 14, y1 - head / 12, head / 4 - head / 9, 4, pi / 4)
    oval(x1 + head / 2 - head / 14, y1 - head / 12, head / 4 - head / 9, 4, pi / 4)

    graph.penColor(0, 0, 0)
    graph.brushColor(225, 170, 135)
    nose = [(x1 + head / 15, y1 + head / 3), (x1 - head / 15, y1 + head / 3), (x1, y1 + head / 3 + head / 10)]
    graph.polygon(nose)

    graph.line(x1, y1 + head / 3 + head / 10, x1, y1 + head / 2)
    sector(x1 - head / 8, y1 + head / 2, head / 8, 0, pi / 2 + pi / 6, 1, 0)
    sector(x1 + head / 8, y1 + head / 2, head / 8, pi / 2 - pi / 6, pi, 1, 0)

    # Ears
    indent = head / 10
    x2 = x1 + head * 0.9 * sin(pi / 12)
    y2 = y1 - head * 0.9 * cos(pi / 12)
    x3 = x1 + head * 0.9 * sin(pi / 3 - pi / 12)
    y3 = y1 - head * 0.9 * cos(pi / 3 - pi / 12)
    x4 = x3 + head / 10
    y4 = y3 - head / 2

    ear = [(x2, y2), (x3, y3), (x4, y4)]
    if color == 'brown':
        graph.brushColor(200, 115, 55)
    else:
        graph.brushColor(110, 95, 85)
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
    if color == 'brown':
        graph.brushColor(200, 115, 55)
    else:
        graph.brushColor(110, 95, 85)
    graph.polygon(ear)
    ear = [(x2 - indent, y2), (x3 + indent / 2, y3 - indent / 2), (x4 + indent / 2, y4 + indent / 2)]
    graph.brushColor(225, 170, 135)
    graph.polygon(ear)

    # Mustache

    k = 1
    ymin = 0;
    ymax = 1000
    h = 0.02
    mult = 0.4

    for i in range(-1, 2):
        x0 = x1 - head / 8 + k / 2
        y0 = y1 + head / 2 + i * indent / 2

        mult *= 1.5
        y = ymin

        points = []
        while y < ymax:
            x = - (mult ** 2) * y * y
            xe = x0 + k * x
            ye = y0 - k * y
            if x >= - head and x <= 0:
                points.append((xe, ye))
            y += h
        graph.polyline(points)
        points.clear()

    mult = 0.4

    for i in range(-1, 2):
        x0 = x1 + head / 8 + k / 2
        y0 = y1 + head / 2 + i * indent / 2

        mult *= 1.5
        y = ymin

        points = []
        while y < ymax:
            x = (mult ** 2) * y * y
            xe = x0 + k * x
            ye = y0 - k * y
            if head >= x >= 0:
                points.append((xe, ye))
            y += h
        graph.polyline(points)
        points.clear()

def clew (x0, y0, r, d):

    if d == 1:
        graph.penColor(0, 0, 0)
        graph.penSize(0.05)
        graph.brushColor(155, 155, 155)

        graph.circle(x0, y0, r)

        indent = r / 10

        sector(x0 - r / 5, y0 + r / 5, r, (3 / 2) * pi, 2 * pi, 1, 0)
        sector(x0 - r / 5 - indent, y0 + r / 5 + indent, r, (3 / 2) * pi, 2 * pi, 1, 0)
        sector(x0 - r / 5 - 2.5 * indent, y0 + r / 5 + 2.5 * indent, r, (3 / 2) * pi, 2 * pi, 1, 0)

        sector(x0 + r / 4, y0 + r / 2, r, pi, (3 / 2) * pi - pi / 6, 1, 0)
        sector(x0 + r / 4 + 2 * indent, y0 + r / 2 + 2 * indent, r, pi, (3 / 2) * pi - pi / 6, 1, 0)
        sector(x0 + r / 4 + 4 * indent, y0 + r / 2 + 4 * indent, r, pi + pi / 10, (3 / 2) * pi - pi / 6, 1, 0)

        graph.penColor(140, 120, 70)

        smr = r / 2
        x1 = x0 - r * sin(pi / 4) - smr * sin(pi / 4)
        y1 = y0 + r * sin(pi / 4) - smr * sin(pi / 4)
        sector(x1, y1, smr, pi / 3, pi, 2, 0)
        sector(x1 - 2 * smr, y1, smr, pi, 2 * pi, 2, 0)
        sector(x1 - 2 * smr - (3 / 2) * smr, y1, smr / 2, 0, pi, 2, 0)

    elif d == -1:

        graph.penColor(0, 0, 0)
        graph.penSize(0.05)
        graph.brushColor(155, 155, 155)

        graph.circle(x0, y0, r)

        indent = r / 10

        sector(x0 - d * r / 5, y0 + r / 5, r, pi, (3 / 2) * pi, 1, 0)
        sector(x0 - d * (r / 5 + indent), y0 + r / 5 + indent, r, pi, (3 / 2) * pi, 1, 0)
        sector(x0 - d * (r / 5 + 2.5 * indent), y0 + r / 5 + 2.5 * indent, r, pi, (3 / 2) * pi, 1, 0)

        sector(x0 + d * r / 4, y0 + r / 2, r, (3 / 2) * pi + pi / 6, 2 * pi, 1, 0)
        sector(x0 + d * (r / 4 + 2 * indent), y0 + r / 2 + 2 * indent, r, (3 / 2) * pi + pi / 6, 2 * pi, 1, 0)
        sector(x0 + d * (r / 4 + 4 * indent), y0 + r / 2 + 4 * indent, r, (3 / 2) * pi + pi / 6, 2 * pi - pi / 10, 1,
                     0)

        graph.penColor(140, 120, 70)

        smr = r / 2
        x1 = x0 - d * (r * sin(pi / 4) + smr * sin(pi / 4))
        y1 = y0 + r * sin(pi / 4) - smr * sin(pi / 4)
        sector(x1, y1, smr, 0, pi - pi / 3, 2, 0)
        sector(x1 - d * 2 * smr, y1, smr, pi, 2 * pi, 2, 0)
        sector(x1 - d * (2 * smr + (3 / 2) * smr), y1, smr / 2, 0, pi, 2, 0)