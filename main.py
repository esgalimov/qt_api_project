import os
import sys
from map import map, find_toponym
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit
from PyQt5.QtCore import Qt
from qt.qt import *

FILE_NAME = 'map.png'
LONGITUDE = 33
LATTITUDE = 55
SPN = [25, 18.75]
TYPE_OF_MAP = 'map'
NAMES = ['map.png', 'map.jpg']
PT = []


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.action.triggered.connect(self.clear_mark)
        self.pushButton_gibrid.clicked.connect(self.change_type)
        self.pushButton_sputnik.clicked.connect(self.change_type)
        self.pushButton_sxema.clicked.connect(self.change_type)
        self.pushButton_find.clicked.connect(self.find_place)
        self.pixmap = QPixmap(FILE_NAME)
        self.new_map()
        self.key_list = [Qt.Key_PageUp, Qt.Key_PageDown,
                         Qt.Key_Left, Qt.Key_Right,
                         Qt.Key_Up, Qt.Key_Down]
        self.oldKeyPressEvent = self.textEdit.keyPressEvent
        self.textEdit.keyPressEvent = self.newKeyPressEvent

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

    def find_place(self):
        global LONGITUDE, LATTITUDE, PT
        toponym = self.textEdit.toPlainText()
        new_coords = find_toponym(toponym)
        if new_coords:
            LONGITUDE = new_coords[0]
            LATTITUDE = new_coords[1]
            PT.append(','.join([str(new_coords[0]), str(new_coords[1])]) + ',org')
            self.new_map()

    def new_map(self):
        map(LONGITUDE, LATTITUDE, SPN, TYPE_OF_MAP, FILE_NAME, PT)
        self.pixmap = QPixmap(FILE_NAME)
        self.map.setPixmap(self.pixmap)
        self.map.update()

    def closeEvent(self, event):
        for i in NAMES:
            if os.path.exists(i):
                os.remove(i)

    # переопределяем event для textEdit
    def newKeyPressEvent(self, event):
        if event.key() in self.key_list:
            self.keyPressEvent(event)
        else:
            self.oldKeyPressEvent(event)

    def keyPressEvent(self, event):
        global SPN, LONGITUDE, LATTITUDE
        if event.key() == Qt.Key_PageUp:
            if SPN[0] >= 0 and SPN[1] >= 0:
                SPN[0] = round(SPN[0] * 0.5, 6)
                SPN[1] = round(SPN[1] * 0.5, 6)
        if event.key() == Qt.Key_PageDown:
            if SPN[0] < 26 and SPN[1] < 26:
                SPN[0] = round(SPN[0] * 2, 6)
                SPN[1] = round(SPN[1] * 2, 6)
        if event.key() == Qt.Key_Left:
            LONGITUDE -= SPN[0]
            if LONGITUDE < -180:
                LONGITUDE = 360 + LONGITUDE
        if event.key() == Qt.Key_Right:
            LONGITUDE += SPN[0]
            if LONGITUDE > 180:
                LONGITUDE = -360 + LONGITUDE
        if event.key() == Qt.Key_Up:
            LATTITUDE += SPN[1]
            if LATTITUDE > 85:
                LATTITUDE = 85
        if event.key() == Qt.Key_Down:
            LATTITUDE -= SPN[1]
            if LATTITUDE < -85:
                LATTITUDE = -85
        self.new_map()

    def clear_mark(self):
        PT.clear()
        self.new_map()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
