import sys
from PyQt5.QtWidgets import QApplication

from CustomWindow import CustomWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # window()
    window = CustomWindow(title="DeepLearning - Cars", x=100,
                          y=100, width=1080, height=720)
    window.run()

    sys.exit(app.exec_())
