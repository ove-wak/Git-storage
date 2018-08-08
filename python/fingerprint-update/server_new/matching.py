from fingerprint_sequence import FingerprintSequence
from fingerprint_sequence import Category
from dbscan import dbscan
import numpy as np
import pymysql


def pprint(l):
    for i in range(len(l)):
        print("%.1f " % l[i], end='')
    print("")


class Matching:
    __current_data = None
    __historical_data = None

    __category_loc_data = None
    __category_loc_rssi_data = None

    __categories = None

    __aps_index = None

    def __init__(self, signal_type):
        self.__current_data = []
        self.__historical_data = []
        self.__category_loc_data = []
        self.__category_loc_rssi_data = []
        self.__categories = []
        self.__aps_index = {}
        return

    # 返回FingerprintSequence List
    def __read_data_DB(self, time_start=0, time_end=0):
        '''
                                fingerprint_record
        +------------------+-------------+------+-----+---------+-------+
        | Field            | Type        | Null | Key | Default | Extra |
        +------------------+-------------+------+-----+---------+-------+
        | fid              | int(10)     | NO   | PRI | NULL    |       |
        | model_num        | int(10)     | NO   |     | NULL    |       |
        | address          | varchar(40) | NO   |     | NULL    |       |
        | signal_type      | int(10)     | NO   |     | NULL    |       |
        | coordinate_x     | float(10,3) | NO   |     | NULL    |       |
        | coordinate_y     | float(10,3) | NO   |     | NULL    |       |
        | signal_time      | varchar(40) | YES  |     | NULL    |       |
        | uploading_device | varchar(40) | NO   |     | NULL    |       |
        +------------------+-------------+------+-----+---------+-------+

                                    signal_record
        +--------------------+-------------+------+-----+---------+-------+
        | Field              | Type        | Null | Key | Default | Extra |
        +--------------------+-------------+------+-----+---------+-------+
        | sid                | int(10)     | NO   | PRI | NULL    |       |
        | fid                | int(10)     | NO   |     | NULL    |       |
        | signal_mac_address | varchar(20) | YES  |     | NULL    |       |
        | signal_name        | varchar(20) | YES  |     | NULL    |       |
        | signal_strength    | int(10)     | NO   |     | NULL    |       |
        +--------------------+-------------+------+-----+---------+-------+
        '''
        results_ = []
        results = []
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "Zc199410", "ZC_DB")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        cursor.execute("select * from fingerprint_record where id >= 0 and signal_time >= \'"
                       + time_start + "\' and signal_time <= \'" + time_end
                       + "\' order by uploader, signal_time")
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchall()
        last_uploader = ""
        start_loc = np.array([-100.0, -100.0])
        current_loc = np.array([-100.0, -100.0])
        last_loc = np.array([-100.0, -100.0])
        last_time = -100
        current_sequence = None
        for i in range(len(data)):
            fid = data[i][0]
            stype = data[i][3]
            current_loc[0] = data[i][4]
            current_loc[1] = data[i][5]
            stime = data[i][6]
            uploader = data[i][7]
            if uploader == last_uploader \
                    and np.sqrt(np.sum(np.square(current_loc - last_loc))) < 1 \
                    and np.sqrt(np.sum(np.square(current_loc - start_loc))) < 3 \
                    and (int(stime) - last_time) <= 3:
                # 当同一个用户上传 当前位置与 起点和上个点 足够近， 时间间隔足够短，在当前序列添加节点
                current_sequence.add_node(fid, current_loc[0], current_loc[1], stime)
            else:
                # 否则新建序列，并及加入结果列表
                current_sequence = FingerprintSequence(fid, current_loc[0], current_loc[1], stime, stype, uploader)
                start_loc[0] = current_loc[0]
                start_loc[1] = current_loc[1]
                results_.append(current_sequence)
            last_uploader = uploader
            last_loc[0] = current_loc[0]
            last_loc[1] = current_loc[1]
            last_time = int(stime)

        ap_ii = 0
        for i in range(len(results_)):
            current_sequence = results_[i]
            if len(current_sequence) > 3:
                for j in range(len(current_sequence)):
                    fid = current_sequence.fids[j]
                    cursor.execute("select * from signal_record where record_id = " + str(fid))
                    rssis_info = cursor.fetchall()
                    for k in range(len(rssis_info)):
                        mac = rssis_info[k][2]
                        if self.__aps_index.get(mac) is None:
                            self.__aps_index[mac] = ap_ii
                            ap_ii += 1

        for i in range(len(results_)):
            current_sequence = results_[i]
            if len(current_sequence) > 3:
                current_sequence.nodes_rssi = [None] * len(current_sequence)
                for j in range(len(current_sequence)):
                    current_sequence.nodes_rssi[j] = [-100] * len(self.__aps_index)
                    fid = current_sequence.fids[j]
                    cursor.execute("select * from signal_record where record_id = " + str(fid))
                    rssis_info = cursor.fetchall()
                    for k in range(len(rssis_info)):
                        mac = rssis_info[k][2]
                        ii = self.__aps_index[mac]
                        current_sequence.nodes_rssi[j][ii] = rssis_info[k][4]
                current_sequence.feature_extraction()
                results.append(current_sequence)
        # 关闭数据库连接
        db.close()

        return results

    # 划分历史数据
    def history_division(self, time_start=0, time_end=0):
        self.__historical_data = self.__read_data_DB(time_start, time_end)
        # print(len(self.__historical_data))
        '''
        for i in range(len(self.__historical_data)):
            t = self.__historical_data[i]
            print(t.uploader)
            pprint(t.feature_location)
            pprint(t.feature_avg)
            pprint(t.feature_std)
            pprint(t.feature_max)
            for j in range(len(t)):
                print(t.nodes_time[j], end=' ')
                print(t.nodes_rssi[j])
        '''
        if self.__division_loc():
            return self.__division_rssi()
        else:
            return False

    # 按照位置划分数据
    def __division_loc(self):
        # 计算每一个对象的类别号
        category_loc = dbscan(self.__historical_data, 1.5, 3, FingerprintSequence.distance_loc)
        category_loc_num = int(np.max(category_loc + 1))
        if category_loc_num == 1:
            return False
        '''
        print(category_loc)
        print(category_loc_num)

        for i in range(len(self.__historical_data)):
            t = self.__historical_data[i]
            print(t.uploader, ' ', i, ' ', category_loc[i])
            pprint(t.feature_location)
            pprint(t.feature_avg)
            pprint(t.feature_std)
            pprint(t.feature_max)
        '''
        self.__category_loc_data = [0] * category_loc_num
        # 统计每一类数据数目
        category_loc_data_num = [0] * category_loc_num
        counts_loc = [0] * category_loc_num
        for i in range(len(category_loc)):
            category_loc_data_num[int(category_loc[i])] += 1
        # 初始化每一类数据的列表
        for i in range(category_loc_num):
            self.__category_loc_data[i] = [0] * category_loc_data_num[i]
        # 为每一位置类添加数据 __category_loc_data[i][j]表示第i个位置类中的第j个数据
        for i in range(category_loc.shape[0]):
            self.__category_loc_data[int(category_loc[i])][int(counts_loc[int(category_loc[i])])] = \
                self.__historical_data[i]
            counts_loc[int(category_loc[i])] += 1
        '''
        for i in range(len(self.__category_loc_data)):
            # print(len(self.__category_loc_data[i]))
            for j in range(len(self.__category_loc_data[i])):
                t = self.__category_loc_data[i][j]
                print(t.uploader, ' ', i)
                pprint(t.feature_location)
                pprint(t.feature_avg)
                pprint(t.feature_std)
                pprint(t.feature_max)
        '''

        # print(counts_loc)
        return True

    # 按照rssi划分数据
    def __division_rssi(self):
        # 总位置类数目
        category_loc_num = len(self.__category_loc_data)
        category_loc_rssi = [None] * category_loc_num
        # print(category_loc_num)
        # print(category_loc_rssi)
        # 计算各个位置类中 各个数据对应的rssi类序号，每个位置类中rssi类序号都从0开始
        for i in range(1, len(self.__category_loc_data)):
            # category_loc_rssi[i][j] 第i位置类中第j个样本的rssi类序号
            category_loc_rssi[i] = dbscan(self.__category_loc_data[i], 5, 2, FingerprintSequence.distance_rssi)
            # print(category_loc_rssi[i])
        self.__category_loc_rssi_data = [None] * category_loc_num

        # 统计每个位置类中 rssi类各个类别的数据数目
        # category_loc_rssi_data_num[i][j] 第i个位置类中第j个rssi类中数据的数目
        category_loc_rssi_data_num = [ [] for i in range(category_loc_num)]
        for i in range(1, category_loc_num):
            # 第i个位置类中 所有rssi类数据数目初始化为0
            category_loc_rssi_data_num[i] = [0] * int(np.max(category_loc_rssi[i]) + 1)
            for j in range(len(category_loc_rssi[i])):
                # 第i个位置类中 第j个数据对应的rssi类数目加1
                category_loc_rssi_data_num[i][int(category_loc_rssi[i][j])] += 1
        # print(category_loc_rssi_data_num)

        # 为每个位置类中的rssi类列表分配空间
        for i in range(1, len(self.__category_loc_data)):
            # 第i位置类中rssi类列表初始化
            self.__category_loc_rssi_data[i] = [[] for i in range(len(category_loc_rssi_data_num[i]))]
            # 第i位置类中第j个rssi类列表初始化
            for j in range(1, len(self.__category_loc_rssi_data[i])):
                self.__category_loc_rssi_data[i][j] = [[] for i in range(category_loc_rssi_data_num[i][j])]
        # print(self.__category_loc_rssi_data)
        # 开始向category_loc_rssi_data写入数据
        # __category_loc_rssi_data[i][j][k] 表示第i个位置类中第j个rssi类中第k个数据
        # count_loc_rssi[i][j]表示i位置类 j rssi类中已写入的数据数目
        count_loc_rssi = [[0] * len(category_loc_rssi_data_num[i]) for i in range(category_loc_num)]
        # print(count_loc_rssi)
        # print()

        for i in range(1, category_loc_num):
            for j in range(len(category_loc_rssi[i])):
                ca_loc_rssi = int(category_loc_rssi[i][j])
                # print(i, ' ', ca_loc_rssi)
                # print(len(self.__category_loc_rssi_data[i]), ' ', len(self.__category_loc_rssi_data[i][ca_loc_rssi]))
                if ca_loc_rssi > 0:
                    self.__category_loc_rssi_data[i][ca_loc_rssi][count_loc_rssi[i][ca_loc_rssi]] = \
                        self.__category_loc_data[i][j]
                    count_loc_rssi[i][ca_loc_rssi] += 1

        print(count_loc_rssi)
        # 开始为每个位置rssi类建立对象
        for i in range(1, category_loc_num):
            for j in range(1, len(category_loc_rssi_data_num[i])):
                # print(i, ' ', j)
                self.__categories.append(Category(self.__category_loc_rssi_data[i][j]))
        print(len(self.__categories))
        for i in range(len(self.__categories)):
            for j in range(len(self.__categories[i].data)):
                print(self.__categories[i].data[j].uploader, ' ', self.__categories[i].data[j].feature_location, ' ', i)

        return True

    # 历史数据匹配
    def history_matching(self, current_start=0, current_end=0):
        current_data = self.__read_data_DB(current_start, current_end)
        for i in range(len(current_data)):
            print(current_data[i].uploader, ' ', current_data[i].feature_location)
        matched_seqs = []
        results = [None] * len(self.__aps_index)
        for i in range(len(current_data)):
            current_lfs = current_data[i]
            for j in range(len(self.__categories)):
                m = self.__categories[j].matched(current_lfs)
                if m:
                    for k in range(len(self.__categories[j])):
                        self.__categories[j].data[k].confidence = m
                        if self.__categories[j].data[k] not in matched_seqs:
                            matched_seqs.append(self.__categories[j].data[k])
        results = [[] for i in range(len(self.__aps_index))]
        for i in range(len(matched_seqs)):
            print(matched_seqs[i].feature_location, ' ', matched_seqs[i].uploader)
            print(matched_seqs[i].feature_avg)
        for i in range(len(matched_seqs)):
            [x, y] = matched_seqs[i].feature_location
            for k in range(len(self.__aps_index)):
                if matched_seqs[i].feature_avg[k] > -100:
                    value = matched_seqs[i].feature_avg[k]
                    c = matched_seqs[i].confidence
                    results[k].append([x, y, value, c])
        return results


match = Matching(0)
match.history_division("01000", "01500")
result__ = match.history_matching("02000", "03000")
for i in range(len(result__)):
    print(result__[i])
print()
result__ = match.history_matching("03000", "04000")
for i in range(len(result__)):
    print(result__[i])
# print(aps_index)
# Matching.read_data_DB
