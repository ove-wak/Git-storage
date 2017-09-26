import generate_RSS

LOC_D = 2  # 空间维度
X_SIZE = 21
Y_SIZE = 21
AP_NUM = 20  # AP数目

# 定义输入输出维度
inD = AP_NUM + LOC_D
outD = 1

RSS_AND_RSS_T = generate_RSS.generate_rss(X_SIZE, Y_SIZE, AP_NUM)  # 数据生成
RSS_NIGHT = RSS_AND_RSS_T[0]  # 晚上数据
RSS_DAY = RSS_AND_RSS_T[1]  # 白天数据（加障碍）
RSS_ = RSS_AND_RSS_T[2]  # 10lg(RSS_) = RSS_NIGHT
Influence = RSS_AND_RSS_T[3]  # 10lg(RSS_*Influence) = RSS_DAY 即变化系数
# RSS生成结束-----------------------------------------------------------------------------------------------
# RSS[行][列][AP序号] 在[-1,1]------------------------------------------------------------------------------

f = open('C:/Users/ove_wak/Desktop/OS-ELM/influence_x_y_3.txt', 'a')
for x in range(X_SIZE):
    for y in range(Y_SIZE):
        f.write(str(Influence[x][y][1] - 0.5) + ' ' + str(x) + ' ' + str(y) + '\n')
f.close()
