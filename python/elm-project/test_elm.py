from hpelm import ELM
import numpy as np
import generate_RSS
import matplotlib.pyplot as plt

LOC_D = 2  # 空间维度
X_SIZE = 21
Y_SIZE = 21
AP_NUM = 20  # AP数目

# 定义输入输出维度
inD = AP_NUM + LOC_D
outD = 1

RSS_AND_RSS_T = generate_RSS.generate_rss(X_SIZE, Y_SIZE, AP_NUM)  # 数据生成
RSS_NIGHT = RSS_AND_RSS_T[0]  # 晚上数据
RSS_DAY = RSS_AND_RSS_T[1]  # 白天数据（加障碍）
RSS_ = RSS_AND_RSS_T[2]  # 10lg(RSS_) = RSS_NIGHT
Influence = RSS_AND_RSS_T[3]  # 10lg(RSS_*Influence) = RSS_DAY 即变化系数
# RSS生成结束-----------------------------------------------------------------------------------------------
# RSS[行][列][AP序号] 在[-1,1]------------------------------------------------------------------------------

# 训练数据 占 总数的 1-1/denominator
denominator = 2
# 总数据数目
dataset_size = int(X_SIZE * Y_SIZE)
# 测试集数目
Test_NUM = int(X_SIZE * Y_SIZE / denominator)
# 训练集数目
Train_Num = X_SIZE * Y_SIZE - Test_NUM
# 训练数据batch大小,即每次训练输入的数据量
batch_size = int(float(Train_Num))  # 暂设为与训练集同样大小

# 训练输入
X = np.array([[0.0 for i in range(inD)] for j in range(Train_Num)])
Y = np.array([[0.0 for i in range(outD)] for j in range(Train_Num)])

# 测试输入
T = np.array([[0.0 for i in range(inD)] for j in range(Test_NUM)])
Y_ = np.array([[0.0 for i in range(outD)] for j in range(Test_NUM)])

test_set_index = -1
train_set_index = -1
for x in range(X_SIZE):
    for y in range(Y_SIZE):
        i = x * Y_SIZE + y
        if (i + 1) % denominator:  # 非denominator的整数倍 加入训练集
            train_set_index += 1
            for a in range(AP_NUM):
                X[train_set_index][a] = RSS_NIGHT[x][y][a]
            X[train_set_index][inD - 2] = float(x)
            X[train_set_index][inD - 1] = float(y)
            Y[train_set_index][0] = Influence[x][y][1] - 0.5
        else:  # denominator的整数倍 加入测试集
            test_set_index += 1
            for a in range(AP_NUM):
                T[test_set_index][a] = RSS_NIGHT[x][y][a]
            T[test_set_index][inD - 2] = float(x)
            T[test_set_index][inD - 1] = float(y)
            Y_[test_set_index][0] = Influence[x][y][1] - 0.5
elm = ELM(inD, outD)
elm.add_neurons(50, "tanh")
# elm.add_neurons(50, "rbf_l1")
elm.train(X, Y)  # elm需要输入nparray的数组
yt = elm.predict(T)
print(np.std(yt-Y_))
yt = yt.tolist()
Y_ = Y_.tolist()
error = [Y_[i][0] - yt[i][0] for i in range(len(Y_))]
# print(error)
print("influence")
print(Y)
# for i in range(len(Y_)):
#     print(Y_[i], "   ", yt[i], "   ", Y_[i] - yt[i])
# plt.figure("hist")
# n, bins, patches = plt.hist(error, bins=220, normed=0, histtype='bar', edgecolor='None', facecolor='red')
# plt.show()
