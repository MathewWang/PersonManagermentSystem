# -*- coding: UTF-8 -*-
'''
Created on 2015年6月14日

@author: Mathew Wang

printer module
'''
#格式化打印log
def PrintInfo(info):
    print info.decode('utf-8').encode('gbk')  
    

import win32ui 
import win32print 
import win32con 
import threading

class PrinterManage(object):
    '''打印模块所有方法'''
    
    printerInstance=None
    printerMutex=threading.Lock()
    
    def _init__(self):
        pass
    
    
    @staticmethod
    def GetInstance():
        if(PrinterManage.printerInstance==None):
            PrinterManage.printerMutex.acquire()
            if(PrinterManage.printerInstance==None):
                PrintInfo('初始化打印机实例')
                PrinterManage.printerInstance=PrinterManage()
            else:
                PrintInfo('打印单例已经实例化')
            PrinterManage.printerMutex.release()
        else:
            PrintInfo('打印单例已经实例化')
           
        return PrinterManage.printerInstance
    
    
    def sendToPrinter(self,tranId, userName, userNO, remainAmont, 
                      program, amont, dateTime):
        '''发送数据到打印机'''
        PrintInfo('开始打印')
        '''transID = ('单号：%d'%tranId).decode('utf-8').encode('gb2312')
        userNumber = ('会员号：%s'%userNO).decode('utf-8').encode('gb2312')
        title = '极致本色'.decode('utf-8').encode('gb2312')
        comp =  '*******极致本色********'.decode('utf-8').encode('gb2312')
        program = ('项目：%s'%program).decode('utf-8').encode('gb2312')
        name =  ('姓名：%s'%userName).decode('utf-8').encode('gb2312')
        date =  ('日期：%s'%dateTime).decode('utf-8').encode('gb2312')
        consum =  ('金额：%.2f￥'%amont).decode('utf-8').encode('gb2312')
        ramain =  ('余额：%.2f￥'%remainAmont).decode('utf-8').encode('gb2312')
        sign =  '签名：'.decode('utf-8').encode('gb2312')
        thx =  '谢谢光临'.decode('utf-8').encode('gb2312')      
    
        txt = comp + '\n\n' + transID + '\n' + userNumber + '\n' \
            + program + '\n' + name + '\n' \
            + date + '\n' + consum+ '\n' + ramain + '\n' \
            + sign+ '\n\n' + thx
        self.doc = win32ui.CreateDC()
        self.doc.CreatePrinterDC(win32print.GetDefaultPrinter())
        self.doc.StartDoc(title)
        self.doc.StartPage()
        self.doc.SetMapMode(win32con.MM_TWIPS)
        
        leftMargin = 10
        topMargin = 0
        width = 11500
        height = -25000
        
        self.doc.DrawText(txt,(leftMargin,topMargin,width,height)
                          ,win32con.DT_LEFT)
        self.doc.EndPage()
        self.doc.EndDoc()'''
        PrintInfo('打印结束')
        
    