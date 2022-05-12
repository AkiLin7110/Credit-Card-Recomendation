# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 13:08:34 2020

@author: Aki z
"""
"""
專題
先想好策略,再透過歷史資料,看看是否得益
透過RSI指標去尋找買進賣出的點
交易策略:
 當短周期超過長週期時買進;
 IRS6>80賣出"""

 
from Methodology import *
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as md
from datetime import datetime
import datetime
from pylab import figure,show

ticker=2330
start='2019-03-30'
end='2020-03-09'

getpricedata(ticker,start,end)

#讀取檔案
data=pd.read_csv(str(ticker)+'.csv')

#把每一日的價-前一日的價
a=1
data['Ut']=Ut(a,data)#注意新增欄位size要相符
data['Dt']=Dt(a,data)

#UPt.DNt
for a in [6,12,24]:
    data['UPt'+str(a)]=UPt(a,data)
    data['DNt'+str(a)]=DNt(a,data)
    data['RSI'+str(a)]=RSI(a,data['UPt'+str(a)],data['DNt'+str(a)])
#畫圖(分析資料)
plt.figure(figsize=(20,10))
plt.style.use('ggplot')
#data.index=list(data['Date'])#將index改為日期

#設圖表x軸--時間
date=[]
for i in range(0,len(data)):
    s=data['Date'][i]
    y=int(s[0:4])
    m=int(s[5:7])
    d=int(s[8:10])
    dt=datetime.datetime(int(y),int(m),int(d))
    date.append(md.date2num(dt))
x=date   
#print(x)
#圖名,軸名
plt.title(str(ticker)+'   RSI Analysis')
plt.xlabel('Date')
plt.ylabel('RSI')
#x=[datetime.strptime(d, '%Y-%m-%d').date() for d in data['Date']]
y0=data['RSI6'].tolist()#.astype('str')
y1=data['RSI12'].tolist()#.astype('str')
y2=data['RSI24'].tolist()#.astype('str')
#畫圖
#print(type(y0))
#print(y0)


plt.plot(x[6:],y0[6:],label='RSI6')
plt.plot(x[12:],y1[12:],label='RSI12')
plt.plot(x[24:],y2[24:],label='RSI24')

plt.gca().xaxis.set_major_formatter(md.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(md.DayLocator())
plt.gcf().autofmt_xdate()
plt.legend(loc = "best", fontsize=20)
#y_sticks=np.arange(0,100,1)
#plt.yticks(y_sticks)
plt.show()

#長期:
#策略:當短周期超過長週期時買進
buy=[]
sell=[]
for i in range(0,len(data)-1):
    if data['RSI6'][i]==' ' or data['RSI12'][i]==' ' or data['RSI24'][i]==' ':
        #print(i)
        continue
    elif ((data['RSI6'][i]>=data['RSI12'][i]) and (data['RSI12'][i]>=data['RSI24'][i])) or \
        data['RSI6'][i]<=20:
            #print(i)
            temp=data['Open'][i+1]
            buy.append(temp)
    if data['RSI6'][i]==' ':
        #print(i)
        continue
    elif ((data['RSI6'][i]<=data['RSI12'][i]) and (data['RSI12'][i]<=data['RSI24'][i])) or \
        data['RSI6'][i]>=80:
        temp=data['Open'][i+1]
        sell.append(temp)
print('平均買進價: ',sum(buy)/len(buy))
print('平均賣出價: ',sum(sell)/len(sell))
if sum(buy)/len(buy) > sum(sell)/len(sell):
    print('長期:我很棒')
else:
    print('長期:我就爛') 
#短期
Buy=0
buy=[]
sell=[]
for i in range(0,len(data)-1):
    if data['RSI6'][i]==' ' or data['RSI12'][i]==' ' or data['RSI24'][i]==' ':
        #print(i)
        continue
    elif ((data['RSI6'][i]>=data['RSI12'][i]) and (data['RSI12'][i]>=data['RSI24'][i])) or \
        data['RSI6'][i]<=20:
            #print(i)
            temp=data['Open'][i+1]
            buy.append(temp)
            for j in range(i,len(data)):
                if data['RSI6'][i]==' ':
                    #print(i)
                    continue
                elif ((data['RSI6'][i]<=data['RSI12'][i]) and (data['RSI12'][i]<=data['RSI24'][i])) or \
                    data['RSI6'][i]>=80:
                    temp=data['Open'][i+1]
                    sell.append(temp)
                    break
                  

