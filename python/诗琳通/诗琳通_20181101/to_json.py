import os,csv,time,json
import jpype
from jpype import *
jvmPath = u'C:\\Program Files\\Java\\jre-9.0.4\\bin\\server\\jvm.dll'
jpype.startJVM(jvmPath,"-Djava.class.path=C:\\Users\\ovewa\\Desktop\\trans.jar")
trans = JClass('wak.Trans')
# wifi指纹数据转为json格式
def wifidata_to_json(dir_path,building_id):

    data = [[],[],[],[],[]]
    point_num = 0
    # 获取文件夹列表
    dir_names = [name for name in os.listdir(dir_path)]
    for dir_name in dir_names:
        room_name = dir_name.split("_")[0]
        floor_id = str(int(room_name[:2]))
        # 显示进度
        print("正在处理 "+room_name + " 下的文件")
        begin_time = time.time()
        file_names  =  [name for name in os.listdir(dir_path+dir_name)]  
        for file_name in file_names:
            file_num = file_name.split("_")[0]
            coo_x = file_name.split("_")[1]
            coo_y = (file_name.split("_")[2])[:-4]


            # 诗琳通原始数据坐标有偏差，现校准 --20180906
            coo_x = float(coo_x) - 0.169
            coo_y = float(coo_y) + 0.0276
            # 坐标系转换
            ba = trans.xy2LB([coo_y, coo_x - 500000])
            coo_y = ba[0]
            coo_x = ba[1]

            path = dir_path+dir_name+"/"+file_name
            if os.path.getsize(path):#判断文件是否为空  
                pt = {} 
                pt['Point NO'] = point_num
                pt['PosLon'] = float(coo_x)
                pt['PosLat'] = float(coo_y)
                pt['Building ID'] = building_id
                pt['Floor ID'] = floor_id
                pt['WIFIscan'] = []
                point_num = point_num + 1 
                with open(path, 'rt', encoding='utf-8') as file_read:
                    line_datas = []
                    read = csv.reader(file_read)
                    for i in read:
                        line_datas.append(i)
                    name = line_datas[0][1:]
                    # print(name)
                    mac = line_datas[1][1:]
                    for x in range(2,len(line_datas)):
                        round_num = x - 1
                        line_data = line_datas[x]
                        line_timet = line_data.pop(0)
                        line_time = line_timet[:-3]
                        line_time = time.strftime("%y-%m-%d %H:%M:%S",time.localtime(int(line_time)))
                        if round_num == 1:
                            pt['Date'] = line_time
                        ap = line_data
                        ap_num = 0
                        record = []
                        for i in range(len(ap)):
                            ap_value = int(ap[i])
                            if ap_value != -200:
                                if name[i] == "null":
                                    name[i] = ""
                                # wifi值转为正数
                                ap_value = abs(ap_value)
                                record.append({'AP':ap_num,'BSSID':mac[i],'SSID':name[i],'Level':ap_value})
                                ap_num = ap_num + 1
                        if ap_num != 0:
                            pt['WIFIscan'].append({'Round':round_num,'Date':line_time,'WifiScanInfo':record})
                data[int(floor_id)-1].append(pt) 
        end_time = time.time()
        print(room_name + " 下的文件处理完成("+str(int((begin_time-end_time)/1000))+"s)")
    return data
# 蓝牙数据转为json格式
def btdata_to_json(dir_path,building_id):
    data = [[],[],[],[],[]]
    # 获取文件夹列表
    dir_names = [name for name in os.listdir(dir_path)]
    for dir_name in dir_names:
        room_name = dir_name.split("_")[0]
        floor_id = str(int(room_name[:2]))
        # 显示进度
        print("正在处理 "+room_name + " 下的文件")
        begin_time = time.time()
        file_names  =  [name for name in os.listdir(dir_path+dir_name)]  
        for file_name in file_names:
            if '-' in file_name:
                file_num = file_name.split("_")[0]
                coo_x = file_name.split("_")[1]
                coo_y = (file_name.split("_")[2])[:-4]
            else:
                file_num = file_name.split(".")[0]
                fts = [name for name in os.listdir(wifi_path+dir_name)]
                for ft in fts:
                    if file_num in ft:
                        coo_x = ft.split("_")[1]
                        coo_y = (ft.split("_")[2])[:-4]

            # 诗琳通原始数据坐标有偏差，现校准 --20180906
            coo_x = float(coo_x) - 0.169
            coo_y = float(coo_y) + 0.0276
            # 坐标系转换
            ba = trans.xy2LB([coo_y, coo_x - 500000])
            coo_y = ba[0]
            coo_x = ba[1]

            path = dir_path+dir_name+"/"+file_name
            if os.path.getsize(path):#判断文件是否为空  
                pt = {}          
                pt['PosLon'] = float(coo_x)
                pt['PosLat'] = float(coo_y)
                line_datas = []
                with open(path, 'rt', encoding='utf-8') as file_read:  
                    read = csv.reader(file_read)
                    for i in read:
                        line_datas.append(i)
                if len(line_datas) != 2:
                    pt['TimeStamp'] = line_datas[2][0]
                    pt['ScanResult'] = []
                    names = line_datas[0][1:]
                    macs = line_datas[1][1:]
                    for i in range(len(names)):
                        rssiinfo = []
                        for x in range(2,len(line_datas)):
                            ap_value = int(line_datas[x][i+1])
                            if ap_value != -200:
                                if names[i] == "null":
                                    rssiinfo.append({"RSSI":ap_value,"APaddress":macs[i]})
                                else:
                                    rssiinfo.append({"APname":names[i],"RSSI":ap_value,"APaddress":macs[i]})
                        if rssiinfo != []:
                            pt['ScanResult'].append({"RSSI info":rssiinfo,"APaddress":macs[i]})
                    data[int(floor_id)-1].append(pt) 
        end_time = time.time()
        print(room_name + " 下的文件处理完成("+str(int((begin_time-end_time)/1000))+"s)")
    return data



print("程序开始执行.")
building_id = "shilintong"
wifi_path = "Wi-Fi_Data/"
bt_path = "BT_Data/" 
print("wifi指纹正在转为json格式.")
data = wifidata_to_json(wifi_path,building_id)
print("json文件正在保存中,请稍等...")
for x in range(5):
    with open('shilintong/floor_'+str(x+1)+'/WIFIscan.json', 'w') as f:
        json.dump(data[x], f)
print("wifi指纹转为json格式完成.\n\n\n\n\n\n\n\n")
print("蓝牙指纹正在转为json格式.")
data = btdata_to_json(bt_path,building_id)
print("json文件正在保存中,请稍等...")
for x in range(5):
    with open('shilintong/floor_'+str(x+1)+'/IBeaconScan.json', 'w') as f:
        json.dump(data[x], f)
print("蓝牙指纹转为json格式完成.")
print("程序执行完毕.")
os.system("pause")