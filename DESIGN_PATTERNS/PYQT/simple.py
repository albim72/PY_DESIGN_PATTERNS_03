# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simple.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(380, 349)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 40, 239, 25))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.verticalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setMouseTracking(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 100, 158, 16))
        self.label.setMinimumSize(QtCore.QSize(158, 0))
        self.label.setObjectName("label")
        self.etImie = QtWidgets.QTextEdit(Dialog)
        self.etImie.setGeometry(QtCore.QRect(100, 100, 239, 21))
        self.etImie.setMinimumSize(QtCore.QSize(158, 0))
        self.etImie.setObjectName("etImie")
        self.etNazwisko = QtWidgets.QTextEdit(Dialog)
        self.etNazwisko.setGeometry(QtCore.QRect(100, 140, 239, 21))
        self.etNazwisko.setMinimumSize(QtCore.QSize(158, 0))
        self.etNazwisko.setObjectName("etNazwisko")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 158, 16))
        self.label_2.setMinimumSize(QtCore.QSize(158, 0))
        self.label_2.setObjectName("label_2")
        self.etMiasto = QtWidgets.QTextEdit(Dialog)
        self.etMiasto.setGeometry(QtCore.QRect(100, 180, 239, 21))
        self.etMiasto.setMinimumSize(QtCore.QSize(158, 0))
        self.etMiasto.setObjectName("etMiasto")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 180, 158, 16))
        self.label_3.setMinimumSize(QtCore.QSize(158, 0))
        self.label_3.setObjectName("label_3")
        self.cbZawod = QtWidgets.QComboBox(Dialog)
        self.cbZawod.setGeometry(QtCore.QRect(100, 240, 221, 22))
        self.cbZawod.setObjectName("cbZawod")
        self.cbZawod.addItem("")
        self.cbZawod.addItem("")
        self.cbZawod.addItem("")
        self.cbZawod.addItem("")
        self.cbZawod.addItem("")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 240, 158, 16))
        self.label_4.setMinimumSize(QtCore.QSize(158, 0))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Otwórz"))
        self.pushButton_3.setText(_translate("Dialog", "Zamknij"))
        self.pushButton_2.setText(_translate("Dialog", "Eksportuj"))
        self.label.setText(_translate("Dialog", "Imię"))
        self.label_2.setText(_translate("Dialog", "Nazwisko"))
        self.label_3.setText(_translate("Dialog", "Miasto"))
        self.cbZawod.setItemText(0, _translate("Dialog", "Dyrektor"))
        self.cbZawod.setItemText(1, _translate("Dialog", "Sekretarka"))
        self.cbZawod.setItemText(2, _translate("Dialog", "Kierowca"))
        self.cbZawod.setItemText(3, _translate("Dialog", "Programista"))
        self.cbZawod.setItemText(4, _translate("Dialog", "Asystent Finansowy"))
        self.label_4.setText(_translate("Dialog", "Stanowisko"))
