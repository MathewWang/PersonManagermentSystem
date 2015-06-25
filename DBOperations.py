# -*- coding: UTF-8 -*-
'''
created by Mathew Wang
created date 2015/06/22

database operations
'''
#格式化打印log
def PrintInfo(info):
    print info.decode('utf-8').encode('gbk')  
    
import DBManage
import UserInfoBean
from UserInfoBean import *
from DBManage import *

class DBOperations(object):
    
    @staticmethod
    def addOneUser(jz_NO, jz_name, jz_gender, 
                   jz_mobile, jz_birth, jz_money):
        '''插入一条用户信息到数据库中'''
        PrintInfo('插入一条用户信息，用户名%s'%jz_name)
        dbManage = DBManage.GetInstance()
        dbManage.DBConnect()
        cur = dbManage.connect.cursor()
        cur.execute('INSERT INTO jz_users \
                     (jz_NO, jz_name, jz_gender, jz_mobile, jz_birth, jz_money)\
                     values (?,?,?,?,?,?)', (jz_NO, jz_name, jz_gender, 
                   jz_mobile, jz_birth, jz_money))
        dbManage.connect.commit()
        dbManage.DBClose()
        PrintInfo('用户名%s插入成功'%jz_name)
    
    @staticmethod    
    def getUserInfoByName(jz_name):
        '''根据用户名获取用户信息'''
        PrintInfo('获取用户信息，用户名%s'%jz_name)
        dbManage = DBManage.GetInstance()
        dbManage.DBConnect()
        cur = dbManage.connect.cursor()
        cur.execute('SELECT * FROM jz_users WHERE jz_name = "%s"'%jz_name)
        userInfo = cur.fetchone()
        dbManage.DBClose()
        PrintInfo('用户名%s获取成功'%jz_name)
        userBean = UserInfoBean(userInfo)
        return userBean
        
    @staticmethod    
    def getUserInfoByMobile(jz_mobile):
        '''根据手机号获取用户信息'''
        PrintInfo('获取用户信息，手机号%s'%jz_mobile)
        dbManage = DBManage.GetInstance()
        dbManage.DBConnect()
        cur = dbManage.connect.cursor()
        cur.execute('SELECT * FROM jz_users WHERE jz_mobile = "%s"'%jz_mobile)
        userInfo = cur.fetchone()
        dbManage.DBClose()
        PrintInfo('手机号%s获取成功'%jz_mobile)
        userBean = UserInfoBean(userInfo)
        return userBean

    
    
    @staticmethod    
    def getUserInfoByNO(jz_NO):
        '''根据手机号获取用户信息'''
        PrintInfo('获取用户信息，会员号%s'%jz_NO)
        dbManage = DBManage.GetInstance()
        dbManage.DBConnect()
        cur = dbManage.connect.cursor()
        cur.execute('SELECT * FROM jz_users WHERE jz_mobile = "%s"'%jz_NO)
        userInfo = cur.fetchone()
        dbManage.DBClose()
        PrintInfo('会员号%s获取成功'%jz_NO)
        userBean = UserInfoBean(userInfo)
        return userBean
    
    @staticmethod
    def addOneTransaction(jz_id, pro_id, amount):
        '''插入一条用户消费记录'''
        PrintInfo('插入一条消费信息，用Id%d'%jz_id)
        #获取当前时间
        now = int(time.time()) 
        timeArray = time.localtime(now)
        otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)            
        
        dbManage = DBManage.GetInstance()
        dbManage.DBConnect()
        cur = dbManage.connect.cursor() 
        #插入一条消费记录
        cur.execute('INSERT INTO jz_pro_trans \
                     (jz_id, pro_id, tran_amount, tran_date)\
                     values (?,?,?,?)', (jz_id, pro_id, amount, 
                   otherStyleTime))
        #更新用户的总额
        cur.execute('UPDATE jz_users SET jz_money = (jz_money - %.2f) \
                      WHERE jz_id = %d'%(amount, jz_id))
        
        dbManage.connect.commit()
        dbManage.DBClose()
        PrintInfo('用户%d插入消费信息成功'%jz_id) 
    
    
    @staticmethod
    def getAllPrograms():
        '''获取所有的消费项目'''
        dbManage = DBManage.GetInstance()
        dbManage.DBConnect()
        cur = dbManage.connect.cursor()
        cur.execute('SELECT * FROM jz_programs')
        programs = cur.fetchall()
        dbManage.DBClose()
        PrintInfo('获取所有的消费项目成功')
        return programs        