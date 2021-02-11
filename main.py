import os
import sys
from map import map
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt
from qt.qt import *

FILE_NAME = 'map.png'
LONGITUDE = 33
LATTITUDE = 55
SPN = 25
MOVE = 10
TYPE_OF_MAP = 'map'
NAMES = ['map.png', 'map.jpg']


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        map(LONGITUDE, LATTITUDE, SPN, TYPE_OF_MAP, FILE_NAME)
        self.initUI()

    def initUI(self):
        self.pushButton_gibrid.clicked.connect(self.change_type)
        self.pushButton_sputnik.clicked.connect(self.change_type)
        self.pushButton_sxema.clicked.connect(self.change_type)

        self.pixmap = QPixmap(FILE_NAME)
        self.new_map()

    def change_type(self):
        global TYPE_OF_MAP, FILE_NAME
        if self.sender() == self.pushButton_gibrid:
            TYPE_OF_MAP = 'sat,skl'
            FILE_NAME = NAMES[1]
        elif self.sender() == self.pushButton_sputnik:
            TYPE_OF_MAP = 'sat'
            FILE_NAME = NAMES[1]
        elif self.sender() == self.pushButton_sxema:
            TYPE_OF_MAP = 'map'
            FILE_NAME = NAMES[0]
        self.new_map()

    def new_map(self):
        map(LONGITUDE, LATTITUDE, SPN, TYPE_OF_MAP, FILE_NAME)
        self.pixmap = QPixmap(FILE_NAME)
        self.map.setPixmap(self.pixmap)
        self.map.update()

    def closeEvent(self, event):
        for i in NAMES:
            if os.path.exists(i):
                os.remove(i)

    def keyPressEvent(self, event):
        global SPN, LONGITUDE, LATTITUDE
        if event.key() == Qt.Key_PageUp:
            if SPN >= 0:
                SPN = round(SPN * 0.5, 6)
        if event.key() == Qt.Key_PageDown:
            if SPN < 26:
                SPN = round(SPN * 1.5, 6)
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
        self.new_map()
        print(LONGITUDE, LATTITUDE, SPN, TYPE_OF_MAP)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
