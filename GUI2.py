# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\PyProg\GUI2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName("TabWidget")
        TabWidget.resize(1280, 784)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TabWidget.sizePolicy().hasHeightForWidth())
        TabWidget.setSizePolicy(sizePolicy)
        TabWidget.setMinimumSize(QtCore.QSize(700, 500))
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        TabWidget.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.pushButton = QtWidgets.QPushButton(self.tab2)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(50, 80, 75, 23))
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.webEngineView = QWebEngineView(self.tab2)
        self.webEngineView.setGeometry(QtCore.QRect(210, 50, 891, 611))
        self.webEngineView.setUrl(QtCore.QUrl("file:///D:/PyProg/temp-plot.html"))
        self.webEngineView.setObjectName("webEngineView")
        TabWidget.addTab(self.tab2, "")

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "TabWidget"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab1), _translate("TabWidget", "Tab 1"))
        self.pushButton.setText(_translate("TabWidget", "PushButton"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab2), _translate("TabWidget", "Tab 2"))

from QtWebEngineWidgets.QWebEngineView import QWebEngineView
