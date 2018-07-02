#-*- coding: utf-8 -*-
#    writing 2018/6/1
#    Author:zou
#    ARMA 预测.py

import xlrd
import pandas as pd
import numpy as np
from scipy import  stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot
from pylab import mpl
#mpl.rcParams['font.sans-serif'] = ['SimHei']

#声明需要的变量和需要预处理的excle数据
x=[]
dta=[]
wb = xlrd.open_workbook(r'C:\Users\god.zou\Desktop\Problem_B\41.xlsx')
try:
    sh = wb.sheet_by_name("Sheet1")

except:
    print("error")

nrow = sh.nrows
ncols = sh.ncols

#遍历数据
for row in range(1,nrow):
    values = []
    for col in range(2,ncols):
        if(col==2 or col ==6):
            values.append(sh.cell(row, col).value)
   # print(values)
    #read data
    if (row>0 and row <=50) :
        x.append(values[0])
        dta.append(values[1])
#将这些数据以numpy的形式存储至dta（list）中 并进行浮点数化
dta=np.array(dta,dtype=np.float)

dta=pd.Series(dta)
#plt.plot(x, dta,label=u"油气消耗量",linewidth=1)
dta.index = pd.Index(sm.tsa.datetools.dates_from_range('1960','2009'))
#dta.plot(figsize=(12,8))
# fig = plt.figure(figsize=(12,8))
# ax1= fig.add_subplot(111)
# diff1 = dta.diff(10)
# diff1.plot(ax=ax1)
#
# fig = plt.figure(figsize=(12,8))
# ax2= fig.add_subplot(111)
# diff2 = dta.diff(2)
# diff2.plot(ax=ax2)
# plt.title(u"一阶差分时序模型")
#
#ARMA模型确立
diff1= dta.diff(1)
fig = plt.figure(figsize=(12,8))
ax1=fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(dta,lags=40,ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(dta,lags=40,ax=ax2)


arma_mod70 = sm.tsa.ARMA(dta,(7,0)).fit()
# print(arma_mod70.aic,arma_mod70.bic,arma_mod70.hqic)
# arma_mod30 = sm.tsa.ARMA(dta,(0,1)).fit()
# print(arma_mod30.aic,arma_mod30.bic,arma_mod30.hqic)
# arma_mod71 = sm.tsa.ARMA(dta,(7,1)).fit()
# print(arma_mod71.aic,arma_mod71.bic,arma_mod71.hqic)
# arma_mod80 = sm.tsa.ARMA(dta,(8,0)).fit()
# print(arma_mod80.aic,arma_mod80.bic,arma_mod80.hqic)

# resid = arma_mod70.resid#残差
# fig = plt.figure(figsize=(12,8))
# ax = fig.add_subplot(111)
# fig = qqplot(resid, line='q', ax=ax, fit=True)

#绘图
predict_sunspots = arma_mod70.predict('2008', '2050', dynamic=True)
#predict_sunspots = arma_mod80.predict('1970', '2020', dynamic=True)
print(predict_sunspots)
fig, ax = plt.subplots(figsize=(12, 8))
ax = dta.ix['1960':].plot(ax=ax)
predict_sunspots.plot(ax=ax)

plt.show()
