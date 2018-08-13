from saveData import SaveData
import os,time

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
            flag = save_data.data_save(wifi_path+dir_name+"/"+file_name,1,addr,coo_x,coo_y)

            if flag != 1:# 存储出错
                print("出错位置:"+wifi_path+dir_name + "/" +file_num+" "+flag)
                save_data.close_connect()
                return -1
            # 存储bt单文件数据
            bt_file_names =  [name for name in os.listdir(bt_path+dir_name)] 
            if file_name in bt_file_names:
                flag = save_data.data_save(bt_path+dir_name+"/"+file_name,2,addr,coo_x,coo_y)
            else:
                flag = save_data.data_save(bt_path+dir_name+"/"+file_num+".csv",2,addr,coo_x,coo_y)

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