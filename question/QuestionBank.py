# -*- coding: utf-8 -*-
# @Time    : 2022/7/28 17:21
# @Author  : Kazeya
# @File    : QuestionBank.py
# @Description : 题库、题单类

import pymysql
from DatabaseUtil import DB

from question.Question import Question


class QuestionBank:
    LOC = ['bank', 'list']

    # type 0->题库，1->题单
    def __init__(self, name, type):
        self._type = type
        self._name = name
        db = DB()
        db.cursor.execute('use base_name')
        db.cursor.execute("select * from " + self.LOC[self._type] + "_name where name=" + "'" + name + "'")
        info = db.cursor.fetchone()
        self._bid = info[0]
        self._fid = info[1]

    @classmethod
    def getBanks(cls):
        db.cursor.execute('use base_name')
        db.cursor.execute('select name from bank_name')
        infos = db.cursor.fetchall()
        banks = []
        for info in infos:
            banks.append(QuestionBank(info[0],0))
        return banks

    @classmethod
    def getLists(cls):
        db.cursor.execute('use base_name')
        db.cursor.execute('select name from list_name')
        infos = db.cursor.fetchall()
        lists = []
        for info in infos:
            lists.append(QuestionBank(info[0], 1))
        return lists

    def getBid(self):
        return self._bid

    def getFid(self):
        return self._fid

    def getName(self):
        return self._name

    def addQuestion(self, question: Question):
        db = DB()
        db.selectDatabase(self.LOC[self._type])
        sql = '(bid,stem,type,answer,analysis)'
        db.cursor.execute("insert into " + self._name + sql + 'values(' + question.toString() + ')')
        db.conn.commit()
        db.cursor.execute("select * from " + self._name + " where id=(select max(id) from " + self._name + ")")
        id = db.cursor.fetchone()[0]
        op = ord('A')
        for option in question.getOptions():
            db.cursor.execute(
                "update " + self._name + " set option" + chr(op) + "='" + option + "' " + "where id=" + str(id))
            db.conn.commit()
            op += 1

    def addQuestions(self, questions):
        for question in questions:
            self.addQuestion(question)

    def deleteQuestion(self, id):
        db = DB()
        db.selectDatabase(self.LOC[self._type])
        db.option("delete", self._name, id)
        db.conn.commit()

    def deleteQuestions(self, ids):
        for id in ids:
            self.deleteQuestion(id)

    def getQuestion(self, id):
        db = DB()
        db.selectDatabase(self.LOC[self._type])
        db.option("select", self._name, id)
        question = db.cursor.fetchone()
        options = [question[-5], question[-4], question[-3], question[-2], question[-1]]
        return Question(question[0], question[1], question[2], question[3], question[4], question[5], options)

    def getQuestions(self):
        db = DB()
        db.selectDatabase(self.LOC[self._type])
        db.cursor.execute("select * from " + self._name)
        rst = db.cursor.fetchall()
        questions = []
        for question in rst:
            questions.append(Question(question[0], question[1], question[2], question[3], question[4], question[5],
                                      [question[6], question[7], question[8], question[9], question[10]]))
        return questions


'''
    def readFromFileWithPath(self, filePath):
        qdata = pd.read_csv(filePath,encoding='utf-8')
        for data in qdata.values:
            self.addQuestion(data)

    def createBank(self):
        open(self.getPath(),'w',encoding='utf-8')

    def saveBank(self):
        qList = sorted(self._list.values(),key=lambda x:x[2])
        df = pd.DataFrame(data=qList,columns=['id','stem','type','answer','analysis','options'])
        df.to_csv(self.getPath(),index=False)

    def getPath(self):
        return './data/' + self.LOC[self._type] + '/' + self._name + '.csv'
'''

if __name__ == '__main__':
    db = DB()
    # db.create Bank("科目一","bank")
    bank = QuestionBank("科目一", 0)
    # for i in range(150):
    bank.addQuestion(Question(4,1,'a',1,'bad','cc',['a','b','c']))
    banks = bank.getBanks()
    for b in banks:
        print(b.getName())
    lists = bank.getLists()
    for l in lists:
        print(l.getName())