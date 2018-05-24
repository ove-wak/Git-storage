import xlrd,os,time,numpy

point = ""

while point != "00000":
    room = input("房间号:")
    point_y = float(input("控制点N:"))
    point_x = float(input("控制点E:"))
    x_1 = float(input("1号点x:")) # 此处的x对应地图的E
    y_1 = float(input("1号点y:")) # 此处的y对应地图的N
    x_2 = float(input("2号点x:"))
    y_2 = float(input("2号点y:"))
    direc = input("方向:") # 输入'+'或者'-'
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
        temp_x = 0.0
        temp_y = 0.0
        direc_t = ""
        temp_d = ""
        temp_d_t = 0.0
        for i in range(len(files)):
            if i == 0:
                temp_x = point_x + x_1
                temp_y = point_y + y_1
            elif i == 1:
                temp_x = temp_x + x_2
                temp_y = temp_y + y_2
                if abs(x_2 - 0) < 0.1:
                    direc_t = "x"
                    temp_d_t = abs(y_2)
                    if y_2 > 0:
                        temp_d = "+"
                    else:
                        temp_d = "-"
                else:
                    direc_t = "y"
                    temp_d_t = abs(x_2)
                    if x_2 >0:
                        temp_d = "+"
                    else:
                        temp_d = "-"
            else:
                if i % x == 0:
                    if direc == "+":
                        if direc_t == "x":
                            x_t = temp_d_t
                            y_t = 0
                        else:
                            x_t = 0
                            y_t = temp_d_t
                    else:
                        if direc_t == "x":
                            x_t = 0 - temp_d_t
                            y_t = 0
                        else:
                            x_t = 0
                            y_t = 0 - temp_d_t
                else:
                    if direc_t == "x":
                        x_t = 0
                        if (i//x) % 2 == 0:
                            if temp_d == "+":
                                y_t = temp_d_t
                            else:
                                y_t = 0 - temp_d_t
                        else:
                            if temp_d == "+":
                                y_t = 0 - temp_d_t
                            else:
                                y_t = temp_d_t
                    else:
                        y_t = 0 
                        if (i//x) % 2 == 0:
                            if temp_d == "+":
                                x_t = temp_d_t
                            else:
                                x_t = 0 - temp_d_t
                        else:
                            if temp_d == "+":
                                x_t = 0 - temp_d_t
                            else:
                                x_t = temp_d_t
                temp_x = temp_x + x_t
                temp_y = temp_y + y_t

            file_name = str(i+1).zfill(5)+"_"+str(round(temp_x,3))+"_"+str(round(temp_y,3))+".csv"
            os.rename("Wi-Fi_Data/"+room+"/"+files[i],"Wi-Fi_Data/"+room+"/"+file_name)

