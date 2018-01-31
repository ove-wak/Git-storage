# 底图保存为excel
# 单独文件,未与其他部分连接
import xlwt
ap_mac = ('d8:15:0d:6c:13:98','00:90:4c:5f:00:2a','ec:17:2f:94:82:fc','70:ba:ef:d5:a6:12')
# 原始数据的底图
ditu = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, [-45, -53, -51, -47], 0, [-36, -48, -36, -43], 0, [-37, -50, -48, -44], 0, [-33, -45, -27, -50], 0, [-36, -54, -45, -51], 0, [-35, -54, -43, -53], 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, [-47, -56, -56, -46], 0, [-35, -49, -56, -47], 0, [-36, -58, -48, -56], 0, [-32, -49, -38, -50], 0, [-39, -47, -42, -54], 0, [-41, -56, -48, -54], 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, [-41, -43, -43, -33], 0, [-37, -50, -52, -40], 0, [-36, -41, -39, -45], 0, [-40, -38, -40, -49], 0, [-22, -47, -42, -45], 0, [-22, -47, -45, -52], 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, [-44, -54, -50, -37], 0, [-44, -53, -50, -33], [-41, -47,-47,-39], [-37, -42,-43,-45], [-33, -37, -40, -51], [-35, -38, -49, -50], 0, [-23, -49, -43, -58], 0, [-19, -40, -51, -54], 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
ap_m = [[[0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0]],
        [[0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0]],
        [[0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0]],
        [[0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0]]]
for x in range(len(ditu)):
    for y in range(len(ditu[0])):
        if ditu[x][y] == 0:
            ap_m[0][x][y] = 0
            ap_m[1][x][y] = 0
            ap_m[2][x][y] = 0
            ap_m[3][x][y] = 0
        else:
            ap_m[0][x][y] = ditu[x][y][0]
            ap_m[1][x][y] = ditu[x][y][1]
            ap_m[2][x][y] = ditu[x][y][2]
            ap_m[3][x][y] = ditu[x][y][3]

wb = xlwt.Workbook(encoding='utf-8')

for t in range(4):
    ws = wb.add_sheet("ap"+str(t))
    ws.write(0, 0, "y\\x")
    for x in range(len(ap_m[t])):
        ws.write(0, x+1, x)
        for y in range(len(ap_m[t][0])):
            if x == 0:
                ws.write(y+1, 0, y)
                ws.write(y+1,x+1,0)
            elif x == 1 or x == 9 or y == 0 or y == 12:
                ws.write(y+1,x+1,0)
            else:
                if ap_m[t][x][y] != 0:
                    ws.write(y+1, x+1, ap_m[t][x][y])
                elif (x % 2) == 1 and (y % 2) == 1:
                    ws.write(y+1, x+1, int((ap_m[t][x-1][y]+ap_m[t][x+1][y])/2))
                elif (x % 2) == 1 and (y % 2) == 0:
                    ws.write(y+1, x+1, int((ap_m[t][x-1][y-1]+ap_m[t][x-1][y+1]+ap_m[t][x+1][y-1]+ap_m[t][x+1][y+1])/4))
                else:
                    ws.write(y+1, x+1, int((ap_m[t][x][y-1]+ap_m[t][x][y+1])/2))


wb.save('excel/底图.xls')