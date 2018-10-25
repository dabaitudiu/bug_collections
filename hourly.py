import pandas as pd
import numpy as np
import datetime
import heapq
import matplotlib.pyplot as plt

data = pd.read_csv("gas.csv")
# print(data)
a = data.loc[:26450,['localminute','dataid','meter_value']]
s = np.array(a)
# print(a)
x = {}
y = {}

ref = datetime.datetime.strptime('00:00:00', '%H:%M:%S')
p = 2
# interval: 0 - 4, 4 - 8, 8 - 12, 12 - 16, 16 - 20, 20 - 24

for i in range(0,len(s)):
    y[s[i][1]] = []

rr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
rx = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

for i in range(0,len(s)):
    temp = s[i][2]
    if (len(y[s[i][1]]) > 0):
        temp -= (y[s[i][1]][0])
        y[s[i][1]][0] += temp
        if temp != 0:
            dif_delta = datetime.datetime.strptime(s[i][0][11:19], '%H:%M:%S') - ref
            dif = int((dif_delta.seconds / 3600))
            rr[dif] += temp
    y[s[i][1]].append(temp)

print(rr)
plt.bar(rx,rr,facecolor='#9999ff', edgecolor='white')
plt.show()