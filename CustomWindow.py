from GraphicCar import GraphicCar
from Window import Window

import sys
import time

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from RotateRect import *


class CustomWindow(Window):
    def __init__(self, title, x, y, width, height):
        super().__init__(title, x, y, width, height)

        self.mainHBoxLayout = QHBoxLayout()
        self.managementVBoxLayout = QVBoxLayout()

        self.setMovingZone()

        self.testButton = QPushButton()
        self.testButton.setText("Test")
        self.testButton.clicked.connect(self.testButtonClicked)

        self.managementVBoxLayout.addWidget(self.testButton)

        self.mainHBoxLayout.addLayout(self.managementVBoxLayout)
        self.mainHBoxLayout.addWidget(self.canvas)

        # self.window.setLayout(self.mainHBoxLayout)
        self.setLayout(self.mainHBoxLayout)

        self.testAngle = 0

        self.one = True
        carW = 5
        carH = 15
        if self.one:
            self.car = GraphicCar(carW, carH, self.canvas, 75, 60)
            self.car.graphic_a = 180
        else:
            self.cars = [GraphicCar(carW, carH, self.canvas), GraphicCar(
                carW, carH, self.canvas), GraphicCar(carW, carH, self.canvas), GraphicCar(carW, carH, self.canvas), GraphicCar(carW, carH, self.canvas), GraphicCar(carW, carH, self.canvas), GraphicCar(carW, carH, self.canvas), GraphicCar(carW, carH, self.canvas), GraphicCar(carW, carH, self.canvas), GraphicCar(carW, carH, self.canvas)]

        self.draw()

    def setMovingZone(self):
        self.pixmap = QPixmap(self.width() * 0.85, self.height() * 1)
        self.pixmap.fill(QColor('white'))

        self.canvas = QLabel()
        self.canvas.setPixmap(self.pixmap)
        self.canvas.setAlignment(Qt.AlignCenter)

        self.setMap()

    def draw(self):
        if self.one:
            self.car.draw(painter=self.getPainter())
        else:
            for car in self.cars:
                car.draw(painter=self.getPainter())

    def update(self):
        return

    def getPainter(self):
        return QPainter(self.canvas.pixmap())

    def testButtonClicked(self):
        for angle in range(0, 361):
            if self.one:
                self.car.graphic_a = angle
            else:
                for car in self.cars:
                    car.graphic_a = angle
            self.updateCanvas()
            time.sleep(0.01)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Z:
            if self.one:
                self.car.moveUp()
            else:
                for car in self.cars:
                    car.moveUp()
        if event.key() == Qt.Key_Q:
            if self.one:
                self.car.moveLeft()
            else:
                for car in self.cars:
                    car.moveLeft()
        if event.key() == Qt.Key_S:
            if self.one:
                self.car.moveDown()
            else:
                for car in self.cars:
                    car.moveDown()
        if event.key() == Qt.Key_D:
            if self.one:
                self.car.moveRight()
            else:
                for car in self.cars:
                    car.moveRight()
        if event.key() == Qt.Key_A:
            self.testAngle += 1
            if self.testAngle > 360:
                self.testAngle = 0

            if self.one:
                self.car.graphic_a = self.testAngle
            else:
                for car in self.cars:
                    car.graphic_a = self.testAngle
            self.updateCanvas()
        self.updateCanvas()

    def updateCanvas(self):
        self.setMap()
        self.draw()
        self.setMap()
        self.canvas.repaint()

    def setHWall(self, painter, x, y, w, h, a=0):
        RotateRect.create(x=x + w/2, y=y + h/2,
                          w=w, h=h, painter=painter, color=QColor('black'), a=0+a)

    def setVWall(self, painter, x, y, w, h, a=0):
        RotateRect.create(x=x + h/2, y=y + w/2,
                          w=w, h=h, painter=painter, color=QColor('black'), a=90+a)

    def setMap(self):
        wmax = self.width() * 0.85
        hmax = self.height()
        thickness = 10
        painter = self.getPainter()

        self.setHWall(painter, 0, 0, wmax, thickness)
        self.setHWall(painter, 0, hmax - thickness, wmax, thickness)
        self.setVWall(painter, 0, 0, hmax, thickness)
        self.setVWall(painter, wmax - thickness, 0, hmax, thickness)

        w = 150
        h = thickness
        self.setVWall(painter, w, h, 100, thickness)
        w -= 5
        h += 90
        self.setVWall(painter, w, h, 100, thickness, 10)
        w -= 25
        h += 90
        self.setVWall(painter, w, h, 200, thickness, 10)
        w -= 20
        h += 195
        self.setVWall(painter, w, h, 200, thickness)
        h += 220
        self.setHWall(painter, w, h, 200, thickness, 15)

        w += 190
        h -= 460
        self.setVWall(painter, w, h, 500, thickness, 2)
        w += 20
        h -= 180
        self.setVWall(painter, w, h, 200, thickness, 10)

        self.setHWall(painter, w+100, h+40, 100, thickness, 10)
        self.setHWall(painter, w+100, h+150, 100, thickness, -10)

        w += 100
        h += 160
        self.setVWall(painter, w, h, 600, thickness, -2)

        w += 90
        h -= 85
        self.setHWall(painter, w, h, 200, thickness, 15)
        self.setHWall(painter, w, h+90, 200, thickness, 15)

        w += 180
        h += 80
        self.setHWall(painter, w, h, 250, thickness, 25)
        self.setHWall(painter, w, h+90, 250, thickness, 25)

        painter.end()
