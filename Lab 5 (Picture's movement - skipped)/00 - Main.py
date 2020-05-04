import graph
from math import *
from Tkinter import *


def main():
    xmax = 500
    ymax = 700
    graph.windowSize(xmax, ymax)
    graph.canvasSize(xmax, ymax)

    background(xmax, ymax, 300)

    x0 = 500
    y0 = 300
    window_width = 180
    window_indent = 20
    while x0 >= 0:
        window(x0, y0, window_width, window_indent, 5)
        x0 -= (window_width + window_indent)

    my_pic = graph.canvas()
    graph.canvasSize(xmax, ymax)

    clew(200, 640, 50, 1)
    cat(350, 300, 80, 1, 'brown')

    my_pic.pack()

    graph.run()


def background(xmax, ymax, middle):
    """Setting background for the picture.
    xmax, ymax - size of the window
    middle - middle point for separation"""

    graph.brushColor(85, 70, 0)
    graph.rectangle(0, 0, xmax, middle)
    graph.brushColor(125, 100, 0)
    graph.rectangle(0, middle, xmax, ymax)


def window(x0, y0, win_width, indent_out, indent_in):
    """Drawing window.
    (x0, y0) - right middle point, indent_out - window indent,
    indent_in - indent inside window"""
    graph.penColor(215, 255, 230)
    graph.brushColor(215, 255, 230)

    x1 = x0 - indent_out
    y1 = y0 - indent_out
    x2 = x0 - indent_out - win_width
    y2 = indent_out

    graph.rectangle(x1, y1, x2, y2)

    graph.penColor(135, 205, 225)
    graph.brushColor(135, 205, 225)
    graph.rectangle(x2 + indent_in, y2 + indent_in, x2 + win_width / 2 - indent_in,
                    y2 + (y1 - y2) / 2 - indent_in)
    graph.rectangle(x2 + indent_in, y2 + (y1 - y2) / 2 + indent_in, x2 + win_width / 2 - indent_in,
                    y2 + (y1 - y2) - indent_in)
    graph.rectangle(x2 + win_width / 2 + indent_in, y2 + indent_in, x2 + win_width - indent_in,
                    y2 + (y1 - y2) / 2 - indent_in)
    graph.rectangle(x2 + win_width / 2 + indent_in, y2 + (y1 - y2) / 2 + indent_in, x2 + win_width - indent_in,
                    y2 + (y1 - y2) - indent_in)


def cat(x0, y0, size, direction, color):
    """Drawing cat.
    (x0, y0) - body center, size - radius of the body,
    direction - side of the head (1 - left, -1 - right),
    color - color of the body as string (brown or grey)"""
    cat_body(x0, y0, size, direction, color)
    cat_head(x0, y0, size, direction, color)
    pass


def cat_body(x0, y0, size, direction, color):
    """Drawing body, tail and paws of the cat.
    (x0, y0) - body center, size - radius of the body,
    direction - side of the tail (1 - right, -1 - left),
    color - color of the body as string (brown or grey)"""
    graph.penColor(0, 0, 0)
    graph.penSize(0.05)

    if color == 'brown':
        graph.brushColor(200, 115, 55)
    else:
        graph.brushColor(110, 95, 85)
    oval(x0 + direction * 1.2 * size, y0 + size / 6, size * 2 / 3, 5, direction * pi / 6)
    oval(x0, y0, size, 2, 0)
    oval(x0 + direction * 0.8 * size, y0 + size / 4, size / 4, 1, 0)
    oval(x0 - direction * 0.8 * size, y0 + size / 3, size / 4, 2, 0)
    oval(x0 + direction * (0.8 * size + size / 5), y0 + size / 4 + size / 3, size / 4, 3, pi / 2)


def cat_head(x0, y0, size, direction, color):
    """Drawing cat head with eyes and nose - all variables sam as for body."""
    x1 = x0 - direction * size
    y1 = y0
    head_size = size / 3

    oval(x1 - direction * head_size * sin(pi / 4), y1 + head_size * cos(pi / 4) / 1.5, size / 4, 3, pi / 2)
    graph.circle(x1, y1, head_size)

    if color == 'brown':
        graph.brushColor(135, 170, 0)
    else:
        graph.brushColor(40, 215, 255)
    graph.circle(x1 - head_size / 2, y1, head_size / 4)
    graph.circle(x1 + head_size / 2, y1, head_size / 4)

    graph.brushColor(0, 0, 0)
    oval(x1 - head_size / 2 + head_size / 10, y1, head_size / 4 - head_size / 30, 4, pi / 2)
    oval(x1 + head_size / 2 + head_size / 10, y1, head_size / 4 - head_size / 30, 4, pi / 2)

    graph.penColor(250, 250, 250)
    graph.brushColor(250, 250, 250)
    oval(x1 - head_size / 2 - head_size / 14, y1 - head_size / 12, head_size / 4 - head_size / 9, 4, pi / 4)
    oval(x1 + head_size / 2 - head_size / 14, y1 - head_size / 12, head_size / 4 - head_size / 9, 4, pi / 4)

    graph.penColor(0, 0, 0)
    graph.brushColor(225, 170, 135)
    nose = [(x1 + head_size / 15, y1 + head_size / 3), (x1 - head_size / 15, y1 + head_size / 3),
            (x1, y1 + head_size / 3 + head_size / 10)]
    graph.polygon(nose)

    graph.line(x1, y1 + head_size / 3 + head_size / 10, x1, y1 + head_size / 2)
    sector(x1 - head_size / 8, y1 + head_size / 2, head_size / 8, 0, pi / 2 + pi / 6, 1)
    sector(x1 + head_size / 8, y1 + head_size / 2, head_size / 8, pi / 2 - pi / 6, pi, 1)

    cat_ears(x1, y1, head_size, color)
    cat_mustache(x1, y1, head_size)


def cat_ears(x1, y1, head_size, color):
    """Drawing cat ears.
     (x1, y1) - head center"""
    indent = head_size / 10
    x2 = x1 + head_size * 0.9 * sin(pi / 12)
    y2 = y1 - head_size * 0.9 * cos(pi / 12)
    x3 = x1 + head_size * 0.9 * sin(pi / 3 - pi / 12)
    y3 = y1 - head_size * 0.9 * cos(pi / 3 - pi / 12)
    x4 = x3 + head_size / 10
    y4 = y3 - head_size / 2

    ear = [(x2, y2), (x3, y3), (x4, y4)]
    if color == 'brown':
        graph.brushColor(200, 115, 55)
    else:
        graph.brushColor(110, 95, 85)
    graph.polygon(ear)

    ear = [(x2 + indent, y2), (x3 - indent / 2, y3 - indent / 2), (x4 - indent / 2, y4 + indent / 2)]
    graph.brushColor(225, 170, 135)
    graph.polygon(ear)

    x2 = x1 - head_size * 0.9 * sin(pi / 12)
    y2 = y1 - head_size * 0.9 * cos(pi / 12)
    x3 = x1 - head_size * 0.9 * sin(pi / 3 - pi / 12)
    y3 = y1 - head_size * 0.9 * cos(pi / 3 - pi / 12)
    x4 = x3 - head_size / 10
    y4 = y3 - head_size / 2

    ear = [(x2, y2), (x3, y3), (x4, y4)]
    if color == 'brown':
        graph.brushColor(200, 115, 55)
    else:
        graph.brushColor(110, 95, 85)
    graph.polygon(ear)
    ear = [(x2 - indent, y2), (x3 + indent / 2, y3 - indent / 2), (x4 + indent / 2, y4 + indent / 2)]
    graph.brushColor(225, 170, 135)
    graph.polygon(ear)


def cat_mustache(x1, y1, head_size):
    """Drawing cat mustache.
     (x1, y1) - head center"""
    k = 1
    ymin = 0
    ymax = 1000
    h = 0.02
    mult = 0.4

    for i in range(-1, 2):
        x0 = x1 - head_size / 8 + k / 2
        y0 = y1 + head_size / 2 + i * head_size / 20

        mult *= 1.5
        y = ymin

        points = []
        while y < ymax:
            x = - (mult ** 2) * y * y
            xe = x0 + k * x
            ye = y0 - k * y
            if - head_size <= x <= 0:
                points.append((xe, ye))
            y += h
        graph.polyline(points)
        points.clear()

    mult = 0.4

    for i in range(-1, 2):
        x0 = x1 + head_size / 8 + k / 2
        y0 = y1 + head_size / 2 + i * head_size / 20

        mult *= 1.5
        y = ymin

        points = []
        while y < ymax:
            x = (mult ** 2) * y * y
            xe = x0 + k * x
            ye = y0 - k * y
            if head_size >= x >= 0:
                points.append((xe, ye))
            y += h
        graph.polyline(points)
        points.clear()
    pass


def clew(x0, y0, radius, direction):
    """Drawing clue with center in (x0, y0), correspondent radius
    and direction (1 - right, -1 - left)."""
    if direction == 1:
        graph.penColor(0, 0, 0)
        graph.penSize(0.05)
        graph.brushColor(155, 155, 155)

        graph.circle(x0, y0, radius)

        indent = radius / 10

        sector(x0 - radius / 5, y0 + radius / 5, radius, (3 / 2) * pi, 2 * pi, 1)
        sector(x0 - radius / 5 - indent, y0 + radius / 5 + indent, radius, (3 / 2) * pi, 2 * pi, 1)
        sector(x0 - radius / 5 - 2.5 * indent, y0 + radius / 5 + 2.5 * indent, radius, (3 / 2) * pi, 2 * pi, 1)

        sector(x0 + radius / 4, y0 + radius / 2, radius, pi, (3 / 2) * pi - pi / 6, 1)
        sector(x0 + radius / 4 + 2 * indent, y0 + radius / 2 + 2 * indent, radius, pi, (3 / 2) * pi - pi / 6, 1)
        sector(x0 + radius / 4 + 4 * indent, y0 + radius / 2 + 4 * indent, radius, pi + pi / 10, (3 / 2) * pi - pi / 6,
               1)

        graph.penColor(140, 120, 70)

        smr = radius / 2
        x1 = x0 - radius * sin(pi / 4) - smr * sin(pi / 4)
        y1 = y0 + radius * sin(pi / 4) - smr * sin(pi / 4)
        sector(x1, y1, smr, pi / 3, pi, 2)
        sector(x1 - 2 * smr, y1, smr, pi, 2 * pi, 2)
        sector(x1 - 2 * smr - (3 / 2) * smr, y1, smr / 2, 0, pi, 2)

    elif direction == -1:

        graph.penColor(0, 0, 0)
        graph.penSize(0.05)
        graph.brushColor(155, 155, 155)

        graph.circle(x0, y0, radius)

        indent = radius / 10

        sector(x0 - direction * radius / 5, y0 + radius / 5, radius, pi, (3 / 2) * pi, 1)
        sector(x0 - direction * (radius / 5 + indent), y0 + radius / 5 + indent, radius, pi, (3 / 2) * pi, 1, )
        sector(x0 - direction * (radius / 5 + 2.5 * indent), y0 + radius / 5 + 2.5 * indent, radius, pi, (3 / 2) * pi,
               1, )

        sector(x0 + direction * radius / 4, y0 + radius / 2, radius, (3 / 2) * pi + pi / 6, 2 * pi, 1)
        sector(x0 + direction * (radius / 4 + 2 * indent), y0 + radius / 2 + 2 * indent, radius, (3 / 2) * pi + pi / 6,
               2 * pi, 1)
        sector(x0 + direction * (radius / 4 + 4 * indent), y0 + radius / 2 + 4 * indent, radius, (3 / 2) * pi + pi / 6,
               2 * pi - pi / 10, 1)

        graph.penColor(140, 120, 70)

        smr = radius / 2
        x1 = x0 - direction * (radius * sin(pi / 4) + smr * sin(pi / 4))
        y1 = y0 + radius * sin(pi / 4) - smr * sin(pi / 4)
        sector(x1, y1, smr, 0, pi - pi / 3, 2)
        sector(x1 - direction * 2 * smr, y1, smr, pi, 2 * pi, 2)
        sector(x1 - direction * (2 * smr + (3 / 2) * smr), y1, smr / 2, 0, pi, 2)


def oval(x0, y0, radius, compression, alpha):
    """Drawing oval with center in (x0, y0), stated radius,
    compression and angle of rotation."""
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


def sector(x0, y0, radius, start, end, compression):
    """Drawing sector of the circle with center in (x0, y0),
    stated radius and compression between start and end angles
    (in initial coordinate system)"""
    t = start
    points = []
    while t < end:
        x = radius * cos(t)
        y = radius * sin(t) / compression
        xe = x0 + x
        ye = y0 + y
        points.append((xe, ye))
        t += pi / 180

    graph.polyline(points)


def keyPressed(event):
    if event.keycode == graph.VK_LEFT:
        graph.moveObjectBy(obj, -5, 0)
    elif event.keycode == graph.VK_RIGHT:
        graph.moveObjectBy(obj, 5, 0)
    elif event.keycode == graph.VK_UP:
        graph.moveObjectBy(obj, 0, -5)
    elif event.keycode == graph.VK_DOWN:
        graph.moveObjectBy(obj, 0, 5)
    elif event.keycode == graph.VK_ESCAPE:
        graph.close()


main()
