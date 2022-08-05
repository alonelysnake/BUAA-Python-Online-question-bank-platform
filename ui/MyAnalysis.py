from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

# from function.ScoreAnalysis import ApplicationWindow

from question.QuestionBank import QuestionBank
from question.Question import Question
from user.User import CUR_USER

from ui.Analysis import Ui_MainWindow
from ui.MyWidgets.MyQuestionInfo import MyQuestionInfo
from ui.MyWidgets.MyQuestionCard import MyQuestionCard
from ui.MyWidgets.MyBankCard import MyBankCard


class MyAnalysis(Ui_MainWindow, QMainWindow):
    def __init__(self, window, parent, bank: QuestionBank):
        super(MyAnalysis, self).__init__(parent=parent)
        self.setupUi(window)
        self.analysisCardsLayout.setAlignment(Qt.AlignTop)
        self.wrongQuestionsLayout.setAlignment(Qt.AlignTop)

        self.bank = bank

        self.analysisButton.clicked.connect(self.analysisButtonEvent)
        self.wrongButton.clicked.connect(self.wrongButtonEvent)
        print("b")
        self.loadAnalysisCards()
        self.loadWrongQuestionCards()
        print("c")
        self.analysisButtonEvent()

    def analysisButtonEvent(self):
        self.stackedWidget.setCurrentIndex(0)
        self.analysisButton.setDisabled(True)
        self.wrongButton.setDisabled(False)

    def wrongButtonEvent(self):
        self.stackedWidget.setCurrentIndex(1)
        self.wrongButton.setDisabled(True)
        self.analysisButton.setDisabled(False)

    # 查看详细的分析结果图
    def seeAnalysis(self, bid):
        # analysisWindow = ApplicationWindow(CUR_USER.getLogs(bid))
        # analysisWindow.show()
        pass

    # 查看错题的详细内容
    def seeWrongDetail(self, bid, qid):
        self.stackedWidget.setCurrentIndex(3)
        self.questionInfo.show(self.bank.getQuestion(qid))

    #题单
    def loadAnalysisCards(self):

        print(QuestionBank.getBanks())
        print("d")
        for bank in QuestionBank.getBanks():
            print(type(bank))
            assert isinstance(bank, QuestionBank)
            analysisCard = MyBankCard(self.analysisCards, bank)
            analysisCard.clickDetail.connect(self.seeAnalysis)
            self.analysisCardsLayout.addWidget(analysisCard)

    def loadWrongQuestionCards(self):
        for question in CUR_USER.getMistakes(self.bank):
            print(1)
            print(type(question))
            assert isinstance(question, Question)
            newQuestionCard = MyQuestionCard(self.wrongQuestions, question.getIndex(), question.getBid())
            newQuestionCard.setText(str(question.getIndex()) + ". " + question.getStem())
            newQuestionCard.clickDetail.connect(self.seeWrongDetail)
            self.wrongQuestionsLayout.addWidget(newQuestionCard)
