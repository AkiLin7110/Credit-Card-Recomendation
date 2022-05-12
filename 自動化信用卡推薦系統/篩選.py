# -*- coding: utf-8 -*-
"""
Created on Fri May 29 19:55:37 2020

@author: USER
"""
import csv
import pandas as pd
#from 張爬資料_全部 import*

#使用者操作:輸入年薪->#用年薪去篩->要/不要 里程 -> 要/不要 紅利

data=pd.read_csv('creditcard.csv')
#處理資料


   
income=int(input('請輸入年薪：'))

new_limit=[]#在跑的目標
for i in range(0,len(data['limit'])):
    (data['limit'][i])=str(data['limit'][i]) 
    if int(data['limit'][i]) <= income:
        new_limit.append(i)

air_choose=input('追求里程回饋嗎? 是/否：')
if air_choose=='是':
    new_limit_1=[]#在跑的目標
    for i in new_limit:
        if data['airline'][i] != '0'  :
            new_limit_1.append(i)
#處理資料
for i in range(0,len(data['airline'])):    
    if data['airline'][i] == '0' :
        data['airline'][i]=0       
    else:
        data['airline'][i]=float(data['airline'][i])
bonus_choose=input('追求紅利回饋嗎? 是/否：')
if bonus_choose=='是':
    if air_choose=='是':
        new_limit_2=[]#在跑的目標
        for i in new_limit_1:
            if data['reward'][i] != '0':
                new_limit_2.append(i)
    else:
        new_limit_2=[]#在跑的目標
        for i in new_limit:
            if data['reward'][i] != '0':
                new_limit_2.append(i)

        
#選比較項目                
target=new_limit
if air_choose =='是':
    target=new_limit_1
if bonus_choose=='是':
    target=new_limit_2

#比重
spending=int(input('請輸入每月花費：'))
print('請輸入花費比重：(total:100)')
while(1):
    sum_p=0
    cash_p=int(input('現金回饋：'))
    sum_p+=cash_p
    if air_choose =='是':
        airline_p=int(input('里程回饋：'))
        sum_p+=airline_p
    if bonus_choose=='是':
        reward_p=int(input('紅利回饋：'))
        sum_p+=reward_p
    if sum_p==100:
        break
    else:
        print('輸入比重錯誤，請重新輸入～')

#找出最讚 : Formula=spending*cash*cash_p+(airline*airline_p)+(reward*reward_p)
choose=[]
choose.append(air_choose)
choose.append(bonus_choose)

compare=[]
for i in target:
    tmp=spending*data['cash'][i]*cash_p#否否
    if choose[0]=='是':
        tmp=spending*(data['cash'][i]*cash_p+(data['airline'][i]*airline_p))#是否
        if choose[1]=='是':
            tmp=spending*(data['cash'][i]*cash_p+(data['airline'][i]*airline_p)+(data['reward'][i]*reward_p))#是是
    elif choose[1]=='是':
        tmp=spending*(data['cash'][i]*cash_p+(data['reward'][i]*reward_p))#否是
    compare.append(tmp)
ans_index= compare.index(max(compare))
print('此為您的命定卡片： %s ' % data['card'][ans_index])
print('年收限制：%s' % data['limit'][ans_index])
print('年費：%s' %data['annual_fee'][ans_index])
print('國內現金回饋：%s' %data['cash'][ans_index]+'%')
print('國內消費里程 ：%s' %data['airline'][ans_index])
print('紅利回饋：%s' %data['reward'][ans_index])
print("""
      此為您的命定卡片： %s
      
      以下為其相關資訊～
      
      年收限制：%s
      年費：%s
      國內現金回饋：%s%% 
      國內消費里程 ：%s
      紅利回饋：%s
      """ %(data['card'][ans_index],data['limit'][ans_index],data['annual_fee'][ans_index],data['cash'][ans_index],data['airline'][ans_index],data['reward'][ans_index])
      )
                                


    


 




