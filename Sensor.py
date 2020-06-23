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

    def angle(self, a, cx, cy):
        self.a = a
        self.cx = cx
        self.cy = cy

    def draw(self, painter, color=QColor('blue')):
        rr = RotateRect.create(x=self.x, y=self.y,
                               w=self.w, h=self.h, a=self.a, painter=painter, color=color, rx=self.cx, ry=self.cy)

        self.graphX = (rr.crx + rr.clx) / 2
        self.graphY = (rr.cry + rr.cly) / 2

        if not self.debug:
            return

        d = 100

        x0 = self.graphX
        y0 = self.graphY
        x1 = x0
        y1 = y0

        self.update()

        lim = 90-self.virtualA

        if not self.vert:
            x1, y1 = self._getY(x0, d, self.a % 360, lim)
        else:
            x1 = x0
            y1 = y0-d if self.a % 360 < lim or self.a % 360 >= lim+180 else y0+d

        lastPen = painter.pen()

        pen = QPen()
        pen.setWidth(1)
        pen.setColor(QColor("green"))
        painter.setPen(pen)
        painter.drawLine(x0, y0, x1, y1)

        painter.setPen(lastPen)

    def create(w, x, y, cx, cy, a, virtualA, painter, color=QColor('blue'), debug=False):
        gs = GraphicSensor(w, x, y, virtualA)
        gs.debug = debug
        gs.angle(a, cx, cy)
        gs.draw(painter, color)

        return gs
    create = staticmethod(create)

    def _getPointOnCircle(self, cx, cy, r, a):
        a = math.radians(a)
        x = cx + r * math.cos(a)
        y = cy + r * math.sin(a)

        return x, y

    def _getHalfSquareDiag(self, l):
        return (l * math.sqrt(2)) / 2

    def update(self):
        x, y = self._getPointOnCircle(
            self.graphX, self.graphY, self.halfDiag, self.virtualA + self.a)

        self.tx = x
        self.ty = y

        if x - self.graphX == 0:
            self.vert = True
            return
        else:
            self.vert = False

        self.coeff = (y - self.graphY) / (x - self.graphX)
        self.b = self.graphY - self.coeff * self.graphX

        return

    def _getY(self, x, d, a, lim):
        i = x
        y0 = self.coeff * x + self.b
        y = y0
        step = 0.1

        additive = False

        if self.virtualA <= 0:
            if a <= lim or a > lim+180:
                additive = True
        else:
            if a > lim+180 and a <= lim+180+180:
                additive = True

        while dist((x, y0), (i, y)) < d:
            y = self.coeff * i + self.b

            if additive:
                i += step
            else:
                i -= step

        return i, y
