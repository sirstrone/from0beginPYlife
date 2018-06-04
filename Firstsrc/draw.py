#
# FileName: draw.py
# Author: zou
# Version: 1.0
# Date: 2018/6/1
# Description: 数据处理和绘图
#

import xlrd
import pandas as pd
import numpy as np
from scipy import  stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']


# 声明在绘图中使用的变量
x_data = []
y_data = []
x1=[]
y1=[]
x2=[]
y2=[]
x3=[]
y3=[]

#打开excle文件
wb = xlrd.open_workbook(r'C:\Users\god.zou\Desktop\Problem_B\2.xlsx')
try:
    sh = wb.sheet_by_name("Sheet1")#声明表名Sheet1
except:
    print("error")

#双重循环提取表中数据
for row in range(1,sh.nrows):
    values = []
    for col in range(2,sh.ncols):
        if(col==2 or col ==6):
            values.append(sh.cell(row, col).value)
    print(values)
    #这里使用了if提取表中特定字符串的数据
    #其实我再想为什么不批量添加到list在绘图时再来提取呢？
    if (row>0 and row <=50) :
        x_data.append(values[0])
        y_data.append(values[1])

    elif(row>50 and row <=100):
        x1.append(values[0])
        y1.append(values[1])

    elif(row>100 and row <=150):
        x2.append(values[0])
        y2.append(values[1])

    elif(row>150 and row <=200):
        x3.append(values[0])
        y3.append(values[1])

#此处为绘图
# 注释可以还可以酱紫写
# label = ["B市", "C市"]
plt.plot(x_data, y_data,label=u"油气消耗量",linewidth=1)
plt.plot(x1,y1,"c--",label=u"煤炭消耗量",linewidth=1 )
plt.plot(x2,y2,':',label=u"可再生能源消耗量",linewidth=1)
plt.plot(x3,y3,'m-.',label=u"能源生产总量",linewidth=1)
plt.title(u"D市能源使用情况分析")#标题
plt.legend()#记得要调用legend方法注释才能正常显示哟
#横轴坐标？
plt.xlabel(u"年份")
plt.ylabel(u"消耗量（千焦）")
#plt.savefig(r'C:\Users\god.zou\Desktop\Problem_B\4.png')

plt.show()


