import xlrd
import numpy as np

dir = input('Enter Dir Path( C:/dir0/dtr1 )')
if dir == '':
    dir = 'D:/QQ Files/1004385883/FileRecv/08-01 c204 data/noman'
print('Got Dir Path: '+dir)

head = ''         # 文件名x坐标前
mid = '-'         # 坐标中间
tail = '-.xls'     # y坐标后

X_max = 12        # 最大行数
Y_max = 12        # 最大列数
index_len = 2     # 坐标字符串长度
MAC_MAX = 300

SAMPLE_NUM = 0    # 样本数目
MAC_NUM = 0       # 设备数目
SAMPLE = None     # 样本列表 每项为 RSS向量
MAC = []          # MAC列表
MAC_effective = []#可利用的MAC 0:不可用 1:可用


SAMPLE_TMP = [[[[] for i in range(MAC_MAX)] for j in range(Y_max)]for k in range(X_max)]   # 临时样本列表 四维 X Y MAC 采集号, 元素值为RSS
print(len(SAMPLE_TMP))
print(len(SAMPLE_TMP[0]))
print(len(SAMPLE_TMP[0][0]))

for x in range(X_max):
    for y in range(Y_max):
        xc = str(x)
        yc = str(y)
        if len(xc) < index_len:
            xc = '0'* (index_len-len(xc)) + xc
        if len(yc) < index_len:
            yc = '0' * (index_len - len(yc)) + yc
        file_path = dir+'/'+head+xc+mid+yc+tail


        data = None                         # x y 处的数据
        try:
            data = xlrd.open_workbook(file_path)
        except Exception as e:
            print(e)
            continue
        print('open file: '+ file_path)

        sheet = data.sheet_by_index(0)      # Excel sheet对象a

        nrows = sheet.nrows                 # 行数
        ncols = sheet.ncols                 # 列数

        row_start = int(nrows/3)                 # 去除人开始采数的干扰
        row_end = int(nrows*2/3)                 # 去除人停止采数的干扰

        for i in range(row_start,row_end):
            row = sheet.row_values(i)           # 获取行

            for j in range(0,len(row),2):
                if row[j] != '':
                    if row[j] not in MAC:      # 未扫描过该AP
                        MAC.append(row[j])
                    index = MAC.index(row[j])   # MAC编号
                    try:
                        SAMPLE_TMP[x][y][index].append(row[j+1])    # 添加X Y 处，该MAC 某次测得的RSS
                    except Exception as e:
                        print(x)
                        print(y)
                        print(index)
                        print(row[j])
                        print(e)
                        exit()


'''
print(len(MAC))
for x in range(X_max):
    for y in range(Y_max):
        for mac in range(len(MAC)):
            try:
                print("%10d     %s" % (mac,MAC[mac]),end = '       ')
                print(SAMPLE_TMP[x][y][mac])
            except Exception as e:
                print(e)
                print(x)
                print(y)
                print(mac)
                exit()
        print('\n\n')
'''

SAMPLE = [[[-100.0 for mac in range(len(MAC))]for y in range(Y_max)]for x in range(X_max)]
MAC_effective = [0 for mac in range(len(MAC))]

for x in range(X_max):
    for y in range(Y_max):
        for mac in range(len(MAC)):
            mean = 0.0
            num = 0
            for i in range(len(SAMPLE_TMP[x][y][mac])):
                mean += SAMPLE_TMP[x][y][mac][i]
                num += 1
            if num > 0:
                mean = mean/float(num)
                SAMPLE[x][y][mac] = mean

for mac in range(len(MAC)):
    num = 0
    for x in range(X_max):
        for y in range(Y_max):
            if SAMPLE[x][y][mac] != -100:
                num += 1
    if num > 3:
        MAC_effective[mac] = 1
'''
for x in range(X_max):
    for y in range(Y_max):
        print ('%d %d:  '%(x,y))
        for mac in range(len(MAC)):
            print("%2.1f"%SAMPLE[x][y][mac],end='\t')
        print('\n')
    print('\n')
'''

for mac in range(len(MAC)):
    if MAC_effective[mac] == 1:
        print('\n========================================================================================================\n')
        print(MAC[mac])
        print('--------------------------------------------------------------------------------------------------------')
        print("    ", end='\t|')
        for y in range(Y_max):
            if y >= 10:
                print(" %2.1f" % float(y), end='\t|')
            else:
                print(" 0%2.1f" % float(y), end='\t|')
        print('\n--------------------------------------------------------------------------------------------------------')
        for x in range(X_max):
            if x >= 10:
                print("%2.1f" % float(x), end='\t|')
            else:
                print("0%2.1f" % float(x), end='\t|')
            for y in range(Y_max):
                if SAMPLE[x][y][mac] > -100.0:
                    print("%2.1f" % SAMPLE[x][y][mac], end='\t|')
                else:
                    print("    ", end='\t|')
            print('\n--------------------------------------------------------------------------------------------------------')





