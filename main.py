import os
import sys
from map import map
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt

SCREEN_SIZE = [600, 450]
FILE_NAME = 'map.png'
LONGITUDE = 33
LATTITUDE = 55
SPN = 25


class Example(QWidget):
    def __init__(self):
        super().__init__()
        map(LONGITUDE, LATTITUDE, SPN)
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, *SCREEN_SIZE)
        self.setWindowTitle('Отображение карты')
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(600, 450)
        self.new_map()

    def new_map(self):
        self.pixmap = QPixmap(FILE_NAME)
        self.image.setPixmap(self.pixmap)
        self.image.update()

    def closeEvent(self, event):
        os.remove(FILE_NAME)

    def keyPressEvent(self, event):
        global SPN
        if event.key() == Qt.Key_PageUp:
            if SPN >= 0:
                SPN -= SPN / 5
            map(LONGITUDE, LATTITUDE, SPN)
            self.new_map()
        if event.key() == Qt.Key_PageDown:
            if SPN >= 0:
                SPN += SPN / 5
            map(LONGITUDE, LATTITUDE, SPN)
            self.new_map()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())