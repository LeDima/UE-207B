# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\GitTestProject\UE-207B\GUI2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName("TabWidget")
        TabWidget.resize(1285, 784)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TabWidget.sizePolicy().hasHeightForWidth())
        TabWidget.setSizePolicy(sizePolicy)
        TabWidget.setMinimumSize(QtCore.QSize(700, 500))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        TabWidget.setFont(font)
        TabWidget.setIconSize(QtCore.QSize(16, 16))
        self.VacTab = QtWidgets.QWidget()
        self.VacTab.setObjectName("VacTab")
        self.mplfigs = QtWidgets.QListView(self.VacTab)
        self.mplfigs.setGeometry(QtCore.QRect(90, 110, 301, 601))
        self.mplfigs.setObjectName("mplfigs")
        self.mplwindow = QtWidgets.QWidget(self.VacTab)
        self.mplwindow.setGeometry(QtCore.QRect(430, 40, 651, 661))
        self.mplwindow.setAcceptDrops(False)
        self.mplwindow.setObjectName("mplwindow")
        TabWidget.addTab(self.VacTab, "")
        self.MainTab = QtWidgets.QWidget()
        self.MainTab.setObjectName("MainTab")
        self.pushButton = QtWidgets.QPushButton(self.MainTab)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(50, 80, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.webView = QtWebKitWidgets.QWebView(self.MainTab)
        self.webView.setGeometry(QtCore.QRect(70, 120, 1211, 621))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webView.sizePolicy().hasHeightForWidth())
        self.webView.setSizePolicy(sizePolicy)
        self.webView.setUrl(QtCore.QUrl("file:///D:/PyProg/temp-plot.html"))
        self.webView.setObjectName("webView")
        TabWidget.addTab(self.MainTab, "")
        self.B1Tab = QtWidgets.QWidget()
        self.B1Tab.setObjectName("B1Tab")
        TabWidget.addTab(self.B1Tab, "")
        self.B2Tab = QtWidgets.QWidget()
        self.B2Tab.setObjectName("B2Tab")
        TabWidget.addTab(self.B2Tab, "")
        self.B3_4Tab = QtWidgets.QWidget()
        self.B3_4Tab.setObjectName("B3_4Tab")
        TabWidget.addTab(self.B3_4Tab, "")

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "TabWidget"))
        TabWidget.setTabText(TabWidget.indexOf(self.VacTab), _translate("TabWidget", "Общие настройки"))
        self.pushButton.setText(_translate("TabWidget", "PushButton"))
        TabWidget.setTabText(TabWidget.indexOf(self.MainTab), _translate("TabWidget", "Управление вакуумом"))
        TabWidget.setTabText(TabWidget.indexOf(self.B1Tab), _translate("TabWidget", "Пушка 1 "))
        TabWidget.setTabText(TabWidget.indexOf(self.B2Tab), _translate("TabWidget", "Пушка 2"))
        TabWidget.setTabText(TabWidget.indexOf(self.B3_4Tab), _translate("TabWidget", "Пушка 3, 4"))

from PyQt5 import QtWebKitWidgets
