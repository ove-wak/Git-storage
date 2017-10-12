import numpy as np


def generate_rss(X_SIZE = 21, Y_SIZE = 21, AP_NUM = 20):
    LOC_D = 2

    SIG_STR = 0.0000002
    ADJUST = -100.0  # 信号强度系数

    MAN = [[8, 8], [12, 13], [5, 8]]
    RSS_NIGHT = [[[-100.0 for i in range(AP_NUM)] for j in range(Y_SIZE)] for k in range(X_SIZE)]     # RSSi
    RSS_ = [[[0.0 for i in range(AP_NUM)] for j in range(Y_SIZE)] for k in range(X_SIZE)]     # RSSi 10lg(RSS_) = RSS
    RSS_DAY = [[[-100.0 for i in range(AP_NUM)] for j in range(Y_SIZE)] for k in range(X_SIZE)]

    Influence = [[[1.0 for i in range(AP_NUM)] for j in range(Y_SIZE)] for k in range(X_SIZE)]

    AP = [[0.0 for i in range(LOC_D + 1)] for j in range(AP_NUM)]   # AP 坐标 强度
    EXIST_AP = [0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    AP_LOCS = [[0.5, 0.5],
               [float(X_SIZE) - 1.5, float(Y_SIZE) - 1.5],
               [0.5, float(Y_SIZE) - 1.5],
               [float(X_SIZE) - 1.5, 0.5],
               [999.0, 999.0],
               [float(X_SIZE) / 2.0, float(Y_SIZE) / 2.0],
               [2.8,5.4],
               [6.3,11.3],
               [7.4,8.1],
               [9.5,12.1],
               [6.8,2.7],
               [7.1,19.2],
               [999.0,999.0]]

   # AP_STRS = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0,1.0,1.0,1.0,1.0,1.0,1.0]


    def influence(man, ap, a,r_x, r_y):
        a_x = ap[a][0]  # ap
        a_y = ap[a][1]
        a_sig_str = ap[a][LOC_D]

        m_x = man[0]  # man
        m_y = man[1]

        vec_a_m = [m_x - a_x, m_y - a_y]  # ap -> man
        vec_r_m = [m_x - r_x, m_y - r_y]  # reciever -> man
        vec_r_a = [a_x - r_x, a_y - r_y]  # reciever -> ap

        mod_a_m_dis = np.sqrt(np.square(vec_a_m[0]) + np.square(vec_a_m[1]))
        mod_r_m_dis = np.sqrt(np.square(vec_r_m[0]) + np.square(vec_r_m[1]))
        mod_r_a_dis = np.sqrt(np.square(vec_r_a[0] + np.square(vec_r_a[1])))

        if mod_r_m_dis == 0 or mod_a_m_dis == 0:
            return

        cos_a_r_m = (vec_r_a[0] * vec_r_m[0] + vec_r_a[1] * vec_r_m[1]) / (mod_r_a_dis * mod_r_m_dis)
        cos_a_m_r = (vec_a_m[0] * vec_r_m[0] + vec_a_m[1] * vec_r_m[1]) / (mod_a_m_dis * mod_r_m_dis)

        if cos_a_m_r > 0:  # 反射
            Influence[x][y][a] += cos_a_m_r / np.square(mod_a_m_dis+mod_r_m_dis+1.0) * 40.0
        elif cos_a_m_r < -0.7:  # 阻挡
            Influence[x][y][a] += cos_a_m_r  / mod_r_m_dis
        if Influence[x][y][a] < 0.0:
            Influence[x][y][a] = 0.0
        return

    # AP位置及信号强度初始化
    APS = 0
    for a in range(AP_NUM):
        if EXIST_AP[a]:
            for j in range(LOC_D):
                AP[a][j] = AP_LOCS[APS][j]  # 位置
                #print("%f %d %d" % (AP_LOCS[APS][j], APS, j))
            AP[a][LOC_D] = SIG_STR  # 强度
            APS = APS + 1

    # 所有位置RSS初始化
    for x in range(X_SIZE):
        for y in range(Y_SIZE):
            for a in range(AP_NUM):
                if EXIST_AP[a]:
                    ap_x = AP[a][0]
                    ap_y = AP[a][1]
                    if np.abs(ap_x - float(x)) > 0.0001 or np.abs(ap_y - float(y)) > 0.0001:  # AP与测量点位置不重合
                        RSS_[x][y][a] = AP[a][LOC_D] / (np.sqrt(np.square(float(x) - ap_x) + np.square(float(y) - ap_y)))
                        RSS_NIGHT[x][y][a] = np.log10( RSS_[x][y][a]) * 10


    for x in range(X_SIZE):
        for y in range(Y_SIZE):
            for a in range(AP_NUM):
                RSS_NIGHT[x][y][a] = RSS_NIGHT[x][y][a] / ADJUST

    # RSS生成结束-------------------------------------------------------------------------------------------------------------------------------------
    # RSS[行][列][AP序号] 在[-1,1]--------------------------------------------------------------------------------------------------------------------

    for x in range(X_SIZE):
        for y in range(Y_SIZE):
            for a in range(AP_NUM):
                if EXIST_AP[a]:
                    for man in MAN:
                        influence(man,AP,a,x,y)

    for x in range(X_SIZE):
        for y in range(Y_SIZE):
            for a in range(AP_NUM):
                if EXIST_AP[a]:
                    sig = RSS_[x][y][a] * Influence[x][y][a]
                    if sig != 0.0:
                        RSS_DAY[x][y][a] = np.log10(sig) * 10

    for x in range(X_SIZE):
        for y in range(Y_SIZE):
            for a in range(AP_NUM):
                RSS_DAY[x][y][a] = RSS_DAY[x][y][a] / ADJUST

    '''
    for a in range(AP_NUM):
        #if EXIST_AP[a]:
            print('%f\t\t%f'%(AP[a][0],AP[a][1]))
            print(MAN)
            for x in range(X_SIZE):
                for y in range(Y_SIZE):
                    print('%8f'%RSS[x][y][a], end='\t')
                print()
            print('\n')
    
            for x in range(X_SIZE):
                for y in range(Y_SIZE):
                    print('%8f'%Influence[x][y][a], end='\t')
                print()
            print('\n')
    
            for x in range(X_SIZE):
                for y in range(Y_SIZE):
                    print('%8f'%RSS_T[x][y][a], end='\t')
                print()
            print('\n')
    '''
    # RSS_NIGHT,RSS_DAY 缩放到[0,1]
    return [RSS_NIGHT,RSS_DAY,RSS_,Influence]

#generate_rss()








