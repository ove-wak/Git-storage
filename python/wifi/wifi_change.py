import csv

time = []#时间戳列表 ##列表初始化
wifi_content = []#wifi列表
time_diff = []#时间差列表
time_diff_add = []#时间差位置列表
filename = "4"
with open('B'+filename+'tampn.csv') as f: ##文件处理,在with内处理不用关闭
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
            wifi_content[x][y] = 100
        else:
            wifi_content[x][y] = int(wifi_content[x][y])

wifi_change = []
for x in range(0,len(time_diff_add),2):
    if time_diff_add[x] == time_diff_add[x+1] or time_diff_add[x+1] == -1:
        wifi_change.append([-1])
    else:
        wifi_change.append(list(map(lambda x: x[0]-x[1], zip(wifi_content[time_diff_add[x]], wifi_content[time_diff_add[x+1]]))))

for y in range(len(wifi_change)):
    temp = 0
    if wifi_change[y] != [-1]:
        wifi_change[y] = list(map(abs, wifi_change[y]))#求列表内所有值的绝对值
        for x in wifi_change[y]:
            if x >= 10:###对于差值大于10的wifi信号权值加1
                temp = temp + 1
        wifi_change[y] = [temp]
print(wifi_change) ##结果为-1的值表示无法判断 
print(len(wifi_change))   

with open('wifi_'+filename+'_new.csv','w', newline='') as f:##如果不加newline,存的文件里每隔一行会多一个空行
    f_csv = csv.writer(f)
    f_csv.writerow(['wifi_change'])#如果直接传入字符串的话,该方法会把每个字符作为单个列表元素来处理
    f_csv.writerows(wifi_change)
    f_csv.writerow(['注释:-1表示无法判断;其他数值为wifi相差大于10的个数的累加值'])
