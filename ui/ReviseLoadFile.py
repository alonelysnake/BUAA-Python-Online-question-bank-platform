# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\coding\python\homework\Online-question-bank-platform\ui\ReviseLoadFile.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.nextButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextButton.sizePolicy().hasHeightForWidth())
        self.nextButton.setSizePolicy(sizePolicy)
        self.nextButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nextButton.setObjectName("nextButton")
        self.gridLayout.addWidget(self.nextButton, 5, 1, 1, 1)
        self.selectButton = QtWidgets.QRadioButton(self.centralwidget)
        self.selectButton.setChecked(True)
        self.selectButton.setObjectName("selectButton")
        self.gridLayout.addWidget(self.selectButton, 2, 1, 1, 1)
        self.fillButton = QtWidgets.QRadioButton(self.centralwidget)
        self.fillButton.setObjectName("fillButton")
        self.gridLayout.addWidget(self.fillButton, 3, 1, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.object = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.object.sizePolicy().hasHeightForWidth())
        self.object.setSizePolicy(sizePolicy)
        self.object.setObjectName("object")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.object)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.objectlabel_2 = QtWidgets.QLabel(self.object)
        self.objectlabel_2.setObjectName("objectlabel_2")
        self.gridLayout_2.addWidget(self.objectlabel_2, 5, 0, 1, 1)
        self.objectExplanation = QtWidgets.QTextEdit(self.object)
        self.objectExplanation.setObjectName("objectExplanation")
        self.gridLayout_2.addWidget(self.objectExplanation, 6, 3, 1, 1)
        self.objectQuestion = QtWidgets.QTextEdit(self.object)
        self.objectQuestion.setObjectName("objectQuestion")
        self.gridLayout_2.addWidget(self.objectQuestion, 4, 0, 1, 4)
        self.objectlabel_3 = QtWidgets.QLabel(self.object)
        self.objectlabel_3.setObjectName("objectlabel_3")
        self.gridLayout_2.addWidget(self.objectlabel_3, 5, 3, 1, 1)
        self.objectlabel_1 = QtWidgets.QLabel(self.object)
        self.objectlabel_1.setObjectName("objectlabel_1")
        self.gridLayout_2.addWidget(self.objectlabel_1, 1, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.object)
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 276, 172))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 6, 0, 1, 1)
        self.stackedWidget.addWidget(self.object)
        self.subject = QtWidgets.QWidget()
        self.subject.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.subject.setObjectName("subject")
        self.subjectLayout = QtWidgets.QVBoxLayout(self.subject)
        self.subjectLayout.setObjectName("subjectLayout")
        self.subjectlabel_2 = QtWidgets.QLabel(self.subject)
        self.subjectlabel_2.setObjectName("subjectlabel_2")
        self.subjectLayout.addWidget(self.subjectlabel_2)
        self.subjectQuestion = QtWidgets.QTextEdit(self.subject)
        self.subjectQuestion.setObjectName("subjectQuestion")
        self.subjectLayout.addWidget(self.subjectQuestion)
        self.subjectlabel_1 = QtWidgets.QLabel(self.subject)
        self.subjectlabel_1.setObjectName("subjectlabel_1")
        self.subjectLayout.addWidget(self.subjectlabel_1)
        self.subjectAnswer = QtWidgets.QTextEdit(self.subject)
        self.subjectAnswer.setObjectName("subjectAnswer")
        self.subjectLayout.addWidget(self.subjectAnswer)
        self.stackedWidget.addWidget(self.subject)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.answerButton = QtWidgets.QRadioButton(self.centralwidget)
        self.answerButton.setCheckable(True)
        self.answerButton.setObjectName("answerButton")
        self.gridLayout.addWidget(self.answerButton, 4, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nextButton.setText(_translate("MainWindow", "下一题"))
        self.selectButton.setText(_translate("MainWindow", "选择题"))
        self.fillButton.setText(_translate("MainWindow", "填空题"))
        self.objectlabel_2.setText(_translate("MainWindow", "选项与答案"))
        self.objectlabel_3.setText(_translate("MainWindow", "答案解析"))
        self.objectlabel_1.setText(_translate("MainWindow", "问题描述"))
        self.subjectlabel_2.setText(_translate("MainWindow", "问题描述"))
        self.subjectlabel_1.setText(_translate("MainWindow", "答案与解析"))
        self.answerButton.setText(_translate("MainWindow", "解答题"))
