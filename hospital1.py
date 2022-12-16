# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hospital.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import time
from db1 import mysql_connect


class Ui_Hospital_Form(object):
    def setupUi(self, Hospital_Form):
        Hospital_Form.setObjectName("Hospital_Form")
        Hospital_Form.resize(750, 541)
        font = QtGui.QFont()
        font.setPointSize(10)
        Hospital_Form.setFont(font)
        self.patient_label = QtWidgets.QLabel(Hospital_Form)
        self.patient_label.setGeometry(QtCore.QRect(80, 60, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.patient_label.setFont(font)
        self.patient_label.setObjectName("patient_label")
        self.Hospital_label = QtWidgets.QLabel(Hospital_Form)
        self.Hospital_label.setGeometry(QtCore.QRect(80, 150, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Hospital_label.setFont(font)
        self.Hospital_label.setObjectName("Hospital_label")
        self.medicine_label = QtWidgets.QLabel(Hospital_Form)
        self.medicine_label.setGeometry(QtCore.QRect(80, 260, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.medicine_label.setFont(font)
        self.medicine_label.setObjectName("medicine_label")
        self.patient_lineEdit = QtWidgets.QLineEdit(Hospital_Form)
        self.patient_lineEdit.setGeometry(QtCore.QRect(260, 60, 113, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.patient_lineEdit.setFont(font)
        self.patient_lineEdit.setObjectName("patient_lineEdit")
        self.hospital_lineEdit = QtWidgets.QLineEdit(Hospital_Form)
        self.hospital_lineEdit.setGeometry(QtCore.QRect(260, 150, 113, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hospital_lineEdit.setFont(font)
        self.hospital_lineEdit.setObjectName("hospital_lineEdit")
        self.medicine_lineEdit = QtWidgets.QLineEdit(Hospital_Form)
        self.medicine_lineEdit.setGeometry(QtCore.QRect(250, 230, 421, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.medicine_lineEdit.setFont(font)
        self.medicine_lineEdit.setObjectName("medicine_lineEdit")
        self.submit_pushButton = QtWidgets.QPushButton(Hospital_Form)
        self.submit_pushButton.setGeometry(QtCore.QRect(330, 370, 112, 34))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.submit_pushButton.setFont(font)
        self.submit_pushButton.setObjectName("submit_pushButton")
        self.otp_label = QtWidgets.QLabel(Hospital_Form)
        self.otp_label.setGeometry(QtCore.QRect(190, 440, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.otp_label.setFont(font)
        self.otp_label.setObjectName("otp_label")

        self.done_label = QtWidgets.QLabel(Hospital_Form)
        self.done_label.setGeometry(QtCore.QRect(490, 440, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.done_label.setFont(font)
        self.done_label.setText("")
        self.done_label.setObjectName("done_label")

        self.retranslateUi(Hospital_Form)
        QtCore.QMetaObject.connectSlotsByName(Hospital_Form)

    def data(self):
        try: 
            self.patient_uid = self.patient_lineEdit.text()
            self.hospital_uid = self.hospital_lineEdit.text()  
            self.medicine = self.medicine_lineEdit.text()
            self.status = 1
            self.time1 = int(time.time())
            self.otp = self.patient_uid + str(self.time1)
            self.otp_label.setText(self.otp)
            
            mydb = mysql_connect()
            cur = mydb.cursor()
            sql = "insert into hospital (patient_id, hospital_id, medicine, date1, status,otp) values (%s,%s,%s,%s,%s,%s)"
            val = (self.patient_uid, self.hospital_uid, self.medicine, self.time1, self.status, self.otp)
            cur.execute(sql,val)
            mydb.commit()
            self.done_label.setText("Done")
            
        except Exception as e:
            print(e)


    def retranslateUi(self, Hospital_Form):
        _translate = QtCore.QCoreApplication.translate
        Hospital_Form.setWindowTitle(_translate("Hospital_Form", "Form"))
        self.patient_label.setText(_translate("Hospital_Form", "Patient ID"))
        self.Hospital_label.setText(_translate("Hospital_Form", "Hospital ID"))
        self.medicine_label.setText(_translate("Hospital_Form", "Medicines"))
        self.submit_pushButton.setText(_translate("Hospital_Form", "Submit"))
        self.otp_label.setText(_translate("Hospital_Form", "OTP"))
        self.submit_pushButton.clicked.connect(self.data)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Hospital_Form = QtWidgets.QWidget()
    ui = Ui_Hospital_Form()
    ui.setupUi(Hospital_Form)
    Hospital_Form.show()
    sys.exit(app.exec_())

