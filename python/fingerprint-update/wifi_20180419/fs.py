class Fs:
    x = 0
    y = 0
    data = []

    def __init__(self, x, y, data):
        self.x = x
        self.y = y
        self.data = data

    def show_info(self):
        print(self.x, ' ', self.y, ' ')
        for i in range(len(self.data)):
            temp = self.data[i]
            for j in range(len(temp)-1):
                print(temp[j], end=',')
            print(temp[len(temp)-1])


def history_match(history_data, current_data):
    m = []
    print('history data')
    for ii in range(len(history_data)):
        temp_ = history_data[ii]
        temp_.show_info()
    print('\ncurrent data')
    for ii in range(len(current_data)):
        temp_ = current_data[ii]
        temp_.show_info()

    aa = [[-99, -61, -19], [-14, -65, -16]]
    bb = [[-98, -99, -99], [-14, -65, -16]]
    fs = Fs(2, 3, aa)
    fs.show_info()
    m.append(fs)
    fs = Fs(3, 3, bb)
    fs.show_info()
    m.append(fs)

    return m


a = [[-13, -62, -19], [-15, -15, -16]]
b = [[-12, -77, -20], [-16, -25, -16]]
c = [[-11, -93, -21], [-17, -35, -16]]
d = [[-16, -21, -22], [-18, -45, -16]]
e = [[-17, -32, -23], [-19, -55, -16]]

hi = []
cu = []

hi.append(Fs(1, 1, a))
hi.append(Fs(1, 2, b))
hi.append(Fs(1, 3, c))

cu.append(Fs(1, 1, d))
cu.append(Fs(1, 2, e))

matched_data = history_match(hi, cu)
print('\nmatched_result')
for i in range(len(matched_data)):
    temp = matched_data[i]
    temp.show_info()




