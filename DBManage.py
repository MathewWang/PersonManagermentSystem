# -*- coding: UTF-8 -*-
'''
created by Mathew Wang

created date 2015/06/22

'''

#格式化打印log
def PrintInfo(info):
    print info.decode('utf-8').encode('gbk')  
    
    
import threading
import sqlite3 as dbapi

class DBManage():
    instance=None
    mutex=threading.Lock()
    
    def _init__(self):
        pass
    
    
    @staticmethod
    def GetInstance():
        if(DBManage.instance==None):
            DBManage.mutex.acquire()
            if(DBManage.instance==None):
                PrintInfo('初始化实例')
                DBManage.instance=DBManage()
            else:
                PrintInfo('单例已经实例化')
            DBManage.mutex.release()
        else:
            PrintInfo('单例已经实例化')
           
        return DBManage.instance
    
    def DBConnect(self):
        '''connect to the database'''
        self.connect = dbapi.connect('UserManagement.db')
        self.connect.text_factory = str
        PrintInfo('数据库连接成功')
    
    def DBClose(self):
        '''close the database connection'''
        self.connect.close()
        PrintInfo('数据库关闭成功')
        
'''def clientUI():
    dbManage = DBManage.GetInstance()
    dbManage.DBConnect()
    cur = dbManage.connect.cursor()
    cur.execute('SELECT * FROM jz_users')
    print(cur.fetchone()[2])
    dbManage.DBClose()
   
    return
if __name__=='__main__':
    clientUI();'''
    