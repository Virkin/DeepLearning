from PyQt5.QtGui import QColor, QPainter, QPen
from RotateRect import RotateRect
import math


def dist(p, q):
    return math.sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))


class Sensor(object):
    def __init__(self):
        self._d = 0
        self.virtualA = 0
        return

    def update(self):
        pass

    def Dist(self):
        return self._d


class GraphicSensor(Sensor):
    def __init__(self, w, x, y, a):
        super().__init__()

        self.w = w
        self.h = self.w

        self.x = x
        self.y = y

        self.graphX = x
        self.graphY = y

        self.cx = x
        self.cy = y

        self.a = 0
        self.virtualA = a

        self.halfDiag = self._getHalfSquareDiag(self.w)
        self.coeff = 0
        self.b = 0
        self.vert = False

        self.debug = False

        self.dmax = 100

    def angle(self, a, cx, cy):
        self.a = a
        self.cx = cx
        self.cy = cy

    def draw(self, painter, color=QColor('blue')):
        rr = RotateRect.create(x=self.x, y=self.y,
                               w=self.w, h=self.h, a=self.a, painter=painter, color=color, rx=self.cx, ry=self.cy)

        self.graphX = (rr.crx + rr.clx) / 2
        self.graphY = (rr.cry + rr.cly) / 2

    def create(w, x, y, cx, cy, a, virtualA, painter, canvas, color=QColor('blue'), debug=False):
        gs = GraphicSensor(w, x, y, virtualA)
        gs.debug = debug
        gs.angle(a, cx, cy)
        gs.draw(painter, color)
        gs.update(painter, canvas)

        return gs
    create = staticmethod(create)

    def _getPointOnCircle(self, cx, cy, r, a):
        a = math.radians(a)
        x = cx + r * math.cos(a)
        y = cy + r * math.sin(a)

        return x, y

    def _getHalfSquareDiag(self, l):
        return (l * math.sqrt(2)) / 2

    def update(self, painter, canvas):
        x, y = self._getPointOnCircle(
            self.graphX, self.graphY, self.halfDiag, self.virtualA + self.a)

        self.tx = x
        self.ty = y

        if x - self.graphX == 0:
            self.vert = True
        else:
            self.vert = False

            self.coeff = (y - self.graphY) / (x - self.graphX)
            self.b = self.graphY - self.coeff * self.graphX

        self.goThrough(self.dmax, painter, canvas)

        return

    def goThrough(self, dmax, painter, canvas):
        lim = 90-self.virtualA

        i = self.graphX
        step = 0.1

        found = False

        img = canvas.pixmap().toImage()

        y0 = 0
        xi = 0
        yi = 0

        if not self.vert:
            y0 = self.coeff * self.graphX + self.b
            y = y0

            additive = False

            if self.virtualA <= 0:
                if self.a <= lim or self.a > lim+180:
                    additive = True
            else:
                if self.a > lim+180 and self.a <= lim+180+180:
                    additive = True

            while dist((self.graphX, y0), (i, y)) < dmax and not found:
                y = self.coeff * i + self.b

                pixel = img.pixel(i, y)
                if QColor(pixel) == QColor('black'):
                    found = True
                    break

                if additive:
                    i += step
                else:
                    i -= step

            xi = i
            yi = y
        else:
            xi = i
            y0 = self.graphY
            i = y0

            while dist((self.graphX, y0), (xi, i)) < dmax and not found:
                pixel = img.pixel(xi, i)
                if QColor(pixel) == QColor('black'):
                    found = True
                    break

                if self.a % 360 < lim or self.a % 360 >= lim+180:
                    i -= step
                else:
                    i += step

            yi = i

        if not found:
            self._d = dmax
        else:
            self._d = dist((self.graphX, y0), (xi, yi))

        if self.debug:
            lastPen = painter.pen()

            pen = QPen()
            pen.setWidth(1)
            pen.setColor(QColor("green"))
            painter.setPen(pen)
            painter.drawLine(self.graphX, y0, xi, yi)

            painter.setPen(lastPen)

        return
