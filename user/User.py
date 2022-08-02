# -*- coding: utf-8 -*-
# @Time    : 2022/8/1 16:53
# @Author  : Kazeya
# @File    : User.py
# @Description :用户类
import time

from DatabaseUtil import DB

db = DB()


class User:
    def __init__(self):
        self.name = None
        self.id = None

    def setInfo(self, id, name):
        self.name = name
        self.id = id

    def addLike(self, bid: int, qid: int):
        if not self.isLogin:
            return
        db.selectDatabase('data')
        db.cursor.execute("insert into " + str(self.id) + "_likes(bid,qid) values('" + str(bid) + "','" + str(qid) + "')")
        db.conn.commit()

    def delLike(self, bid: int, qid: int):
        if not self.isLogin:
            return
        db.selectDatabase('data')
        db.cursor.execute("delete from " + str(self.id) + "_likes where bid='" + str(bid) + "' and qid='" + str(qid) + "'")
        db.conn.commit()

    # isWrong:0->正确，1->错误
    def addExercise(self, bid:int, qid:int, isWrong:int):
        if not self.isLogin:
            return
        db.selectDatabase('data')
        table = str(self.id) + "_mistakes(bid,qid,wrong_times,exc_times)"
        values = " values('" + str(bid) + "','" + str(qid) + "','" + str(isWrong) + "','1')"
        condition = " on duplicate key update wrong_times=wrong_times+" + str(isWrong) + ", exc_times=exc_times+1"
        db.cursor.execute("insert into " + table + values + condition)
        db.conn.commit()

    # mistakes: "index1,index2,index3,...", date:"yyyy-mm-dd hh:mm:ss"
    def addListExercise(self, bid:int, listName:str, mistakes:str, date:str):
        if not self.isLogin:
            return
        db.selectDatabase('data')
        values = "('" + str(bid) + "','" + listName + "','" + mistakes + "','" + date + "')"
        db.cursor.execute("insert into " + str(self.id) + "_logs(bid,name,mistakes,date) values" + values)
        db.conn.commit()

    @property
    def isLogin(self) -> bool:
        if self.id:
            return True
        else:
            print("用户未登录")
            return False


CUR_USER = User()


class UserUtil:
    @classmethod
    def login(cls, name: str, pwd: str) -> bool:
        user = db.fetchOne('data', 'users', 'name', name)
        if user is None or user[2] != pwd:
            print("用户名或密码错误")
            return False
        CUR_USER.setInfo(user[0], user[1])
        return True

    @classmethod
    def logout(cls):
        CUR_USER.setInfo(None, None)

    @classmethod
    def register(cls, name, pwd) -> bool:
        user = db.fetchOne('data', 'users', 'name', name)
        if user is not None:
            print("该用户已存在")
            return False
        db.cursor.execute("insert into users(name,pwd) values('" + name + "','" + pwd + "')")
        db.conn.commit()
        user = db.fetchOne('data', 'users', 'name', name)
        sql = str(user[0]) + """_likes(
            bid int not null,
            qid int not null,
            unique(bid,qid)
        )default charset=utf8;
        """
        db.cursor.execute("create table " + sql)
        sql = str(user[0]) + """_mistakes(
            bid int not null,
            qid int not null,
            wrong_times int not null,
            exc_times int not null,
            unique(bid,qid)
        )default charset=utf8;
        """
        db.cursor.execute("create table " + sql)
        sql = str(user[0]) + """_logs(
            bid int not null,
            name text(128) not null,
            mistakes text(512),
            date datetime
        )default charset=utf8;
        """
        db.cursor.execute("create table " + sql)
        db.conn.commit()
        return True

if __name__ == '__main__':
    UserUtil.register('Kazeya', '123456')
    CUR_USER.addLike(1, 1)
    UserUtil.login('Kazeya', '1234567')
    UserUtil.login('kazeyaa', '123456')
    UserUtil.login('Kazeya', '123456')
    CUR_USER.addLike(1, 1)
    CUR_USER.delLike(1, 1)
    CUR_USER.addExercise(1, 1, 0)
    CUR_USER.addExercise(1, 1, 1)
    CUR_USER.addExercise(1, 1, 1)
    CUR_USER.addExercise(1, 2, 1)
    CUR_USER.addListExercise(1,'科目一试卷1','11,13,15,17',time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))