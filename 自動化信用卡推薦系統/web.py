# -*- coding: utf-8 -*-
"""
Created on Sun May 24 13:51:34 2020

@author: robecca
"""
from flask import render_template,redirect,url_for
from flask import Flask
from flask import Flask,request
import csv
import pandas as pd

data=pd.read_csv('creditcard.csv')
app = Flask(__name__)

@app.route('/iwantcard',methods = ['GET','POST'])
def card():
      if request.method == 'POST': 
            global new_limit
            global air_choose
            global bonus_choose
            global target
            global spending
            income = request.values['income']
            air_choose = request.form.get('air_choose')
            bonus_choose = request.form.get('bonus_choose')
            spending = int(request.values['spending'])
            new_limit=[]
            for i in range(0,len(data['limit'])):
                if int(data['limit'][i]) <= int(income):
                    new_limit.append(i)
                    
            if air_choose=='是':
                new_limit_1=[]#在跑的目標
                for i in new_limit:
                    if data['airline'][i] != 0  :
                        new_limit_1.append(i)
            
            if bonus_choose=='是':
                if air_choose=='是':
                    new_limit_2=[]#在跑的目標
                    for i in new_limit_1:
                        if  data['reward'][i] != 0:
                            new_limit_2.append(i)
                else:
                    new_limit_2=[]#在跑的目標
                    for i in new_limit:
                        if  data['reward'][i] != 0:
                            new_limit_2.append(i)
                            
            target=new_limit
            if air_choose =='是':
                target=new_limit_1
            if bonus_choose=='是':
                target=new_limit_2  
            if len(target) == 0:
                  return render_template('card2.html')
                      
            return redirect(url_for('p'))       
      return render_template('card.html')

@app.route('/p',methods = ['GET','POST'])
def p():
      global new_limit
      global air_choose
      global bonus_choose
      global target
      global spending

      sum_p = 0
      compare=[]
      if air_choose == '是':
            if bonus_choose == '是':
                  if request.method == 'POST':
                        cash_p = int(request.values['cash_p'])
                        airline_p = int(request.values['airline_p'])
                        reward_p = int(request.values['reward_p'])
                        sum_p = cash_p + airline_p + reward_p   
                        if not sum_p == 100:
                              return redirect(url_for('p'))                        
                        
                        for i in target:
                              tmp=spending*(data['cash'][i]*cash_p+(data['airline'][i]*airline_p)+(data['reward'][i]*reward_p))-data['annual_fee'][i]
                              compare.append(tmp)
                        ans_index=target[ compare.index(max(compare))]
                        return render_template('finalcard.html',card =data['card'][ans_index], limit =data['limit'][ans_index],annual = data['annual_fee'][ans_index], cash = data['cash'][ans_index],air = data['airline'][ans_index],bonus = data['reward'][ans_index],image = data['image'][ans_index] )
                  return render_template('p_all.html')
            else:
                  if request.method == 'POST':
                        cash_p = int(request.values['cash_p'])
                        airline_p = int(request.values['airline_p'])
                        sum_p = cash_p + airline_p
                        if not sum_p == 100:
                              return redirect(url_for('p'))
                        
                        for i in target:
                              tmp=spending*(data['cash'][i]*cash_p+(data['airline'][i]*airline_p))-data['annual_fee'][i]
                              compare.append(tmp)
                        ans_index=target[ compare.index(max(compare))]
                        return render_template('finalcard.html',card =data['card'][ans_index], limit =data['limit'][ans_index],annual = data['annual_fee'][ans_index], cash = data['cash'][ans_index],air = data['airline'][ans_index],bonus = data['reward'][ans_index],image = data['image'][ans_index] )
                  return render_template('p_c+a.html')
      else:
            if bonus_choose == '是':
                  if request.method == 'POST':
                        cash_p = int(request.values['cash_p'])
                        reward_p = int(request.values['reward_p'])
                        sum_p = cash_p + reward_p
                        if not sum_p == 100:
                              return redirect(url_for('p'))
                        
                        for i in target:
                              tmp=spending*(data['cash'][i]*cash_p+(data['reward'][i]*reward_p))-data['annual_fee'][i]
                              compare.append(tmp)
                        ans_index=target[ compare.index(max(compare))]
                        return render_template('finalcard.html',card =data['card'][ans_index], limit =data['limit'][ans_index],annual = data['annual_fee'][ans_index], cash = data['cash'][ans_index],air = data['airline'][ans_index],bonus = data['reward'][ans_index],image = data['image'][ans_index] )
                  return render_template('p_c+b.html')
            else:
                  if request.method == 'POST':
                        cash_p = int(request.values['cash_p'])
                        sum_p = cash_p
                        if not sum_p == 100:
                              return redirect(url_for('p'))
                        
                        for i in target:
                              tmp=spending*data['cash'][i]*cash_p-data['annual_fee'][i]
                              compare.append(tmp)
                              
                        ans_index=target[ compare.index(max(compare))]
                        return render_template('finalcard.html',card =data['card'][ans_index], limit =data['limit'][ans_index],annual = data['annual_fee'][ans_index], cash = data['cash'][ans_index],air = data['airline'][ans_index],bonus = data['reward'][ans_index],image = data['image'][ans_index] )
      
                  return render_template('p_c.html')
            
if __name__ == '__main__':
      app.run()
