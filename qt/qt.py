# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(848, 730)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 2, 0, 1, 3)
        self.scroll = QtWidgets.QScrollBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scroll.sizePolicy().hasHeightForWidth())
        self.scroll.setSizePolicy(sizePolicy)
        self.scroll.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.scroll.setOrientation(QtCore.Qt.Vertical)
        self.scroll.setObjectName("scroll")
        self.gridLayout.addWidget(self.scroll, 1, 0, 1, 1)
        self.pushButton_find = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_find.sizePolicy().hasHeightForWidth())
        self.pushButton_find.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(13)
        self.pushButton_find.setFont(font)
        self.pushButton_find.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_find.setObjectName("pushButton_find")
        self.gridLayout.addWidget(self.pushButton_find, 2, 3, 1, 1)
        self.map = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.map.sizePolicy().hasHeightForWidth())
        self.map.setSizePolicy(sizePolicy)
        self.map.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.map.setText("")
        self.map.setPixmap(QtGui.QPixmap("../../../OneDrive/Рабочий стол/Screenshot_2.png"))
        self.map.setScaledContents(True)
        self.map.setObjectName("map")
        self.gridLayout.addWidget(self.map, 1, 1, 1, 3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_sxema = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_sxema.sizePolicy().hasHeightForWidth())
        self.pushButton_sxema.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(12)
        self.pushButton_sxema.setFont(font)
        self.pushButton_sxema.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_sxema.setObjectName("pushButton_sxema")
        self.horizontalLayout.addWidget(self.pushButton_sxema)
        self.pushButton_sputnik = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_sputnik.sizePolicy().hasHeightForWidth())
        self.pushButton_sputnik.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(12)
        self.pushButton_sputnik.setFont(font)
        self.pushButton_sputnik.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_sputnik.setObjectName("pushButton_sputnik")
        self.horizontalLayout.addWidget(self.pushButton_sputnik)
        self.pushButton_gibrid = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_gibrid.sizePolicy().hasHeightForWidth())
        self.pushButton_gibrid.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(12)
        self.pushButton_gibrid.setFont(font)
        self.pushButton_gibrid.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_gibrid.setObjectName("pushButton_gibrid")
        self.horizontalLayout.addWidget(self.pushButton_gibrid)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 848, 26))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu.addAction(self.action)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_find.setText(_translate("MainWindow", "Искать"))
        self.pushButton_sxema.setText(_translate("MainWindow", "схема"))
        self.pushButton_sputnik.setText(_translate("MainWindow", "спутник"))
        self.pushButton_gibrid.setText(_translate("MainWindow", "гибрид"))
        self.menu.setTitle(_translate("MainWindow", "меню"))
        self.action.setText(_translate("MainWindow", "Сброс поискового результата"))