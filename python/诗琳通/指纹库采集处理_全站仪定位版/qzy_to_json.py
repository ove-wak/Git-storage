import os,csv,time,json

# 把全站仪的位置和采集的指纹通过时间对应起来
def data_with_qzy():
    quanfiles = os.listdir("全站仪测/")
    for quanfile in quanfiles:
        quandata = []
        with open("全站仪测/"+quanfile) as csvfile:  
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:  
                quandata.append(row)
        room = quanfile.split(".")[0]
        files = os.listdir("Wi-Fi_Data/")
        for file in files:
            if room in file:
                room = file
                break
        files = os.listdir("Wi-Fi_Data/"+room)
        timed = []
        locd = []
        for file in files:
            timet = ""
            with open("Wi-Fi_Data/"+room+"/"+file) as csvfile: 
                readCSV = csv.reader(csvfile, delimiter=',')
                data = []
                for row in readCSV:
                    data.append(row)
                timet = data[2][0]
                timet = timet[:-3]
                timet = time.strftime("%m/%d/%Y %H:%M:%S",time.localtime(int(timet)+60))#全站仪绝对时间偏差约为60秒
                timed.append(timet)
        flag = 0
        for q in quandata:
            # print(q)
            if flag < len(timed) and timed[flag] in q:
                flag = flag + 1
                locd.append([q[3],q[4]])
        for j in range(len(files)):
            file_name = str(j+1).zfill(5)+"_"+str(round(float(locd[j][0]),3))+"_"+str(round(float(locd[j][1]),3))+".csv"
            os.rename("Wi-Fi_Data/"+room+"/"+files[j],"Wi-Fi_Data/"+room+"/"+file_name)
            os.rename("BT_Data/"+room+"/"+files[j],"BT_Data/"+room+"/"+file_name)

# 指纹数据转为json格式
def data_to_json(dir_path,building_id):
    data = []
    point_num = 0
    # 获取文件夹列表
    dir_names = [name for name in os.listdir(dir_path)]
    for dir_name in dir_names:
        room_name = dir_name.split("_")[0]
        floor_id = room_name[:2]
        # 显示进度
        print("正在处理 "+room_name + " 下的文件")
        begin_time = time.time()
        file_names  =  [name for name in os.listdir(dir_path+dir_name)]  
        for file_name in file_names:
            file_num = file_name.split("_")[0]
            coo_x = file_name.split("_")[1]
            coo_y = (file_name.split("_")[2])[:-4]
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
                with open(path, 'r') as file_read:
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
                            if int(ap[i]) != -200:
                                if name[i] == "null":
                                    name[i] = ""
                                record.append({'AP':ap_num,'BSSID':mac[i],'SSID':name[i],'Level':int(ap[i])})
                                ap_num = ap_num + 1
                        if ap_num != 0:
                            pt['WIFIscan'].append({'Round':round_num,'Date':line_time,'WifiScanInfo':record})
                data.append(pt) 
        end_time = time.time()
        print(room_name + " 下的文件处理完成("+str(int((begin_time-end_time)/1000))+"s)")
    return data

print("程序开始执行.")
data_with_qzy()
print("位置和指纹匹配完成.")
building_id = input("请输入建筑名称:")
wifi_path = "Wi-Fi_Data/"
bt_path = "BT_Data/" 
print("wifi指纹正在转为json格式.")
data = data_to_json(wifi_path,building_id)
print("json文件正在保存中,请稍等...")
with open(building_id+'_wifi.json', 'w') as f:
    json.dump(data, f)
print("wifi指纹转为json格式完成.\n\n\n\n\n\n\n\n")
print("蓝牙指纹正在转为json格式.")
data = data_to_json(bt_path,building_id)
print("json文件正在保存中,请稍等...")
with open(building_id+'_bt.json', 'w') as f:
    json.dump(data, f)
print("蓝牙指纹转为json格式完成.")
print("程序执行完毕.")
os.system("pause")