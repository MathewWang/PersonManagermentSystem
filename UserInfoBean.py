# -*- coding: UTF-8 -*-
'''
created by Mathew Wang
created date 2015/06/22

database beans
'''

class UserInfoBean(object):
    '''用户信息的bean'''
    
    def __init__(self, userInfo):
        '''根据数组初始化用户的bean,ORM 映射'''
        self.id = userInfo[0]
        self.NO = userInfo[1]
        self.name = userInfo[2]
        self.gender = userInfo[3]
        self.mobile = userInfo[4]
        self.birth = userInfo[5]
        self.money = userInfo[6]