import os,csv,time

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
    x = int(room.split("_")[1])
    y = int(room.split("_")[2])
    files = os.listdir("Wi-Fi_Data/"+room)
    if len(files) > x*y:
        print(room+"  error")
        break
    else:
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
        print(quanfile)
        print(timed)
        for q in quandata:
            # print(q)
            if flag < len(timed) and timed[flag] in q:
                flag = flag + 1
                locd.append([q[3],q[4]])
        print(len(timed))
        print(len(locd))
        print(locd)




    # file_name = str(i+1).zfill(5)+"_"+str(round(temp_x,3))+"_"+str(round(temp_y,3))+".csv"
    # os.rename("Wi-Fi_Data/"+room+"/"+files[i],"Wi-Fi_Data/"+room+"/"+file_name)

