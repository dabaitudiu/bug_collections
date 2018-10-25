import pandas as pd
import numpy as np
import datetime
import heapq

data = pd.read_csv("gas.csv")
# print(data)
a = data.loc[:,['localminute','dataid','meter_value']]
s = np.array(a)
# print(a)
x = {}
y = {}

ref = datetime.datetime.strptime('00:00:00', '%H:%M:%S')
p = 2
# interval: 0 - 4, 4 - 8, 8 - 12, 12 - 16, 16 - 20, 20 - 24

for i in range(0,len(s)):
    x[s[i][1]] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    y[s[i][1]] = []

count = 0

for i in range(0,len(s)):
    temp = s[i][2]
    if (len(y[s[i][1]]) > 0):
        temp -= (y[s[i][1]][0])
        y[s[i][1]][0] += temp
        if temp != 0:
            dif_delta = datetime.datetime.strptime(s[i][0][11:19], '%H:%M:%S') - ref
            dif = int((dif_delta.seconds / 3600))
            x[s[i][1]][dif] += 1
            # if count < 20:
            #     if (s[i][1] == 739):
            #         print(s[i][0], "   ", dif)
            #         print(x[s[i][1]])
            #         count += 1
    y[s[i][1]].append(temp)

sum = {}
g = x

X_cor = []
first_min_index = []
first_min_neighbours = []

for j in x:
    sum[j] = []
    X_cor.append(j)
    for k in x:
        sum[j].append(round((np.sqrt(np.sum(np.power((np.array(x[k]) - np.array(x[j])), 2)) / 24)), 2))

for e in sum:
    first_min_index = []
    first_min_neighbours = []
    first_mins = heapq.nsmallest(6, sum[e])
    for i in first_mins:
        first_min_index.append(sum[e].index(i))
        first_min_neighbours.append(X_cor[sum[e].index(i)])
    print(e, ": ", first_min_neighbours[1:])

# uu = np.array(x[739]) - np.array(x[6910])
# print(np.sum(uu))
# print(round((np.sqrt(sum(np.power((np.array(x[739]) - np.array(x[739])),2)) / 24)),2))

