import pandas as pd
import numpy as np
import datetime

data = pd.read_csv("gas.csv")

# slice raw data into last three columns
a = data.loc[:,['localminute','dataid','meter_value']]
s = np.array(a)

# x = {key:[readingX, reading increment, ...], ...} e.g., x = {739:[A,0,0,0,2,2,0,..],...}
x = {}

# set threshold manually set for detecting abnormal readings
threshold = 200

# total malfunction units
count = 0

# the exact date abnormal meter readings occured. e.g., k = {739:[2015-10-1 00:05:10],...}
k = {}

# exact dates zero occured. e.g., zero_dates = {739:[2015-10-1 00:05:10 2015-10-5 10:05:10],...}
zero_dates = {}



# initialize x
for i in range(0,len(s)):
    x[s[i][1]] = []

# for every item in s, make dictionary for every item, then manipulate the dictionary showing as increments.
for i in range(0,len(s)):
    temp = s[i][2]
    if (len(x[s[i][1]]) > 0):
        temp -= (x[s[i][1]][0])
        x[s[i][1]][0] += temp
        # if increments exceeds the threshold, markdown and store in dictionary k.
        if (temp > threshold):
            count += 1
            if s[i][1] not in k.keys():
                k[s[i][1]] = []
                k[s[i][1]].append(s[i][0])
            else:
                k[s[i][1]].append(s[i][0])
    x[s[i][1]].append(temp)
    # solely store dates that zero occurs.
    if s[i][1] not in zero_dates.keys():
        zero_dates[s[i][1]] = []
        zero_dates[s[i][1]].append(s[i][0])
    else:
        zero_dates[s[i][1]].append(s[i][0])

# if want to check abnormal readings, uncomment following.

# for i in k:
#     print(i,": ", k[i])

# start mark for first zero appears.
start_mark = 0

# end mark for last zero appears.
end = 0

# zero appearance flag
start = 1

# duration of zeros in exact dates form.
dates = {}

# duration of zeros in hours form.
dur = {}


# Detect Long time no use
for i in x:
    inner_count = 0
    for j in x[i]:
        if j == 0:
            if start_mark == 0:
                start = zero_dates[i][inner_count]
                end = zero_dates[i][inner_count]
                start_mark = 1
            else:
                end = zero_dates[i][inner_count]
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



for v in dur:
    cc = 0
    for h in dur[v]:
        if h > 18:
            # print("Long time no use happens at ",v," with dur = ", h)
            print(v, ": ", dates[v][cc])
        cc += 1

# if want to check exact date durations, uncomment below

# for v in dates:
#     print(v,": ", dates[v])


# print("With threshold = ", threshold, ", malfunctions in total = ", count)