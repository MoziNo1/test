"http://www.weather.com.cn/weather1d/101060101.shtml"
import requests
import json

li_num1=[4,5,2,7]
li_num2=[3, 6]
lim = []
for i in li_num1:
    lim.append(i)
for j in li_num2:
    lim.append(j)
lim.sort(reverse=True)
print(lim)
tu_num1=('p','y','t',['o','n'])
list1 = tu_num1[-1]
list1.append('h')
print(tu_num1[-1])

syr = 'skdaskerkjsalkj'
count = 0
for i in syr:
