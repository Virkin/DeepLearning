from PyQt5.QtGui import QColor, QPen

from RotateRect import RotateRect


class GraphicCar(object):
    def __init__(self, baseWidth, baseHeight, canvas, x=400, y=300):
        self.graphic_x = x
        self.graphic_y = y

        self.graphic_a = 0

        self.graphic_w = baseWidth * 5
        self.graphic_h = baseHeight * 4

        self.canvas = canvas

        self.saveLast()

    def saveLast(self):
        self.graphic_lastX = self.graphic_x
        self.graphic_lastY = self.graphic_y
        self.graphic_lastA = self.graphic_a
        self.graphic_lastW = self.graphic_w
        self.graphic_lastH = self.graphic_h

    def _drawCar(self, painter, color, frontColor, x, y, a, w, h):
        RotateRect.create(x=x, y=y,
                          w=w, h=h, a=0+a, painter=painter, color=color, debug=True)

        # RotateRect.create(x=x, y=y-h/2+5, a=a,
        #                   painter=painter, color=frontColor, w=10, h=10, rx=x, ry=y)

        # RotateRect.create(x=x-w/2+5, y=y-h/2+5, a=a,
        #                   painter=painter, color=frontColor, w=10, h=10, rx=x, ry=y)
        # RotateRect.create(x=x+w/2-5, y=y-h/2+5, a=a,
        #                   painter=painter, color=frontColor, w=10, h=10, rx=x, ry=y)

        # RotateRect.create(x=x-w/2+5, y=y-h/2+15, a=a,
        #                   painter=painter, color=frontColor, w=10, h=10, rx=x, ry=y)
        # RotateRect.create(x=x+w/2-5, y=y-h/2+15, a=a,
        #                   painter=painter, color=frontColor, w=10, h=10, rx=x, ry=y)

    def draw(self, painter, color=QColor('red')):
        self._drawCar(x=self.graphic_lastX, y=self.graphic_lastY,
                      w=self.graphic_lastW, h=self.graphic_lastH, a=self.graphic_lastA, painter=painter, color=QColor('white'), frontColor=QColor('white'))
        self._drawCar(x=self.graphic_x, y=self.graphic_y,
                      w=self.graphic_w, h=self.graphic_h, a=self.graphic_a, painter=painter, color=color, frontColor=QColor('blue'))
        painter.end()
        self.saveLast()

    def collides(self, color):
        xmin = self.graphic_x - self.graphic_h / 2
        xmax = self.graphic_x + self.graphic_h / 2
        xlim = self.canvas.width()

        ymin = self.graphic_y - self.graphic_h / 2
        ymax = self.graphic_y + self.graphic_h / 2
        ylim = self.canvas.height()

        if xmin < 0 or xmax > xlim:
            return True
        if ymin < 0 or ymax > ylim:
            return True

        return False

    def moveUp(self):
        self.graphic_y -= 10
        if self.collides(QColor('black')):
            self.graphic_y += 10
            return

        self.graphic_a = 0

    def moveLeft(self):
        self.graphic_x -= 10
        if self.collides(QColor('black')):
            self.graphic_x += 10
        self.graphic_a = -90

    def moveDown(self):
        self.graphic_y += 10
        if self.collides(QColor('black')):
            self.graphic_y -= 10
        self.graphic_a = 180

    def moveRight(self):
        self.graphic_x += 10
        if self.collides(QColor('black')):
            self.graphic_x -= 10
        self.graphic_a = 90
