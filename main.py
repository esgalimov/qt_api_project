import os
import sys
from map import map
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt
from qt.qt_for_tasks_1_3 import *

FILE_NAME = 'map.png'
LONGITUDE = 33
LATTITUDE = 55
SPN = 25
MOVE = 10


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        map(LONGITUDE, LATTITUDE, SPN)
        self.initUI()

    def initUI(self):
        self.pixmap = QPixmap(FILE_NAME)
        self.new_map()

    def new_map(self):
        self.pixmap = QPixmap(FILE_NAME)
        self.map.setPixmap(self.pixmap)
        self.map.update()

    def closeEvent(self, event):
        os.remove(FILE_NAME)

    def keyPressEvent(self, event):
        global SPN, LONGITUDE, LATTITUDE
        if event.key() == Qt.Key_PageUp:
            if SPN >= 0:
                SPN -= SPN
        if event.key() == Qt.Key_PageDown:
            if SPN < 50:
                SPN += SPN
        if event.key() == Qt.Key_Left:
            if LONGITUDE > -170:
                LONGITUDE -= MOVE
        if event.key() == Qt.Key_Right:
            if LONGITUDE < 170:
                LONGITUDE += MOVE
        if event.key() == Qt.Key_Up:
            if LATTITUDE < 80:
                LATTITUDE += MOVE
        if event.key() == Qt.Key_Down:
            if LATTITUDE > -80:
                LATTITUDE -= MOVE
        map(LONGITUDE, LATTITUDE, SPN)
        self.new_map()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
