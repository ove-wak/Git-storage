import pymysql
import numpy as np


# print("data_generating")
aps_location = [[4, 4], [3, 7], [2, 8], [10, 1], [10, 1], [1, 1], [10, 10], [70, 60]]
aps_strength = [0.001, 0.0012, 0.002, 0.0008, 0.001, 0.001, 0.001, 0.001]
aps_mac = ["a1", "a2", "a3", "a4", "c1", "c2", "c3", "c4"]
aps_index = {}
for i in range(len(aps_mac)):
    aps_index[aps_mac[i]] = i


def data_generating():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "Zc199410", "ZC_DB")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()
    uploaders = ['a001', 'a002', 'a003', 'a004', 'a005', 'a006', 'a007']
    location = [[3, 4], [6, 8], [9, 2], [2, 5], [4, 6], [4.3, 6.2], [4.4, 6.4]]
    time_ = [3000] * len(location)
    model_num = 1
    address = 'c207'
    signal_type = 1
    # cmd = "select max(id) from fingerprint_record"
    # cursor.execute(cmd)
    # db.commit()
    # fid = cursor.fetchone()[0] + 1

    cmd = "delete from fingerprint_record"
    cursor.execute(cmd)
    cmd = "delete from signal_record"
    cursor.execute(cmd)
    db.commit()

    fid = 0

    for i in range(400):
        current_index = np.random.randint(0, len(uploaders))
        # current_index = np.random.randint(2, 3)
        uploader = uploaders[current_index]
        x = location[current_index][0] + np.random.rand()
        y = location[current_index][1] + np.random.rand()
        temp = np.random.randint(0, 30)
        if temp == 0:
            time_[current_index] += 5
        elif temp < 1 == 1:
            time_[current_index] += 4
        elif temp < 3 == 1:
            time_[current_index] += 3
        elif temp < 5 == 1:
            time_[current_index] += 2
        else:
            time_[current_index] += 1

        signal_time = '0' + str(time_[current_index])
        fid += 1
        cmd = "insert into fingerprint_record values(" \
              + str(fid) + ',' \
              + str(model_num) + ',' \
              + '\'' + address + "\'," \
              + str(signal_type) + ',' \
              + str(x) + ',' \
              + str(y) + ',' \
              + "\'" + signal_time + "\'," \
              + "\'" + uploader + "\');"
        # print(cmd)
        cursor.execute(cmd)
        # print(i)
    db.commit()



    cmd = "select * from fingerprint_record"
    cursor.execute(cmd)
    db.commit()
    results = cursor.fetchall()
    signal_id = 0
    for i in range(len(results)):
        fid = results[i][0]
        x = results[i][4]
        y = results[i][5]
        for j in range(len(aps_mac)):
            # 一定概率本次扫描中该AP未搜到
            if np.random.randint(0, 10) != 0:
                signal_id += 1
                ap_mac = aps_mac[j]
                ap_x = aps_location[j][0]
                ap_y = aps_location[j][1]
                ap_strength = aps_strength[j]
                dx = ap_x - x
                dy = ap_y - y
                rssi = 10 * np.log10(ap_strength/(1 + dx*dx + dy*dy)) - 1 + np.random.rand()*2
                cmd = "insert into signal_record values(" + str(signal_id) + ',' + str(fid) + ",\'" + ap_mac + "\'," + "null" + "," + str(rssi) + ");"
                # print(cmd)
                cursor.execute(cmd)
    db.commit()
    db.close()

data_generating()
