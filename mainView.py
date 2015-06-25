# -*- coding: UTF-8 -*-
'''
Created on 2015年6月14日

@author: Mathew Wang
'''

from Tkinter import *
from DBOperations import *

#提交数据
def confirmTrans(v1, v2, v3, v4):
    print(v1.get(), v2.get(), v3.get(), v4.get())

window = Tk()
window.geometry('800x600+400+100')

frame = Frame(window)
frame.pack()


programs = DBOperations.getAllPrograms()

#将checkbox的绑定值初始化
#for i in range(len(programs)):
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
checks = [var1,var2,var3,var4]

for (pro_id, pro_name) in programs:
    check = Checkbutton(frame, text=pro_name, variable=checks[pro_id-1])
    check.pack(side='left')

confirmBtn = Button(frame, text='确定', command=lambda:confirmTrans(var1,var2,var3,var4))

confirmBtn.pack(side='left')

window.mainloop()


#开始打印
'''import PrinterManage
import time

from PrinterManage import *

if __name__ == '__main__':
    printerManage = PrinterManage.GetInstance()
    now = int(time.time()) 
    timeArray = time.localtime(now)
    otherStyleTime = time.strftime("%Y/%m/%d", timeArray)    
    printerManage.sendToPrinter(1,'王卫','122334',100.2,
                                '洗-吹-剪',200.2,otherStyleTime)'''

'''def PrintInfo(info):
    print info.decode('utf-8').encode('gbk')  
    
    
import time
#import UserInfoBean

from DBOperations import *
from UserInfoBean import *

if __name__ == '__main__':
    #获得当前时间时间戳
    now = int(time.time()) 
    timeArray = time.localtime(now)
    otherStyleTime = time.strftime("%Y/%m/%d", timeArray)
    #DBOperations.addOneUser('132156','雅松',0,'18521037392',otherStyleTime,300)
    userInfo = DBOperations.getUserInfoByName('王卫')
    userInfo2 = DBOperations.getUserInfoByName('王卫')
    PrintInfo(userInfo.birth)
    print(userInfo2.id)'''

