from saveData import SaveData
import os,time
#房间设备对应，标定使用
room_devices = {'0225': 'VIE-AL10', '0207': 'VIE-AL10', '0418': 'SM-N9200', '0306': 'Nexus 5', '0314': 'Nexus 5', '0211': 'VIE-AL10', '0212': 'VIE-AL10', '1502': 'HUAWEI NXT-AL10', '0104': 'Pixel', '0110': 'MI 5', '0509': 'HUAWEI NXT-AL10', '0309': 'Nexus 5', '0318': 'OD103', '0121': 'OD103', '0206': 'VIE-AL10', '0312': 'OD103', '0313': 'Nexus 5', '04052': 'SM-N9200', '0115': 'MI 5', '0512': 'Pixel', '0108': 'MI 5', '0503': 'HUAWEI NXT-AL10', '0421': 'SM-N9200', '0417': 'SM-N9200', '0305': 'Nexus 5', '0410': 'SM-N9200', '0502': 'HUAWEI NXT-AL10', '0430': 'HUAWEI NXT-AL10', '0303': 'Nexus 5', '0220': 'OD103', '0515': 'Pixel', '0316': 'OD103', '0419': 'Pixel', '0408': 'Pixel', '0127': 'MI 5', '0202': 'VIE-AL10', '0215': 'MI 5', '0103': 'MI 5', '0501': 'HUAWEI NXT-AL10', '0409': 'SM-N9200', '0311': 'OD103', '0302': 'Nexus 5', '0315': 'OD103', '0420': 'SM-N9200', '0407': 'SM-N9200', '0304': 'Nexus 5', '0120': 'OD103', '0210': 'VIE-AL10', '0205': 'VIE-AL10', '0201': 'VIE-AL10', '1501': 'HUAWEI NXT-AL10', '0118': 'OD103', '0432': 'HUAWEI NXT-AL10', '0122': 'OD103', '0402': 'SM-N9200', '0505': 'Pixel', '0105': 'Pixel', '0219': 'Pixel', '0514': 'HUAWEI NXT-AL10', '0217': 'MI 5', '0101': 'MI 5', '0414': 'SM-N9200', '0213': 'MI 5', '0508': 'HUAWEI NXT-AL10', '0513': 'HUAWEI NXT-AL10', '0413': 'SM-N9200', '0506': 'HUAWEI NXT-AL10', '0317': 'Nexus 5', '0221': 'VIE-AL10', '0208': 'VIE-AL10', '0102': 'MI 5', '0107': 'MI 5', '0415': 'SM-N9200', '0222': 'VIE-AL10', '04181': 'SM-N9200', '0128': 'MI 5', '0216': 'MI 5', '0126': 'MI 5', '0507': 'HUAWEI NXT-AL10', '0412': 'SM-N9200', '0119': 'OD103', '0112': 'MI 5', '0308': 'Nexus 5', '0123': 'OD103', '0125': 'OD103', '0109': 'MI 5', '0214': 'MI 5', '0431': 'Pixel', '0116': 'MI 5', '04051': 'SM-N9200', '0204': 'VIE-AL10', '0307': 'Nexus 5', '0124': 'OD103', '0114': 'MI 5', '0111': 'MI 5', '0224': 'VIE-AL10', '0411': 'SM-N9200', '0301': 'Nexus 5', '0504': 'Pixel', '0416': 'SM-N9200', '0310': 'Nexus 5', '0117': 'OD103', '0209': 'VIE-AL10', '0203': 'VIE-AL10', '0106': 'MI 5', '0510': 'HUAWEI NXT-AL10', '0406': 'SM-N9200', '0223': 'VIE-AL10', '0199': 'HUAWEI NXT-AL10', '0299': 'HUAWEI NXT-AL10', '0399': 'HUAWEI NXT-AL10', '0499': 'HUAWEI NXT-AL10', '0599': 'HUAWEI NXT-AL10', '0422': 'SM-N9200'}


# 文件数据存储
def save_data_event():
    wifi_path = "Wi-Fi_Data/"
    bt_path = "BT_Data/"           
    save_data = SaveData()
    print("开始存储")
    # 获取文件夹列表
    dir_names = [name for name in os.listdir(wifi_path)]
    for dir_name in dir_names:
        room_name = dir_name.split("_")[0]
        room_device = room_devices[room_name]#设备匹配
        addr = "shilintong"+room_name 
        # 显示进度
        print(room_name + " 下的文件正在存储")
        file_names =  [name for name in os.listdir(wifi_path+dir_name)]  
        for file_name in file_names:
            file_num = file_name.split("_")[0]
            coo_x = file_name.split("_")[1]
            coo_y = (file_name.split("_")[2])[:-4]
            begin_time = time.time()

            # 存储wifi文件数据
            flag = save_data.data_save(wifi_path+dir_name+"/"+file_name,1,addr,coo_x,coo_y,room_device)

            if flag != 1:# 存储出错
                print("出错位置:"+wifi_path+dir_name + "/" +file_num+" "+flag)
                save_data.close_connect()
                return -1
            # 存储bt单文件数据
            bt_file_names =  [name for name in os.listdir(bt_path+dir_name)] 
            if file_name in bt_file_names:
                flag = save_data.data_save(bt_path+dir_name+"/"+file_name,2,addr,coo_x,coo_y,room_device)
            else:
                flag = save_data.data_save(bt_path+dir_name+"/"+file_num+".csv",2,addr,coo_x,coo_y,room_device)

            if flag != 1:# 存储出错
                print("出错位置:" +bt_path+dir_name + "/" +file_num+" "+flag)
                save_data.close_connect()
                return -1
            end_time = time.time()      
            # print(dir_name + "/"+ file_num + " saved,time:"+str(int(end_time-begin_time))+"s")

        # print("该文件夹存储完成.")

    # 全部存储结束断开连接
    save_data.close_connect()
       
    return 1
        
save_data_event()