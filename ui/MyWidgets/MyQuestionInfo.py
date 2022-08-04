from ui.MyWidgets.QuestionInfo import Ui_Form
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *
from question.Question import *
from user.User import CUR_USER


class MyQuestionInfo(Ui_Form, QWidget):
    backSignal = pyqtSignal()

    def __init__(self, parent):
        super(MyQuestionInfo, self).__init__(parent)
        self.setupUi(self)
        self.seeAnswerFlag.clicked.connect(self.showAnswer)
        self.backButton.clicked.connect(self.back)
        self.likeButton.clicked.connect(self.like)

        self.question = None

    def show(self, question: Question = None):
        self.question = question
        if question:
            print("ok")
            # 主客观题的差异化设置
            if question.getType() == CHOICE:
                self.setObjectQuestion(question)
            else:
                self.setSubjectQuestion(question)
            # 相同的设置
            self.seeAnswerFlag.setChecked(False)
            self.answerText.setText(question.getAnswer() + "\n" + question.getAnalysis())
            self.answerText.hide()
            if True:
                # TODO
                self.likeButton.setText("取消收藏")
            else:
                self.likeButton.setText("收藏")
        super(Ui_Form, self).show()

    def setObjectQuestion(self, question: Question):
        self.stackedWidget.setCurrentIndex(1)
        self.objectQuestion.setText(question.getStem())
        # TODO 根据question设置
        # 设置选项
        for child in self.selectionBox.children():
            if isinstance(child, QCheckBox):
                self.selectionBoxLayout.removeWidget(child)
        options = question.getOptions()
        for i in range(len(options)):
            if not options[i]:
                continue
            newSelection = QCheckBox()
            newSelection.setText(chr(ord('A') + i) + options[i])
            newSelection.setCheckable(True)
            newSelection.setChecked(False)
            self.selectionBoxLayout.addWidget(newSelection)

    def setSubjectQuestion(self, question: Question):
        self.stackedWidget.setCurrentIndex(0)
        self.subjectQuestion.setText(question.getStem())

    def showAnswer(self):
        if self.seeAnswerFlag.isChecked():
            self.answerText.show()
        else:
            self.answerText.hide()

    def back(self):
        self.backSignal.emit()

    def like(self):
        if True:
            # TODO 如果未收藏
            self.likeButton.setText("收藏")
            CUR_USER.addLike(self.question.getBid(), self.question.getIndex())
        else:
            self.likeButton.setText("取消收藏")
