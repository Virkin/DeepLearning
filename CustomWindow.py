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

        self.one = False
        carW = 5
        carH = 15
        if self.one:
            self.car = GraphicCar(carW, carH, self.canvas)
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
        pass

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
        self.updateCanvas()

    def updateCanvas(self):
        self.setMap()
        self.draw()
        self.setMap()
        self.canvas.repaint()

    def setMap(self):
        w = 700
        h = 10
        RotateRect.create(x=20 + w/2, y=20 + h/2,
                          w=w, h=h, painter=self.getPainter(), color=QColor('black'))
        RotateRect.create(x=20 + w/2, y=600 + h/2,
                          w=w, h=h, painter=self.getPainter(), color=QColor('black'))
        RotateRect.create(x=20, y=300 + h/2,
                          w=w, h=h, painter=self.getPainter(), color=QColor('black'), a=90)
        RotateRect.create(x=500 + w/2, y=300 + h/2,
                          w=w, h=h, painter=self.getPainter(), color=QColor('black'), a=90)
