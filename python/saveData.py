import os
from connectMysql import ConnectMysql
path = "C:/Users/ove_wak/Desktop/git-storage/OS-ELM-matlab/wifiinfo/"
path_time = "11.17/"
file_name = []

# 连接数据库
conn = ConnectMysql()

# 如果表不存在则创建表
conn.create_table()

# 获取指定目录下所有数据的文件名
tt = os.walk(path + path_time)
for i in tt:
    for j in i[2]:
        if ".txt" in j:
            file_name.append(j)

# 遍历指定目录下所有数据文件并插入到数据库中
for file in file_name:
    with open(path + path_time + file, 'r') as file_read:
        file_a = file.split('.')
        file_b = file_a[0].split('-')
        addr = file_b[0]
        strx = file_b[1] # 注意x,y的先后
        stry = file_b[2]
        phoneIP = strx + ', ' +stry # ##phoneIP为采集中缺失的参数,暂时用位置和代替
        while True:
            lines = file_read.readline() # 读取整行数据
            if not lines:
                break
            line_data = lines.split()
            line_time = line_data.pop(0)
            line_time = line_time + " " + line_data.pop(0)
            mac = []
            ap = []
            if line_data:
                for x in range(0,2,len(line_data)):
                    mac.append(line_data[x])
                    ap.append(line_data[x+1])

            flag = conn.insert_data(addr,phoneIP,1,strx,stry,line_time,mac,ap)  
            if flag == -1:
                print("数据库插入数据出错")
                print(file+lines)
                break       
    print(file+"已存储完成")    

# 数据库中的数据需要全部清掉,代码好像还有点逻辑上的问题,主键跟外键一直是一样的.
# 跑的太慢,加个时间的代码




conn.close_conn()