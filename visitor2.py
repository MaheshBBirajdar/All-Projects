# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visitor1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from db1 import mysql_connect
import pyqrcode 
import time 


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sender_label = QtWidgets.QLabel(self.centralwidget)
        self.sender_label.setGeometry(QtCore.QRect(60, 40, 91, 19))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sender_label.setFont(font)
        self.sender_label.setObjectName("sender_label")
        self.visitor_label = QtWidgets.QLabel(self.centralwidget)
        self.visitor_label.setGeometry(QtCore.QRect(60, 140, 68, 19))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.visitor_label.setFont(font)
        self.visitor_label.setObjectName("visitor_label")
        self.time_label = QtWidgets.QLabel(self.centralwidget)
        self.time_label.setGeometry(QtCore.QRect(60, 230, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.time_label.setFont(font)
        self.time_label.setObjectName("time_label")
        self.sender_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.sender_lineEdit.setGeometry(QtCore.QRect(170, 30, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sender_lineEdit.setFont(font)
        self.sender_lineEdit.setObjectName("sender_lineEdit")
        self.visitor_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.visitor_lineEdit.setGeometry(QtCore.QRect(170, 130, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.visitor_lineEdit.setFont(font)
        self.visitor_lineEdit.setObjectName("visitor_lineEdit")
        self.time_dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.time_dateTimeEdit.setGeometry(QtCore.QRect(180, 230, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.time_dateTimeEdit.setFont(font)
        self.time_dateTimeEdit.setObjectName("time_dateTimeEdit")
        self.submit_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.submit_pushButton.setGeometry(QtCore.QRect(300, 340, 112, 34))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.submit_pushButton.setFont(font)
        self.submit_pushButton.setObjectName("submit_pushButton")
        self.mysql_label = QtWidgets.QLabel(self.centralwidget)
        self.mysql_label.setGeometry(QtCore.QRect(110, 400, 591, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mysql_label.setFont(font)
        self.mysql_label.setText("")
        self.mysql_label.setObjectName("mysql_label")
        self.qr_label = QtWidgets.QLabel(self.centralwidget)
        self.qr_label.setGeometry(QtCore.QRect(150, 470, 511, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qr_label.setFont(font)
        self.qr_label.setText("")
        self.qr_label.setObjectName("qr_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menubar.setObjectName("menubar")
        self.menuVisitor_App = QtWidgets.QMenu(self.menubar)
        self.menuVisitor_App.setObjectName("menuVisitor_App")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuVisitor_App.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def data(self):
        t1 = self.time_dateTimeEdit.text()
        s1 = self.sender_lineEdit.text()
        v1 = self.visitor_lineEdit.text()
        try:
            mydb = mysql_connect()
            cur = mydb.cursor()
            q3 = "insert into visitor_management (sender,visitor,timing,status) values (%s,%s,%s,%s)"
            val = (s1,v1,t1,1)
            cur.execute(q3,val)
            mydb.commit()
            self.mysql_label.setText("record added")
            qr = pyqrcode.create(f"('{s1}','{v1}','{t1}')")
            t3 = str(int(time.time()))
            file_name = "qr\\" + v1 + "-" + t3 + ".png" 
            qr.png(file_name,scale = 6)
            self.qr_label.setText("QR code generated")
            
        except Exception as e:
            print(e)
            self.mysql_label.setText(e)
        finally:
            cur.close()
            mydb.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sender_label.setText(_translate("MainWindow", "Sender"))
        self.visitor_label.setText(_translate("MainWindow", "Visitor"))
        self.time_label.setText(_translate("MainWindow", "Timing"))
        self.submit_pushButton.setText(_translate("MainWindow", "Submit"))
        self.menuVisitor_App.setTitle(_translate("MainWindow", "Visitor App"))
        self.submit_pushButton.clicked.connect(self.data)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

