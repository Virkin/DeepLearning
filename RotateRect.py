from PyQt5.QtGui import QColor, QPen
import math
import numpy as np


class RotateRect(object):
    def __init__(self, x, y, w, h, a=0, rx='', ry=''):
        self.x = x
        self.y = y

        self.deg = a

        self.w = w
        self.h = h

        if w >= h:
            self.l = h
        else:
            self.l = w

        self.computeCorners(rx, ry)

    def create(painter, x, y, w, h, a=0, color=QColor('black'), rx='', ry='', debug=False):
        rr = RotateRect(x, y, w, h, a, rx, ry)
        rr.draw(painter, color, debug=debug)
    create = staticmethod(create)

    def computeCorners(self, rx='', ry=''):
        x = self.x
        y = self.y
        w = self.w
        h = self.h
        deg = self.deg
        rad = math.radians(deg)

        cx = x
        cy = y
        if rx == '':
            rx = cx
        if ry == '':
            ry = cy

        x1, y1 = self.computeCorner(
            rx, ry, cx + (w / 2), cy + (h / 2), rad)

        x2, y2 = self.computeCorner(
            rx, ry, cx + (-w / 2), cy + (h / 2), rad)

        x3, y3 = self.computeCorner(
            rx, ry, cx + (-w / 2), cy + (-h / 2), rad)

        x4, y4 = self.computeCorner(
            rx, ry, cx + (w / 2), cy + (-h / 2), rad)

        mx1, my1 = self.computeCorner(
            rx, ry, cx + (w / 2) - self.l / 4, cy + (h / 2) - self.l / 4, rad)

        mx2, my2 = self.computeCorner(
            rx, ry, cx + (-w / 2) + self.l / 4, cy + (h / 2) - self.l / 4, rad)

        mx3, my3 = self.computeCorner(
            rx, ry, cx + (-w / 2) + self.l / 4, cy + (-h / 2) + self.l / 4, rad)

        mx4, my4 = self.computeCorner(
            rx, ry, cx + (w / 2) - self.l / 4, cy + (-h / 2) + self.l / 4, rad)

        clx = (mx1 + mx2) / 2
        cly = (my1 + my2) / 2
        crx = (mx3 + mx4) / 2
        cry = (my3 + my4) / 2

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4

        self.mx1 = mx1
        self.my1 = my1
        self.mx2 = mx2
        self.my2 = my2
        self.mx3 = mx3
        self.my3 = my3
        self.mx4 = mx4
        self.my4 = my4

        self.cx = cx
        self.cy = cy

        self.clx = clx
        self.cly = cly
        self.crx = crx
        self.cry = cry

    def computeCorner(self, rx, ry, px, py, a):
        x = 0
        y = 0

        rotation = np.array([[math.cos(a), -math.sin(a)],
                             [math.sin(a), math.cos(a)]])

        P = np.array([[px], [py]])
        R = np.array([[rx], [ry]])

        tmp = P - R
        tmp = rotation.dot(tmp)
        result = R + tmp

        return float(result[0]), float(result[1])

    def draw(self, painter, color=QColor('black'), debug=False):
        lastPen = painter.pen()

        pen = QPen()
        pen.setWidth(self.l/2)
        pen.setColor(color)
        painter.setPen(pen)

        painter.drawLine(self.mx1, self.my1, self.mx2, self.my2)
        painter.drawLine(self.mx2, self.my2, self.mx3, self.my3)
        painter.drawLine(self.mx3, self.my3, self.mx4, self.my4)
        painter.drawLine(self.mx4, self.my4, self.mx1, self.my1)

        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawLine(self.clx, self.cly, self.crx, self.cry)

        if debug == True:
            pen.setWidth(5)
            if color != QColor('white'):
                pen.setColor(QColor('black'))
            painter.setPen(pen)

            painter.drawPoint(self.cx, self.cy)
            painter.drawPoint(self.x1, self.y1)
            painter.drawPoint(self.x2, self.y2)
            painter.drawPoint(self.x3, self.y3)
            painter.drawPoint(self.x4, self.y4)
            painter.drawPoint(self.mx1, self.my1)
            painter.drawPoint(self.mx2, self.my2)
            painter.drawPoint(self.mx3, self.my3)
            painter.drawPoint(self.mx4, self.my4)
            painter.drawPoint(self.clx, self.cly)
            painter.drawPoint(self.crx, self.cry)

        painter.setPen(lastPen)
