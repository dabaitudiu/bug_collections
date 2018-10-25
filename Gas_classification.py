import pandas as pd
import numpy as np
import datetime

data = pd.read_csv("gas.csv")
# print(data)
a = data.loc[:,['localminute','dataid','meter_value']]
s = np.array(a)
# print(a)
x = {}

threshold = 200
count = 0
k = {}
zerok = 0
duration = {}

for i in range(0,len(s)):
    x[s[i][1]] = []

for i in range(0,len(s)):
    temp = s[i][2]
    if (len(x[s[i][1]]) > 0):
        temp -= (x[s[i][1]][0])
        x[s[i][1]][0] += temp
        if (temp > threshold):
            count += 1
            if s[i][1] not in k.keys():
                k[s[i][1]] = []
                k[s[i][1]].append(s[i][0])
            else:
                k[s[i][1]].append(s[i][0])
        # if (temp == 0):
        #     # dif = s[i][0] - zerok
        #     if s[i][1] not in duration.keys():
        #         duration[s[i][1]] = []
        #         duration[s[i][1]].append(s[i][0])
        #     else:
        #         duration[s[i][1]].append(s[i][0])
    x[s[i][1]].append(temp)
    if s[i][1] not in duration.keys():
        duration[s[i][1]] = []
        duration[s[i][1]].append(s[i][0])
    else:
        duration[s[i][1]].append(s[i][0])


start_mark = 0
start = 1
end = 0
dates = {}
dur = {}

bb = 0


# Detect Long time no use


for i in x:
    inner_count = 0
    for j in x[i]:
        if j == 0:
            if start_mark == 0:
                start = duration[i][inner_count]
                end = duration[i][inner_count]
                start_mark = 1
            else:
                end = duration[i][inner_count]
        else:
            if start_mark == 1:
                tmp_start = datetime.datetime.strptime(start[:19], '%Y-%m-%d %H:%M:%S')
                tmp_end = datetime.datetime.strptime(end[:19], '%Y-%m-%d %H:%M:%S')
                if i not in dates.keys():
                    dates[i] = []
                    dur[i] = []
                    dates[i].append([start, end])
                    dur[i].append(round((tmp_end - tmp_start).seconds / 3600.0, 2))
                else:
                    dates[i].append([start, end])
                    dur[i].append(round((tmp_end - tmp_start).seconds / 3600.0, 2))

            start_mark = 0
        inner_count += 1


# print(x[3635])
# print(dates[3635])

print(dur[3635])

# cc = 0
for v in dur:
    for h in dur[v]:
        if h > 18:
            print("Long time no use happens at ",v," with dur = ", h)

# for v in duration:
#     print(v,": ", duration[v])

#


print("With threshold = ", threshold, ", malfunctions in total = ", count)