# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\coding\python\homework\Online-question-bank-platform\ui\MyWidgets\BankCard.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bankName = QtWidgets.QLabel(Form)
        self.bankName.setMaximumSize(QtCore.QSize(16777215, 30))
        self.bankName.setText("")
        self.bankName.setObjectName("bankName")
        self.horizontalLayout.addWidget(self.bankName)
        self.detailButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.detailButton.sizePolicy().hasHeightForWidth())
        self.detailButton.setSizePolicy(sizePolicy)
        self.detailButton.setObjectName("detailButton")
        self.horizontalLayout.addWidget(self.detailButton)
        self.testButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.testButton.sizePolicy().hasHeightForWidth())
        self.testButton.setSizePolicy(sizePolicy)
        self.testButton.setObjectName("testButton")
        self.horizontalLayout.addWidget(self.testButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.detailButton.setText(_translate("Form", "查看详情"))
        self.testButton.setText(_translate("Form", "开始测试"))
