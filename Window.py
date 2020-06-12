import sys
from threading import Thread
import time

from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class WindowUpdater(Thread):
    def __init__(self, window):
        Thread.__init__(self)
        self.window = window

    def run(self):
        while self.window.running:
            self.window.update()
            time.sleep(0.001)


class Window(QWidget):
    def __init__(self, title, x, y, width, height):
        super().__init__()
        self.running = True

        self.setGeometry(x, y, width, height)
        self.setWindowTitle(title)

        self.updater = WindowUpdater(self)

    def run(self):
        self.show()

        self.updater.start()

    def closeEvent(self, event):
        self.running = False
        self.updater.join()
