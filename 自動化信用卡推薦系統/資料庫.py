# -*- coding: utf-8 -*-
"""
Created on Wed May 27 13:36:39 2020

@author: USER
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E5%85%A8%E9%83%A8'
html = urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html, features = 'lxml')
script = soup.find_all('script')
script_list = []

for i in range(0,len(script)):
      script_list.append(script[i].text)
      
script_target = script_list[2]
script_card = script_target.split('"')

card = []
card_idx = []
for i in range (0,len(script_card)):
      if str(script_card[i]) == "productName":
            card.append(script_card[i+2])
            card_idx.append(i)

            

annual_fee = []
for i in range(0,len(script_card)):
      if script_card[i] == '年費':
            for j in range (0,50):
                  if script_card[i-j] == 'displayValue':
                        annual_fee.append(script_card[i-j+2])
                        
cash = []
for i in range(0,len(script_card)):
      if script_card[i] == '國內消費現金回饋':
            for j in range (0,50):
                  if script_card[i-j] == 'displayValue':
                        cash.append(script_card[i-j+2])

limit = []
limit_idx = []
for i in range(0,len(script_card)):
      if script_card[i] == '最低年薪要求':
            limit_idx.append(i)
            for j in range (0,50):
                  if script_card[i+j] == 'value':
                        limit.append(script_card[i+j+2])

for i in range(0,len(limit)):
      if len(limit[i]) == 0:
            for  j in range(0,60):
                  if script_card[limit_idx[i]+j] == 'shortDescription':
                        limit[i] = (str(script_card[limit_idx[i]+j+2]))
                        
for i in range(0,len(limit)):
      b = []
      for k in  range(0,len(annual_fee[i])):
            if annual_fee[i][k].isdigit():
                  b.append(annual_fee[i][k])
      if len(limit[i]) == 0 or limit[i] == '不適用':
            limit[i] = 0
      else:
            a = []
            for j in range (0,len(limit[i])):
                  if limit[i][j].isdigit() or limit[i][j] == '萬' :
                        a.append(limit[i][j])
            
            if '萬' in a:
                  a[a.index('萬')] = '0000'
            limit[i] = ''.join(a)
      annual_fee[i] = ''.join(b)

for i in range(0,len(card)):
      if len(annual_fee[i]) == 0 :
            annual_fee[i] = 0
      if cash[i] == '不適用':
            cash[i] = 0
      annual_fee[i] = int(annual_fee[i])
      cash[i] = 1+float(cash[i])/100
      limit[i] = float(limit[i])

img = []
for i in card_idx:
      for j in range (0,240):
            if "https://images" in script_card[i+j]:
                  img.append(script_card[i+j])


         
url_airline = 'https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E5%93%A9%E7%A8%8B%E5%9B%9E%E9%A5%8B%E5%84%AA%E6%83%A0'
html_airline = urlopen(url_airline).read().decode('utf-8')
soup_airline = BeautifulSoup(html_airline, features = 'lxml')
script_airline = soup_airline.find_all('script')
script_airline_list = []

for i in range(0,len(script_airline)):
      script_airline_list.append(script_airline[i].text)
      
script_airline_target = script_airline_list[2]
script_airline_card = script_airline_target.split('"')
airlinecard = []

for i in range (0,len(script_airline_card)):
      if str(script_airline_card[i]) == "productName":
            airlinecard.append(script_airline_card[i+2])

airline = []
for i in range(0,len(script_airline_card)):
      if script_airline_card[i] == '國內消費累積哩程':
            for j in range (0,50):
                  if script_airline_card[i-j] == 'displayValue':
                        airline.append(script_airline_card[i-j+2])

for i in range (0,len(airlinecard)):
      if airline[i] == '不適用':
            airline[i] = 0
      airline[i] = float(airline[i])
            
url_reward = 'https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E7%B4%85%E5%88%A9%E9%BB%9E%E6%95%B8'
html_reward = urlopen(url_reward).read().decode('utf-8')
soup_reward = BeautifulSoup(html_reward, features = 'lxml')
script_reward = soup_reward.find_all('script')
script_reward_list = []

for i in range(0,len(script_reward)):
      script_reward_list.append(script_reward[i].text)
      
script_reward_target = script_reward_list[2]
script_reward_card = script_reward_target.split('"')
rewardcard = []

for i in range (0,len(script_reward_card)):
      if str(script_reward_card[i]) == "productName":
            rewardcard.append(script_reward_card[i+2])

reward = []
for i in range(0,len(script_reward_card)):
      if script_reward_card[i] == '紅利折抵金':
            for j in range (0,50):
                  if script_reward_card[i-j] == 'displayValue':
                        reward.append(script_reward_card[i-j+2])

for i in range (0,len(rewardcard)):
      if reward[i] == '不適用':
            reward[i] = 0
      reward[i] = float(reward[i])


Card = {}
for i in range(0,len(card)):
      Card[i] = {'card':card[i],'limit': limit[i], 'annual_fee':annual_fee[i],'cash':cash[i],'rate':15,'image':img[i]}
      
idx = []
for i in range(0,len(airlinecard)):
      for j in range(0,len(card)):
            if card[j] == airlinecard[i]:
                  idx.append(j)
                  
                  
for i in range(0,len(airlinecard)):
      for j in range(0,len(card)):
            if card[j] == airlinecard[i]:                
                  Card[j]['airline'] = airline[i]
               
            elif j not in idx :
                  Card[j]['airline'] = 0

idx = []
for i in range(0,len(rewardcard)):
      for j in range(0,len(card)):
            if card[j] == rewardcard[i]:
                  idx.append(j)
                  
                  
for i in range(0,len(rewardcard)):
      for j in range(0,len(card)):
            if card[j] == rewardcard[i]:                
                  Card[j]['reward'] = reward[i]
               
            elif j not in idx :
                  Card[j]['reward'] = 0
import csv
with open('creditcard.csv', 'w', newline='',encoding='utf_8_sig') as f:
      name = ['card','limit','annual_fee','cash','rate','airline','reward','image']
      writer = csv.DictWriter(f,fieldnames = name)
      writer.writeheader()
      for i in range(0,len(card)):
            writer.writerow(Card[i])