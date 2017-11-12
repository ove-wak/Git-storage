import csv,os

time = []#时间戳列表
wifi_content = []#wifi列表
time_diff = []#时间差列表
time_diff_add = []#时间差位置列表
filename = "4"
filefolder = "Samsung/"
wifi_mac = []
with open(filefolder+'b'+filename+'/'+filename+'.csv') as f: 
    f_csv = csv.reader(f)
    #headers = next(f_csv) #新数据从第一行开始 
    for row in f_csv:
        time_diff.append(int(row[0]) - 5000)#前后延长五秒
        time_diff.append(int(row[1]) + 5000)

with open(filefolder + filename+'.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    wifi_mac = headers[1:] 
    for row in f_csv:
        if row[0] != '':
            time.append(int(row[0]))
            wifi_content.append(row[1:])

len_time = len(time)
len_time_diff = len(time_diff)
for y in range(len_time_diff):
    for x in range(len_time):
        if time[x] > time_diff[y]:
            time_diff_add.append(x)
            break
    else:
        time_diff_add.append(len_time - 1)

for x in range(len(wifi_content)):
    for y in range(len(wifi_content[0])):
        if wifi_content[x][y] == "":
            wifi_content[x][y] = -95
        else:
            wifi_content[x][y] = int(wifi_content[x][y])

wifi_change = []
time_diff_add_all = [] # 不止存储时间差,而是存储整个时间段
for x in range(0,len(time_diff_add),2):
    if time_diff_add[x] == time_diff_add[x+1]:
        time_diff_add_all.append(-1)
        wifi_change.append(-1)
    else:
        time_diff_add_all.append([])
        wifi_change.append([])
        for y in range(time_diff_add[x],time_diff_add[x+1]):
            time_diff_add_all[int(x/2)].append(time[y])
            wifi_change[int(x/2)].append(wifi_content[y])

#过滤
wifi_change_new = []
for y in range(len(wifi_change)):
    if wifi_change[y] == -1:
        wifi_change_new.append(-1)
    else:
        a = list(map(list, zip(*wifi_change[y]))) # list的矩阵转置
        wifi_change_new.append([])
        for x in range(len(a)):
            if max(a[x]) > -70: # 在整段时间里如果没有大于-70的,则该ap放弃掉
                wifi_change_new[y].append(a[x] + [wifi_mac[x]]) 

# 目录不存在时创建目录
try: 
    os.mkdir(filefolder + 'wifi_'+filename)
except OSError:
    if not os.path.isdir(filefolder + 'wifi_'+filename):
        raise

effect_num = 0 # 有效数字       
for x in range(int(len_time_diff/2)):
    with open(filefolder + 'wifi_'+filename+'/'+str(x)+'_'+str(time_diff[2*x])+'_'+str(time_diff[2*x+1])+'.csv','w', newline='') as f:##如果不加newline,存的文件里每隔一行会多一个空行
        f_csv = csv.writer(f)
        if time_diff_add_all[x] == -1 or wifi_change_new[x] == []:
            f_csv.writerow([-1])
        else:
            effect_num = effect_num + 1
            m = wifi_change_new[x]
            n = time_diff_add_all[x]
            t = []
            for y in range(len(m)):
                t.append(m[y].pop())
            f_csv.writerow([''] + t)#如果直接传入字符串的话,该方法会把每个字符作为单个列表元素来处理
            m = list(map(list, zip(*m)))
            for y in range(len(n)):
                f_csv.writerow([n[y]] + m[y])
print(effect_num)
# 注释:-1表示无法判断;-95的值是对空值的标准化;去除了信号一直微弱(-70为标准)的值;时间前后延长五秒;
