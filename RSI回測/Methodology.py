# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 00:07:56 2020

@author: Aki
"""

import pandas as pd
import urllib.request
import time
#爬股價
def getpricedata(ticker,start,end):
    start=time.strptime(start,"%Y-%m-%d")
    start=int(time.mktime(start))
    end=time.strptime(end,"%Y-%m-%d")
    end=int(time.mktime(end))+86400
    url="https://query1.finance.yahoo.com/v7/finance/download/"+str(ticker)+".TW?period1="+str(start)+"&period2="+str(end)+"&interval=1d&events=history"
    urllib.request.urlretrieve(url,str(ticker)+'.csv')
#找UP(絕對漲幅)&DOWN(絕對跌幅)
def Ut(a,data):
    up=[]
    for i in range(0,a):
        up.append(' ')
    for i in range(a,len(data)):
        temp=data['Close'][i]-data['Close'][i-1]
        if temp<0:
            temp=0
        up.append(temp)
    #data['UP']=up
    return up

def Dt(a,data):
    down=[]
    for i in range(0,a):
        down.append(' ')
    for i in range(a,len(data)):
        temp=data['Close'][i]-data['Close'][i-1]
        if temp>0:
            temp=0
        temp*=(-1)
        down.append(temp)
    return down
#對漲幅跌幅取平滑
def UPt(a,data):
    UPt=[]
    for i in range(0,len(data)):  
        if i<a:
            temp=' '
        elif i==a:
            temp=sum(data['Ut'][1:a+1])/a#1~6取值
        else:#( 1 – 1/N) UP t-1 + 1/N Ut
            temp=(1-1/a)*temp+(1/a)*data['Ut'][i]
        UPt.append(temp)
    return UPt
    #print('UPt=')
    #print(UPt)
def DNt(a,data):
    DNt=[]
    for i in range(0,len(data)):  
        if i<a:
            temp=' '
        elif i==a:
            temp=sum(data['Dt'][1:a+1])/a#1~6取值
        else:#( 1 – 1/N) UP t-1 + 1/N Ut
            temp=(1-1/a)*temp+(1/a)*data['Dt'][i]
        DNt.append(temp)
    return DNt

#取得RSI=100 * UP / (DN+UP)
def RSI(a,up,down):
    RSI=[]
    for i in range(0,len(up)):
        if i<a:
            temp=' '
        else:
            temp=100*up[i]/(up[i]+down[i])    
        RSI.append(temp)
    return RSI
            
        
    

  