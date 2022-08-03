from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import pyqtSignal, Qt
import sys

from question.Question import *
from question.QuestionBank import QuestionBank

from ui.MainWindow import Ui_MainWindow
from ui.MyWidgets.MyQuestionCard import MyQuestionCard
from ui.MyChooseLoadFile import MyChooseLoadFile
from ui.MyChooseQuestion import MyChooseQuestion
from ui.MyRegister import MyRegister
from ui.MyLogin import MyLogin


class MyMainWindow(Ui_MainWindow, QMainWindow):
    switch2reviseFile = pyqtSignal(QMainWindow, str)  # 跳转到上传后修改的信号

    def __init__(self, mainWindow, bank: QuestionBank):
        super(MyMainWindow, self).__init__()
        self.setupUi(mainWindow)
        self.mainWindow = mainWindow
        self.questions = {}  # questions集合
        self.questionDetail.backSignal.connect(self.backFromDetail)
        self.addQuestionButton.triggered.connect(self.uploadFileEvent)
        self.selfTestButton.triggered.connect(self.selfTestEvent)
        self.registerButton.triggered.connect(self.registerEvent)
        self.loginButton.triggered.connect(self.loginEvent)
        self.questionCategoryLayout.setAlignment(Qt.AlignTop)

        self.bank = bank
        self.updateQuestions()

    # 主界面到上传界面
    def uploadFileEvent(self):
        dialog = QDialog()
        uploadWindow = MyChooseLoadFile(dialog)
        if dialog.exec_() == QDialog.Accepted:
            # TODO 识别文件并跳转到修改界面
            self.switch2reviseFile.emit(self.mainWindow, uploadWindow.filepath)
            pass
        else:
            # 取消读取，正常返回
            pass

    # 主界面到自测界面
    def selfTestEvent(self):
        newWindow = QMainWindow()
        chooseWindow = MyChooseQuestion(newWindow, self, self.bank, self.questions)
        newWindow.show()

    def registerEvent(self):
        dialog = QDialog()
        registerWindow = MyRegister(dialog)
        print("gg")
        res = dialog.exec_()
        while res != QDialog.Accepted and res != QDialog.Rejected:
            res = dialog.exec_()

    def loginEvent(self):
        dialog = QDialog()
        loginWindow = MyLogin(dialog)
        res = dialog.exec_()
        while res != QDialog.Accepted and res != QDialog.Rejected:
            res = dialog.exec_()

    def seeDetail(self, index):
        self.menuBar.hide()
        self.stackedWidget.setCurrentIndex(1)
        question = self.questions[index]
        self.questionDetail.show(question=question)

    def backFromDetail(self):
        self.menuBar.show()
        self.stackedWidget.setCurrentIndex(0)

    def updateQuestions(self):
        for question in self.bank.getQuestions():
            assert isinstance(question, Question)
            index = question.getIndex()
            if index not in self.questions.keys():
                self.questions[index] = question
                newQuestionCard = MyQuestionCard(self.questionCategory, index, False)
                newQuestionCard.setText(str(question.getIndex()))
                newQuestionCard.clickDetail.connect(self.seeDetail)
                self.questionCategoryLayout.addWidget(newQuestionCard)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    bank = QuestionBank("科目一", 0)
    mainWindow = MyMainWindow(window, bank)
    # dialog.show()
    window.show()
    app.exec_()
    # print("filepath: " + chooseFile.filepath)
    # print(dialog.exec_() == QDialog.Rejected)
    sys.exit()
