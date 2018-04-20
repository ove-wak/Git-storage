import csv
tt_time = []
with open('time.csv', 'r') as file_read:
            while True:
                lines = file_read.readline() # 读取整行数据
                if not lines:
                    break
                tt_time.append(lines.split("\n")[0].split(","))
tt_time = tt_time[0:-1]
print(tt_time)