from PyQt5.QtGui import QColor, QPainter, QPen

from RotateRect import RotateRect
from Sensor import GraphicSensor


class GraphicCar(object):
    def __init__(self, baseWidth, baseHeight, canvas, x=400, y=300):
        self.graphic_x = x
        self.graphic_y = y

        self.graphic_a = 0

        self.graphic_w = baseWidth * 5
        self.graphic_h = baseHeight * 4

        self.canvas = canvas

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
        gs1 = GraphicSensor.create(sensorWidth, x, y - h/2 +
                                   sensorWidth/2, x, y, a, 0-90, painter, frontColor, True)

        gs3 = GraphicSensor.create(sensorWidth, x + w/2 - sensorWidth/2, y - h/2 +
                                   sensorWidth/2, x, y, a, 45-90, painter, frontColor)
        gs5 = GraphicSensor.create(sensorWidth, x + w/2 - sensorWidth/2, y - h/2 +
                                   sensorWidth*1.5, x, y, a, 90-90, painter, frontColor)

        gs2 = GraphicSensor.create(sensorWidth, x - w/2 + sensorWidth/2, y - h/2 +
                                   sensorWidth/2, x, y, a, -45-90, painter, frontColor)
        gs4 = GraphicSensor.create(sensorWidth, x - w/2 + sensorWidth/2, y - h/2 +
                                   sensorWidth*1.5, x, y, a, -90-90, painter, frontColor)

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
        return

    def draw(self, painter, color=QColor('red')):
        self._drawCar(x=self.graphic_lastX, y=self.graphic_lastY,
                      w=self.graphic_lastW, h=self.graphic_lastH, a=self.graphic_lastA, painter=painter, color=QColor('white'), frontColor=QColor('white'))
        print("")
        self._drawCar(x=self.graphic_x, y=self.graphic_y,
                      w=self.graphic_w, h=self.graphic_h, a=self.graphic_a, painter=painter, color=color, frontColor=QColor('blue'))
        painter.end()
        self.saveLast()

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
                color = QColor(pixel).getRgbF()
                if QColor(pixel) == QColor('black'):
                    return True

        return False

    def move(self):
        pass

    def moveUp(self):
        self.move()
        self.graphic_y -= 10
        if self.collides(QColor('black')):
            self.graphic_y += 10
            return

        self.graphic_a = 0
        self.side = False

    def moveLeft(self):
        self.move()
        self.graphic_x -= 10
        if self.collides(QColor('black')):
            self.graphic_x += 10
            return

        self.graphic_a = -90
        self.side = True

    def moveDown(self):
        self.move()
        self.graphic_y += 10
        if self.collides(QColor('black')):
            self.graphic_y -= 10
            return

        self.graphic_a = 180
        self.side = False

    def moveRight(self):
        self.move()
        self.graphic_x += 10
        if self.collides(QColor('black')):
            self.graphic_x -= 10
            return

        self.graphic_a = 90
        self.side = True
