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

        self.car = GraphicCar(10, 50, self.canvas)
        self.car.graphic_a = 0
        self.draw()

    def setMovingZone(self):
        self.pixmap = QPixmap(self.width() * 0.85, self.height() * 1)
        self.pixmap.fill(QColor('white'))

        self.canvas = QLabel()
        self.canvas.setPixmap(self.pixmap)
        self.canvas.setAlignment(Qt.AlignCenter)

        self.setMap()

    def draw(self):
        self.car.draw(painter=self.getPainter())

    def update(self):
        pass

    def getPainter(self):
        return QPainter(self.canvas.pixmap())

    def testButtonClicked(self):
        for angle in range(0, 361):
            self.car.graphic_a = angle
            self.updateCanvas()
            time.sleep(0.01)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Z:
            self.car.moveUp()
            self.updateCanvas()
        if event.key() == Qt.Key_Q:
            self.car.moveLeft()
            self.updateCanvas()
        if event.key() == Qt.Key_S:
            self.car.moveDown()
            self.updateCanvas()
        if event.key() == Qt.Key_D:
            self.car.moveRight()
            self.updateCanvas()

    def updateCanvas(self):
        self.setMap()
        self.draw()
        self.canvas.repaint()

    def setMap(self):
        w = 700
        h = 10
        RotateRect.create(x=20 + w/2, y=20 + h/2,
                          w=w, h=h, painter=self.getPainter(), color=QColor('black'))
