from PyQt5.QtGui import QColor, QPainter, QPen

from RotateRect import RotateRect
from Sensor import GraphicSensor

class GraphicCar(object):
    def __init__(self, baseWidth, baseHeight, canvas,x ,y):
        self.graphic_x = x
        self.graphic_y = y

        self.graphic_a = 0

        self.graphic_w = baseWidth * 5
        self.graphic_h = baseHeight * 4

        self.canvas = canvas

        self.lastMove = None

        self.side = True

        self.saveLast()

    def saveLast(self):
        self.graphic_lastX = self.graphic_x
        self.graphic_lastY = self.graphic_y
        self.graphic_lastA = self.graphic_a
        self.graphic_lastW = self.graphic_w
        self.graphic_lastH = self.graphic_h

    def _drawCar(self, painter, color, frontColor, x, y, a, w, h):
        RotateRect.create(x=x, y=y,
                          w=w, h=h, a=0+a, painter=painter, color=color, debug=False)

        sensorWidth = 4
        self.gs3 = GraphicSensor.create(sensorWidth, x, y - h/2 +
                                   sensorWidth/2, x, y, a, -90, painter, self.canvas, frontColor)

        self.gs4 = GraphicSensor.create(sensorWidth, x + w/2 - sensorWidth/2, y - h/2 +
                                   sensorWidth/2, x, y, a, -45, painter, self.canvas, frontColor)
        self.gs5 = GraphicSensor.create(sensorWidth, x + w/2 - sensorWidth/2, y - h/2 +
                                   sensorWidth*1.5, x, y, a, 0, painter, self.canvas, frontColor)

        self.gs2 = GraphicSensor.create(sensorWidth, x - w/2 + sensorWidth/2, y - h/2 +
                                   sensorWidth/2, x, y, a, 225, painter, self.canvas, frontColor)
        self.gs1 = GraphicSensor.create(sensorWidth, x - w/2 + sensorWidth/2, y - h/2 +
                                   sensorWidth*1.5, x, y, a, 180, painter, self.canvas, frontColor)

        return

    def getSensor(self) :
        return [self.gs1.Dist(), self.gs2.Dist(), self.gs3.Dist(), self.gs4.Dist(), self.gs5.Dist()]

    def draw(self, painter, color=QColor('red')):
        self._drawCar(x=self.graphic_lastX, y=self.graphic_lastY,
                      w=self.graphic_lastW, h=self.graphic_lastH, a=self.graphic_lastA, painter=painter, color=QColor('white'), frontColor=QColor('white'))
        self._drawCar(x=self.graphic_x, y=self.graphic_y,
                      w=self.graphic_w, h=self.graphic_h, a=self.graphic_a, painter=painter, color=color, frontColor=QColor('blue'))
        painter.end()
        self.saveLast()

    def clear(self, painter) :
        self._drawCar(x=self.graphic_lastX, y=self.graphic_lastY,
                      w=self.graphic_lastW, h=self.graphic_lastH, a=self.graphic_lastA, painter=painter, color=QColor('white'), frontColor=QColor('white'))

        self._drawCar(x=self.graphic_x, y=self.graphic_y,
                      w=self.graphic_w, h=self.graphic_h, a=self.graphic_a, painter=painter, color=QColor('white'), frontColor=QColor('white'))

    def collides(self, color):
        startX = self.graphic_lastX
        endX = self.graphic_x
        startY = self.graphic_lastY
        endY = self.graphic_y
        diff = 0

        if self.side:
            xmin = int(self.graphic_x - self.graphic_h / 2)
            xmax = int(self.graphic_x + self.graphic_h / 2)
            xlim = int(self.canvas.width())

            ymin = int(self.graphic_y - self.graphic_w / 2)
            ymax = int(self.graphic_y + self.graphic_w / 2)
            ylim = int(self.canvas.height())

            startY = ymin
            endY = ymax
            if startX > endX:
                # diff = startX - endX
                tmp = startX - int(self.graphic_h / 2) + diff
                startX = endX - int(self.graphic_h / 2) + diff
                endX = tmp
            else:
                # diff = endX - startX
                startX += int(self.graphic_h / 2) - diff
                endX += int(self.graphic_h / 2) - diff
        else:
            xmin = int(self.graphic_x - self.graphic_w / 2)
            xmax = int(self.graphic_x + self.graphic_w / 2)
            xlim = int(self.canvas.width())

            ymin = int(self.graphic_y - self.graphic_h / 2)
            ymax = int(self.graphic_y + self.graphic_h / 2)
            ylim = int(self.canvas.height())

            startX = xmin
            endX = xmax
            if startY > endY:
                # diff = startY - endY
                tmp = startY - int(self.graphic_h / 2) + diff
                startY = endY - int(self.graphic_h / 2) + diff
                endY = tmp
            else:
                # diff = endY - startY
                startY += int(self.graphic_h / 2) - diff
                endY += int(self.graphic_h / 2) - diff

        if xmin < 0 or xmax > xlim:
            return True
        if ymin < 0 or ymax > ylim:
            return True

        img = self.canvas.pixmap().toImage()

        for x in range(startX, endX+1):
            for y in range(startY, endY+1):
                pixel = img.pixel(x, y)
                if QColor(pixel) == QColor('black'):
                    return True

        return False

    def move(self):
        pass

    def moveUp(self):
        self.move()
        self.graphic_y -= 10
        if self.collides(QColor('black')) or self.lastMove == "down":
            self.graphic_y += 10
            return False

        self.lastMove = "up"

        self.graphic_a = 0
        self.side = False

        return True

    def moveLeft(self):
        self.move()
        self.graphic_x -= 10
        if self.collides(QColor('black')) or self.lastMove == "right":
            self.graphic_x += 10
            return False

        self.lastMove = "left"

        self.graphic_a = -90
        self.side = True

        return True

    def moveDown(self):
        self.move()
        self.graphic_y += 10
        if self.collides(QColor('black')) or self.lastMove == "up":
            self.graphic_y -= 10
            return False

        self.lastMove = "down"

        self.graphic_a = 180
        self.side = False

        return True

    def moveRight(self):
        self.move()
        self.graphic_x += 10
        if self.collides(QColor('black')) or self.lastMove == "left":
            self.graphic_x -= 10
            return False

        self.lastMove = "right"

        self.graphic_a = 90
        self.side = True

        return True