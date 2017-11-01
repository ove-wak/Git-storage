import csv

filename = "1"
Samsung_wifi = []
LG_wifi = []
Oneplus_wifi = []
Nexus_wifi = []

with open('Samsung/wifi_' + filename+'.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        Samsung_wifi.append(row[1:])

with open('LG/wifi_' + filename+'.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        LG_wifi.append(row[1:])

with open('Oneplus/wifi_' + filename+'.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        Oneplus_wifi.append(row[1:])

with open('Nexus/wifi_' + filename+'.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        Nexus_wifi.append(row[1:])
wifi_all = []
for x in range(int(len(Samsung_wifi)/3)):
    wifi_all.append([])
    wifi_mac = []
    for y in range(len(Samsung_wifi[3*x])):
        wifi_all[x].append([Samsung_wifi[3*x][y],Samsung_wifi[3*x+1][y],Samsung_wifi[3*x+2][y]])
        wifi_mac.append(Samsung_wifi[3*x][y])
    for y in range(len(LG_wifi[3*x])):
        if LG_wifi[3*x][y] in wifi_mac:
            indexx = wifi_mac.index(LG_wifi[3*x][y])
            wifi_all[x][indexx].append(LG_wifi[3*x+1][y])
            wifi_all[x][indexx].append(LG_wifi[3*x+2][y])
        else:
            wifi_mac.append(LG_wifi[3*x][y])
            wifi_all[x].append([LG_wifi[3*x][y],'','',LG_wifi[3*x+1][y],LG_wifi[3*x+2][y]])
    for y in range(len(Oneplus_wifi[3*x])):
        if Oneplus_wifi[3*x][y] in wifi_mac:
            indexx = wifi_mac.index(Oneplus_wifi[3*x][y])
            wifi_all[x][indexx].append(Oneplus_wifi[3*x+1][y])
            wifi_all[x][indexx].append(Oneplus_wifi[3*x+2][y])
        else:
            wifi_mac.append(Oneplus_wifi[3*x][y])
            wifi_all[x].append([Oneplus_wifi[3*x][y],'','','','',Oneplus_wifi[3*x+1][y],Oneplus_wifi[3*x+2][y]])
    for y in range(len(Nexus_wifi[3*x])):
        if Nexus_wifi[3*x][y] in wifi_mac:
            indexx = wifi_mac.index(Nexus_wifi[3*x][y])
            wifi_all[x][indexx].append(Nexus_wifi[3*x+1][y])
            wifi_all[x][indexx].append(Nexus_wifi[3*x+2][y])
        else:
            wifi_mac.append(Nexus_wifi[3*x][y])
            wifi_all[x].append([Nexus_wifi[3*x][y],'','','','','','',Nexus_wifi[3*x+1][y],Nexus_wifi[3*x+2][y]])

with open('wifi_all_'+filename+'.csv','w', newline='') as f:##如果不加newline,存的文件里每隔一行会多一个空行
    f_csv = csv.writer(f)
    f_csv.writerow([['time'],['wifi_change']])#如果直接传入字符串的话,该方法会把每个字符作为单个列表元素来处理
    num = 1
    for x in wifi_all:
        f_csv.writerow([num])
        num = num + 1
        wifi1 = []
        wifi2 = []
        wifi3 = []
        wifi4 = []
        wifi5 = []
        wifi6 = []
        wifi7 = []
        wifi8 = []
        wifi9 = []
        for y in x:
            if len(y) == 3:
                wifi1.append(y[0])
                wifi2.append(y[1])
                wifi3.append(y[2])
                wifi4.append('')
                wifi5.append('')
                wifi6.append('')
                wifi7.append('')
                wifi8.append('')
                wifi9.append('')
            elif len(y) == 5:
                wifi1.append(y[0])
                wifi2.append(y[1])
                wifi3.append(y[2])
                wifi4.append(y[3])
                wifi5.append(y[4])
                wifi6.append('')
                wifi7.append('')
                wifi8.append('')
                wifi9.append('')
            elif len(y) == 7:
                wifi1.append(y[0])
                wifi2.append(y[1])
                wifi3.append(y[2])
                wifi4.append(y[3])
                wifi5.append(y[4])
                wifi6.append(y[5])
                wifi7.append(y[6])
                wifi8.append('')
                wifi9.append('')
            else:
                wifi1.append(y[0])
                wifi2.append(y[1])
                wifi3.append(y[2])
                wifi4.append(y[3])
                wifi5.append(y[4])
                wifi6.append(y[5])
                wifi7.append(y[6])
                wifi8.append(y[7])
                wifi9.append(y[8])
        f_csv.writerow(['MAC'] + wifi1)
        f_csv.writerow(['Samsung'] + wifi2)
        f_csv.writerow(['Samsung'] + wifi3)
        f_csv.writerow(['LG'] + wifi4)
        f_csv.writerow(['LG'] + wifi5)
        f_csv.writerow(['Oneplus'] + wifi6)
        f_csv.writerow(['Oneplus'] + wifi7)
        f_csv.writerow(['Nexus'] + wifi8)
        f_csv.writerow(['Nexus'] + wifi9)

    f_csv.writerow(['注释:-1表示无法判断;-95的值是对空值的标准化;每9行为一组数据,同一组内去除了相差不大于10的值,去除了信号一直微弱(-75为标准)的值'])