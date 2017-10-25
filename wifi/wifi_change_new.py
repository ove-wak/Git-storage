import csv

time = []#时间戳列表
wifi_content = []#wifi列表
time_diff = []#时间差列表
time_diff_add = []#时间差位置列表
filename = "2"
with open('B'+filename+'tampn.csv') as f: 
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        time_diff.append(int(row[0]))
        time_diff.append(int(row[1]))

with open(filename+'.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        if row[0] != '':
            time.append(int(row[0]))
        else:
            time.append(-1)
        wifi_content.append(row[1:])

diff = 0
len_time = len(time)
len_time_diff = len(time_diff)
for x in range(len_time):
        while diff < len_time_diff and time[x] > time_diff[diff]:
                time_diff_add.append(x)
                diff = diff + 1
while len(time_diff_add) < len_time_diff:
    time_diff_add.append(-1)

for x in range(len(wifi_content)):
    for y in range(len(wifi_content[0])):
        if wifi_content[x][y] == "":
            wifi_content[x][y] = -95
        else:
            wifi_content[x][y] = int(wifi_content[x][y])

wifi_change = []
for x in range(0,len(time_diff_add),2):
    if time_diff_add[x+1] == -1 or time_diff_add[x+1] == 0:
        wifi_change.append(-1)
        wifi_change.append(-1)
    elif time_diff_add[x] == time_diff_add[x+1]:
        wifi_change.append(wifi_content[time_diff_add[x] - 1])
        wifi_change.append(wifi_content[time_diff_add[x+1]])
    else:
        wifi_change.append(wifi_content[time_diff_add[x]])
        wifi_change.append(wifi_content[time_diff_add[x+1]])
wifi_change_new = []
for y in range(0,len(wifi_change),2):
    temp = 0
    if wifi_change[y] == -1:
        wifi_change_new.append(-1)
    else:
        wifi_change_new.append([])
        for x in range(len(wifi_change[y])):
            if abs(wifi_change[y][x] - wifi_change[y+1][x]) > 5:
                if wifi_change[y][x] > -80 or wifi_change[y+1][x] > -80:
                    wifi_change_new[int(y/2)].append([wifi_change[y][x],wifi_change[y+1][x]])
  
wifi_change_new_sort = []
for x in wifi_change_new:
    if x == -1:
        wifi_change_new_sort.append(-1)
        wifi_change_new_sort.append(-1) 
    else:
        wifi_change_new_sort.append([])
        wifi_change_new_sort.append([])
        x.sort(reverse=True)
        for y in x:
            wifi_change_new_sort[len(wifi_change_new_sort)-2].append(y[0])
            wifi_change_new_sort[len(wifi_change_new_sort)-1].append(y[1])
print(wifi_change_new_sort)

with open('wifi_'+filename+'_new_content.csv','w', newline='') as f:##如果不加newline,存的文件里每隔一行会多一个空行
    f_csv = csv.writer(f)
    f_csv.writerow([['time'],['wifi_change']])#如果直接传入字符串的话,该方法会把每个字符作为单个列表元素来处理
    for x in range(len(time_diff)):
        if wifi_change_new_sort[x] == -1:
            f_csv.writerow([str(time_diff[x])] + [str(wifi_change_new_sort[x])])
        else:
            f_csv.writerow([str(time_diff[x])] + wifi_change_new_sort[x])
        if x%2 == 1:
            f_csv.writerow('\n')
    f_csv.writerow(['注释:-1表示无法判断;-95的值是对空值的标准化;每两行为一组数据,同一组内去除了相差不大于5的值,去除了信号一直微弱的值,并对剩下的值排序'])
