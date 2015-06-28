# -*- coding: UTF-8 -*-
'''
Created on 2015年6月14日

@author: Mathew Wang
'''
from Dialog import *
from Tkinter import *
from DBOperations import *
from PrinterManage import *
import time


window = Tk()
window.wm_title("极致本色")
window.geometry('800x600+400+100')

'''用户消费信息模块'''
frame = Frame(window, borderwidth=4, relief=GROOVE)
frame
frame.pack(side='left', fill=Y)


programs = DBOperations.getAllPrograms()

#将checkbox的绑定值初始化
#所有的理发项目
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
checks = [var1,var2,var3,var4]

for (pro_id, pro_name) in programs:
    check = Checkbutton(frame, text=pro_name, variable=checks[pro_id-1])
    check.grid(column=pro_id-1, row=1)

confirmBtn = Button(frame, text='确定', command=lambda:popupWindow())

confirmBtn.grid(column=3, row=8)

#输入框
frameTitle = Label(frame, text='输入用户消费信息')
frameTitle.grid(column=0, row=0, columnspan=4)

#名字
nameField = StringVar()
nameLabel = Label(frame, text="姓名")
nameEntry = Entry(frame, textvariable=nameField)
nameLabel.grid(column=0, row=2)
nameEntry.grid(column=1, row=2, columnspan=3)
#手机号码
phoneField = StringVar()
phoneLabel = Label(frame, text="手机号")
phoneEntry = Entry(frame, textvariable=phoneField)
phoneLabel.grid(column=0, row=3)
phoneEntry.grid(column=1, row=3, columnspan=3)
#会员号
numberField = StringVar()
numberLabel = Label(frame, text="会员号")
numberEntry = Entry(frame, textvariable=numberField)
numberLabel.grid(column=0, row=4)
numberEntry.grid(column=1, row=4, columnspan=3)

#消费金额
amountField = DoubleVar()
amountLabel = Label(frame, text='消费总额')
amountEntry = Entry(frame, textvariable=amountField)
amountLabel.grid(column=0, row=5)
amountEntry.grid(column=1, row=5, columnspan=3)

#关闭窗口
def termiantWindow(child):
    child.destroy()

#展示打印页面
def popupWindow():

    consumeUserInfo = None
    
    if  (len(nameField.get()) > 0):
        consumeUserInfo = DBOperations.getUserInfoByName(nameField.get())
    elif (len(phoneField.get()) > 0):
        consumeUserInfo = DBOperations.getUserInfoByMobile(phoneField.get())
    elif (len(numberField.get()) > 0):
        consumeUserInfo = DBOperations.getUserInfoByNO(numberField.get())  

    
    programStr = None
    if (var1.get() > 0):
        programStr = '洗'
    if (var2.get() > 0):
        programStr += ',吹'
    if (var3.get() > 0):
        programStr += ',剪'
    if (var4.get() > 0):
        programStr += ',造型'
        
    if (consumeUserInfo != None and programStr != None):
        printerWindow = Toplevel()
        printerWindow.wm_title('确认信息')
        printerWindow.geometry('200x100+600+150')
        
        footer = Frame(printerWindow)
        footer.pack(side='bottom', fill=X)
        
        #姓名
        printerStr = '姓名：' + '\n' + '消费项目:'+ programStr + '\n' \
                      + '总消费金额：'+ str(amountField.get())+'￥'    
        printerText = Label(printerWindow, 
                            text = printerStr, bg='white').pack(side='top')
        
        cancelBtn = Button(footer, text='取消', 
                          command=lambda m = printerWindow :termiantWindow(m))
        printBtn = Button(footer, text='确定', 
                          command=lambda m = printerWindow :confirmTrans(m,consumeUserInfo,programStr))
        cancelBtn.pack(side='left', anchor=SW)
        printBtn.pack(side='right', anchor=SE)        
    else:
        Dialog(frame, title='提示', text='请补全信息', 
                    bitmap=DIALOG_ICON, default=0, strings=('取消','确定')
               )        
    
#提交数据
def confirmTrans(child, usrModel, pro_str):
    programId = 0
    if (var1.get() > 0):
        programId += 0
    if (var2.get() > 0):
        programId += 1
    if (var3.get() > 0):
        programId += 2
    if (var4.get() > 0):
        programId += 4    
    consumTranId = DBOperations.addOneTransaction(usrModel.id, programId, 
                                   amountField.get())
    
    termiantWindow(child)
    
    printerManage = PrinterManage.GetInstance()
    now = int(time.time()) 
    timeArray = time.localtime(now)
    otherStyleTime = time.strftime("%Y/%m/%d", timeArray)  
    
    afterUserInfo = DBOperations.getUserInfoByNO(usrModel.NO) 


    printerManage.sendToPrinter(consumTranId,afterUserInfo.name,afterUserInfo.NO,
                                amountField.get(),pro_str,
                                afterUserInfo.money,otherStyleTime,0)      
    printerManage.sendToPrinter(consumTranId,afterUserInfo.name,afterUserInfo.NO,
                                amountField.get(),pro_str,
                                afterUserInfo.money,otherStyleTime,1)     
    Dialog(frame, title='提示', text='消费信息录入成功', 
                bitmap=DIALOG_ICON, default=0, strings=('取消','确定')
            )

        



'''添加用户信息模块'''
usrModelFrame = Frame(window, borderwidth=4, relief=GROOVE)
usrModelFrame.pack(side='left', fill=Y)

userModelTitle = Label(usrModelFrame, text='添加用户信息')
userModelTitle.grid(column=0, row=0, columnspan=3)

#会员号
memberNOField = StringVar()
memberNOLabel = Label(usrModelFrame, text='会员号')
memberNOEntry = Entry(usrModelFrame, textvariable=memberNOField)
memberNOLabel.grid(column=0, row=1)
memberNOEntry.grid(column=1, row=1, columnspan=2)

#姓名
memberNameField = StringVar()
memberNameLabel = Label(usrModelFrame, text='姓名')
memberNameEntry = Entry(usrModelFrame, textvariable=memberNameField)
memberNameLabel.grid(column=0, row=2)
memberNameEntry.grid(column=1, row=2, columnspan=2)

#性别
memberGenderLabel = Label(usrModelFrame, text='性别')
memberGender = IntVar()
memberMale = Radiobutton(usrModelFrame, text="男", 
                         variable=memberGender, value=0)
memberFemal = Radiobutton(usrModelFrame, text="女", 
                          variable=memberGender, value=1)
memberGenderLabel.grid(column=0, row=3)
memberMale.grid(column=1, row=3)
memberFemal.grid(column=2, row=3)

#手机号
memberPhoneField = StringVar()
memberPhoneLabel = Label(usrModelFrame, text='手机号')
memberPhoneEntry = Entry(usrModelFrame, textvariable=memberPhoneField)
memberPhoneLabel.grid(column=0, row=4)
memberPhoneEntry.grid(column=1, row=4, columnspan=2)

#生日
memberBirthField = StringVar()
memberBirthLabel = Label(usrModelFrame, text='生日')
memberBirthEntry = Entry(usrModelFrame, textvariable=memberBirthField)
memberBirthLabel.grid(column=0, row=5)
memberBirthEntry.grid(column=1, row=5, columnspan=2)

#总金额
memberAmontField = DoubleVar()
memberAmontLabel = Label(usrModelFrame, text='金额')
memberAmontEntry = Entry(usrModelFrame, textvariable=memberAmontField)
memberAmontLabel.grid(column=0, row=6)
memberAmontEntry.grid(column=1, row=6, columnspan=2)

#添加按钮
addMemberBtn = Button(usrModelFrame, text='添加', command=lambda:popConfirm())
addMemberBtn.grid(column=2, row=7)

addUserInfo = None

def popConfirm():

    addUserInfo = DBOperations.getUserInfoByName(memberNameField.get())
    if (addUserInfo == None):
        addUserInfo = DBOperations.getUserInfoByMobile(memberPhoneField.get())
    if (addUserInfo == None):
        addUserInfo = DBOperations.getUserInfoByNO(memberNOField.get())
        
    #姓名
    if (addUserInfo == None):
        addWindow = Toplevel()
        addWindow.wm_title('确认信息')
        addWindow.geometry('200x100+600+150')
        
        footer = Frame(addWindow)
        footer.pack(side='bottom', fill=X)
        
        printerStr = '姓名：'+ memberNameField.get() \
                     + '\n' + '项目: 添加用户' + '\n' \
                    + '初始金额：' + str(memberAmontField.get()) +'￥'
        printerText = Label(addWindow, 
                            text = printerStr, bg='white').pack(side='top')
        cancelBtn = Button(footer, text='取消', 
                          command=lambda m = addWindow :termiantWindow(m))
        printBtn = Button(footer, text='确定', 
                          command=lambda m = addWindow :confirmAdd(m))
        cancelBtn.pack(side='left', anchor=SW)
        printBtn.pack(side='right', anchor=SE)   
    else:
        dialogView = Dialog(frame, title='提示', text='该用户已经存在', 
                            bitmap=DIALOG_ICON, default=0, strings=('取消','确定')
                            )        
  
    
def confirmAdd(child):
    DBOperations.addOneUser(memberNOField.get(),memberNameField.get()
                            ,memberGender.get(),memberPhoneField.get()
                            ,memberBirthField.get(),memberAmontField.get())
    termiantWindow(child)
    Dialog(frame, title='提示', text='用户添加成功', 
                        bitmap=DIALOG_ICON, default=0, strings=('取消','确定')
                        )    
    

'''用户充值模块'''
depositFrame = Frame(window, borderwidth=4, relief=GROOVE)
depositFrame.pack(side='left',fill=Y)

depositTitle = Label(depositFrame, text='用户充值模块')
depositTitle.grid(column=0, row=0, columnspan=2)

#名字
depositNameField = StringVar()
depositNameLabel = Label(depositFrame, text="姓名")
depositNameEntry = Entry(depositFrame, textvariable=depositNameField)
depositNameLabel.grid(column=0, row=1)
depositNameEntry.grid(column=1, row=1)
#手机号码
depositPhoneField = StringVar()
depositPhoneLabel = Label(depositFrame, text="手机号")
depositPhoneEntry = Entry(depositFrame, textvariable=depositPhoneField)
depositPhoneLabel.grid(column=0, row=2)
depositPhoneEntry.grid(column=1, row=2)
#会员号
depositNumberField = StringVar()
depositNumberLabel = Label(depositFrame, text="会员号")
depositNumberEntry = Entry(depositFrame, textvariable=depositNumberField)
depositNumberLabel.grid(column=0, row=3)
depositNumberEntry.grid(column=1, row=3)

#金额
depositAmountField = DoubleVar()
depositAmountLabel = Label(depositFrame, text='充值')
depositAmountEntry = Entry(depositFrame, textvariable=depositAmountField)
depositAmountLabel.grid(column=0, row=4)
depositAmountEntry.grid(column=1, row=4)

#添加按钮
depositBtn = Button(depositFrame, text='充值', 
                    command=lambda:popConfirmDeposit())
depositBtn.grid(column=1, row=5)

def popConfirmDeposit():
    
    depoistUserInfo = None
    if  (len(depositNameField.get()) > 0):
        depoistUserInfo = DBOperations.getUserInfoByName(depositNameField.get())
    elif (len(depositPhoneField.get()) > 0):
        depoistUserInfo = DBOperations.getUserInfoByMobile(depositPhoneField.get())
    elif (len(depositNumberField.get()) > 0):
        depoistUserInfo = DBOperations.getUserInfoByNO(depositNumberField.get())
    if (depoistUserInfo != None):
        addWindow = Toplevel()
        addWindow.wm_title('确认信息')
        addWindow.geometry('200x100+600+150')
        
        footer = Frame(addWindow)
        footer.pack(side='bottom', fill=X)
    
        #姓名
        printerStr = '姓名：'+ depoistUserInfo.name + '\n' + '项目: 充值' + '\n' \
                      + '总消费金额：' + str(depositAmountField.get()) + '￥' 
        printerText = Label(addWindow, 
                            text = printerStr, bg='white').pack(side='top')
        cancelBtn = Button(footer, text='取消', 
                          command=lambda m = addWindow :termiantWindow(m))
        printBtn = Button(footer, text='确定', 
                          command=lambda m = addWindow :confirmDeposit(m, depoistUserInfo))
        cancelBtn.pack(side='left', anchor=SW)
        printBtn.pack(side='right', anchor=SE) 
    else:
        Dialog(frame, title='提示', text='请补全信息', 
                    bitmap=DIALOG_ICON, default=0, strings=('取消','确定')
               )             
    

def confirmDeposit(child, depositUsrModel):
    tranId = DBOperations.addOneTransaction(depositUsrModel.id, 999, 
                                   0 - depositAmountField.get())
    
    termiantWindow(child)
    
    printerManage = PrinterManage.GetInstance()
    now = int(time.time()) 
    timeArray = time.localtime(now)
    otherStyleTime = time.strftime("%Y/%m/%d", timeArray)  
    
    afterDepositInfo = DBOperations.getUserInfoByNO(depositUsrModel.NO) 


    printerManage.sendToPrinter(tranId,afterDepositInfo.name,afterDepositInfo.NO,
                                depositAmountField.get(),'充值',
                                afterDepositInfo.money,otherStyleTime,0) 
    printerManage.sendToPrinter(tranId,afterDepositInfo.name,afterDepositInfo.NO,
                                depositAmountField.get(),'充值',
                                afterDepositInfo.money,otherStyleTime,1)     
    
    Dialog(frame, title='提示', text='消费信息录入成功', 
                bitmap=DIALOG_ICON, default=0, strings=('取消','确定')
            )



'''如果单纯的打印失败了，此处可以直接打印信息'''
infoPrintFrame = Frame(window, borderwidth=4, relief=GROOVE)
infoPrintFrame.pack(side='left', fill=Y)

infoPrintTitle = Label(infoPrintFrame, text='直接打印小票')
infoPrintTitle.grid(column=0, row=0, columnspan=2)

#name
infoNameField = StringVar()
infoNameLabel = Label(infoPrintFrame, text='姓名')
infoNameEntry = Entry(infoPrintFrame, textvariable=infoNameField)
infoNameLabel.grid(column=0, row=1)
infoNameEntry.grid(column=1, row=1)

#number
infoNumberField = StringVar()
infoNumberLabel = Label(infoPrintFrame, text='会员号')
infoNumberEntry = Entry(infoPrintFrame, textvariable=infoNumberField)
infoNumberLabel.grid(column=0, row=2)
infoNumberEntry.grid(column=1, row=2)

#amount
infoAmountField = DoubleVar()
infoAmountLabel = Label(infoPrintFrame, text='消费额')
infoAmountEntry = Entry(infoPrintFrame, textvariable=infoAmountField)
infoAmountLabel.grid(column=0, row=3)
infoAmountEntry.grid(column=1, row=3)

#program
infoProgramField = StringVar()
infoProgramLabel = Label(infoPrintFrame, text='项目')
infoProgramEntry = Entry(infoPrintFrame, textvariable=infoProgramField)
infoProgramLabel.grid(column=0, row=4)
infoProgramEntry.grid(column=1, row=4)

#remain amount
infoRemainField = DoubleVar()
infoRemainLabel = Label(infoPrintFrame, text='账户余额')
infoRemainEntry = Entry(infoPrintFrame, textvariable=infoRemainField)
infoRemainLabel.grid(column=0, row=5)
infoRemainEntry.grid(column=1, row=5)

infoPrintBtn = Button(infoPrintFrame, text='打印', 
                      command=lambda:printConsumeInfo())
infoPrintBtn.grid(column=1, row=6)

queryAmontBtn = Button(infoPrintFrame, text='查余额',
                       command=lambda:queryAmont())
queryAmontBtn.grid(column=0, row=6)

def queryAmont():
    if  (len(infoNameField.get()) > 0):
        userInfo = DBOperations.getUserInfoByName(infoNameField.get())
        infoRemainField.set(userInfo.money)
        infoNumberField.set(userInfo.NO)
    elif (len(infoNumberField.get()) > 0):
        userInfo = DBOperations.getUserInfoByNO(infoNumberField.get())
        infoRemainField.set(userInfo.money)
        infoNameField.set(userInfo.name)
       

def printConsumeInfo():
    printerManage = PrinterManage.GetInstance()
    now = int(time.time()) 
    timeArray = time.localtime(now)
    otherStyleTime = time.strftime("%Y/%m/%d", timeArray)  
    printerManage.sendToPrinter(999999,infoNameField.get(),infoNumberField.get(),
                                infoAmountField.get(),infoProgramField.get(),
                                infoRemainField.get(),otherStyleTime,0)  
    printerManage.sendToPrinter(999999,infoNameField.get(),infoNumberField.get(),
                                infoAmountField.get(),infoProgramField.get(),
                                infoRemainField.get(),otherStyleTime,1)      

window.mainloop()
