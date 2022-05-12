# -*- coding: utf-8 -*-
"""
Created on Tue May 12 15:33:02 2020

@author: USER
"""


import pickle
class account():
    balance=0
    def __init__(self,name):
        self.name=name
    def balance_(self,amount,ty):
        #print("initial",self.balance)
        if ty==0:   
            self.balance+=amount
            #print(self.balance)
        elif ty==1:
            self.balance-=amount
        return self.balance
    def printbalance(self):
        print(self.balance)
    def phone(self,number):
        self.number=number
        
    

selected=input("(a)新增客戶資料，(b) 新增消費紀錄，(c) 確認信用卡剩餘: (d)修改客戶資料 (e)印出客戶電話號碼 ")
customer_name=input("請輸入姓名: ")
filename = customer_name + ".pkl"
if selected=="a":
    customer=account(str(customer_name))
    number=input("請輸入連絡電話: ")
    amount=int(input("請輸入信用額度: "))
    customer.phone(number)
    customer.balance_(amount,0)
    with open(filename,'wb') as l:
        pickle.dump(customer, l)#存檔的標準格式
elif selected=="b":
    amount=int(input("請輸入新增消費金額: "))
    with open(filename,'rb') as l:
        customer=pickle.load(l)#讀黨的儲存格式
    #print(customer.balance)
    if customer.balance>=amount:
        customer.balance_(amount,1) 
    else:
        print("無法新增消費,已超過信用額度")
    with open(filename,'wb') as l:
        pickle.dump(customer,l)
elif selected=="c":
    with open(filename,'rb') as l:
        customer=pickle.load(l)
    customer.printbalance()
elif selected=="d":
    try:
        with open(filename,'rb') as l:
            customer=pickle.load(l)
        number=input("請輸入連絡電話: ")
        customer.phone(number)
        with open(filename,'wb') as l:
            pickle.dump(customer, l)#存檔的標準格式      
    except:
        print('查無用戶資料__請新增用戶')
        customer=account(str(customer_name))
        number=input("請輸入連絡電話: ")
        amount=int(input("請輸入信用額度: "))
        customer.phone(number)
        customer.balance_(amount,0)
        with open(filename,'wb') as l:
            pickle.dump(customer, l)#存檔的標準格式
elif selected=='e':
    with open(filename,'rb') as l:
        customer=pickle.load(l)
    print(customer.number)

        