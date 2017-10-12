import tensorflow as tf
import threading
import numpy as np
import generate_RSS
# import draw_3D
# import time

with tf.device("/CPU:0"):  # 机器中的CPU
    LOC_D = 2  # 空间维度

    X_SIZE = 21
    Y_SIZE = 21
    AP_NUM = 20  # AP数目

    RSS_AND_RSS_T = generate_RSS.generate_rss(X_SIZE, Y_SIZE, AP_NUM)  # 数据生成

    RSS_NIGHT = RSS_AND_RSS_T[0]  # 晚上数据
    RSS_DAY = RSS_AND_RSS_T[1]  # 白天数据（加障碍）
    RSS_ = RSS_AND_RSS_T[2]  # 10lg(RSS_) = RSS_NIGHT
    Influence = RSS_AND_RSS_T[3]  # 10lg(RSS_*Influence) = RSS_DAY 即变化系数
    # RSS生成结束-----------------------------------------------------------------------------------------------
    # RSS[行][列][AP序号] 在[-1,1]------------------------------------------------------------------------------

    # 定义输入输出维度
    inD = AP_NUM + LOC_D
    outD = 1

    # 定义隐藏层（N=LN+1）层数与节点数
    LN = 2
    HD = [61, 30, 11, 8, 8]  # ??

    # 学习率
    global_step = tf.Variable(0)
    learning_rate = tf.train.exponential_decay(
        0.1, global_step, 1000, 0.99, staircase=True
    )
    # 设定最大训练轮数
    STEPS = 2000000

    # 正则化系数
    lam = 0.0001

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
    X = [[0.0 for i in range(inD)] for j in range(Train_Num)]
    Y = [[0.0 for i in range(outD)] for j in range(Train_Num)]

    # 测试输入
    T = [[0.0 for i in range(inD)] for j in range(Test_NUM)]
    Y_ = [[0.0 for i in range(outD)] for j in range(Test_NUM)]

    IC = [[0.0 for i in range(inD)] for j in range(X_SIZE * Y_SIZE)]  # 转换前数据
    OC_NIGHT = [[0.0 for i in range(outD)] for j in range(X_SIZE * Y_SIZE)]  # 转换前数据（部分AP）
    OC_DAY = [[0.0 for i in range(outD)] for j in range(X_SIZE * Y_SIZE)]  # 转换后数据（部分AP）

    OC_TRAINED_LOCAL = [[0.0 for i in range(outD)] for j in range(X_SIZE * Y_SIZE)]  # 部分区域变换
    OC_TRAINED_GLOBAL = [[0.0 for i in range(outD)] for j in range(X_SIZE * Y_SIZE)]  # 全部区域变换
    ii = [[0.0 for i in range(outD)] for j in range(X_SIZE * Y_SIZE)]  # 所有AP的影响系数
    ii1 = [[0.5 for i in range(outD)] for j in range(X_SIZE * Y_SIZE)]  # 所有AP的影响系数

    for x in range(X_SIZE):
        for y in range(Y_SIZE):
            i = x * X_SIZE + y
            for a in range(AP_NUM):
                IC[i][a] = RSS_NIGHT[x][y][a]
            IC[i][inD - 2] = float(x)
            IC[i][inD - 1] = float(y)
            OC_NIGHT[i][0] = RSS_NIGHT[x][y][1]
            OC_DAY[i][0] = RSS_DAY[x][y][1]
            ii[i][0] = Influence[x][y][1] - 0.5

    center_x = 15.0
    center_y = 15.0
    r = 6
    test_set_index = -1
    train_set_index = -1
    for x in range(X_SIZE):
        for y in range(Y_SIZE):
            if (np.square(x-center_x)+np.square(center_y-y)) <= np.square(r):   # 局部圆形区域内部
                i = x * Y_SIZE + y
                if (i + 1) % denominator:  # 非denominator的整数倍 加入训练集
                    train_set_index += 1
                    # print(train_set_index)
                    # print('train %d\n'% i )
                    for a in range(AP_NUM):
                        X[train_set_index][a] = RSS_NIGHT[x][y][a]
                    X[train_set_index][inD - 2] = float(x)
                    X[train_set_index][inD - 1] = float(y)
                    Y[train_set_index][0] = Influence[x][y][1] - 0.5
                else:  # denominator的整数倍 加入测试集
                    test_set_index += 1
                    # print(test_set_index)
                    # print('test %d\n' % i)
                    for a in range(AP_NUM):
                        T[test_set_index][a] = RSS_NIGHT[x][y][a]
                    T[test_set_index][inD - 2] = float(x)
                    T[test_set_index][inD - 1] = float(y)
                    Y_[test_set_index][0] = Influence[x][y][1] - 0.5
    local_sample_num = test_set_index + train_set_index + 2
    OC_NIGHT_LOCAL_ONLY = [[0.0 for i in range(outD)] for j in range(local_sample_num)]  # 仅包含局部区域
    OC_DAY_LOCAL_ONLY = [[0.0 for i in range(outD)] for j in range(local_sample_num)] # 仅包含局部区域
    OC_TRAINED_LOCAL_ONLY = [[0.0 for i in range(outD)] for j in range(local_sample_num)]  # 仅包含局部区域
    i0 = 0
    for x in range(X_SIZE):
        for y in range(Y_SIZE):
            if (np.square(x - center_x) + np.square(center_y - y)) <= np.square(r):  # 局部圆形区域内部
                a = 1
                OC_NIGHT_LOCAL_ONLY[i0][0] = RSS_NIGHT[x][y][a]
                OC_DAY_LOCAL_ONLY[i0][0] = RSS_DAY[x][y][a]
                i0 += 1

    global u_break
    u_break = 0


    def user_break():
        raw_input_ = input("enter to break")
        global u_break
        u_break = 1
        return


    t1 = threading.Thread(target=user_break)
    t1.setDaemon(True)
    t1.start()

    # 定义神经网络参数
    w = [tf.Variable(tf.random_normal([inD, HD[0]], stddev=1, seed=1))]

    tf.add_to_collection('losses', tf.contrib.layers.l2_regularizer(lam)(w[0]))
    if LN > 0:
        for _ in range(1, LN + 1):
            w.append(tf.Variable(tf.random_normal([HD[_ - 1], HD[_]], stddev=1, seed=1 + _)))
            tf.add_to_collection('losses', tf.contrib.layers.l2_regularizer(lam)(w[_]))
    w.append(tf.Variable(tf.random_normal([HD[LN], outD], stddev=1, seed=LN + 1)))
    tf.add_to_collection('losses', tf.contrib.layers.l2_regularizer(lam)(w[LN + 1]))

    # 偏置值
    biases = [tf.Variable(tf.constant(0.1, shape=[HD[0]]))]
    if LN > 0:
        for _ in range(1, LN + 1):
            biases.append(tf.Variable(tf.constant(0.1, shape=[HD[_]])))
    biases.append(tf.Variable(tf.constant(0.1, shape=[outD])))

    # 输入数据
    inputData = tf.placeholder(tf.float32, shape=(None, inD), name='x-input')
    outputData = tf.placeholder(tf.float32, shape=(None, outD), name='y-input')

    testData = tf.placeholder(tf.float32, shape=(None, inD), name='t-input')

    data_before_transfer = tf.placeholder(tf.float32, shape=(None, outD), name='b-input')
    data_after_transfer = tf.placeholder(tf.float32, shape=(None, outD), name='a-input')

    # 定义神经网络前向传播过程

    # ''' 非线性激活函数 正向传播
    layer = [tf.nn.tanh(tf.matmul(inputData, w[0]) + biases[0])]
    if LN > 0:
        for _ in range(1, LN + 1):
            layer.append(tf.nn.tanh(tf.matmul(layer[_ - 1], w[_]) + biases[_]))
    layer.append(tf.nn.tanh(tf.matmul(layer[LN], w[LN + 1]) + biases[LN + 1]))
    # '''

    # 交叉熵
    cross_entropy = -tf.reduce_mean(
        outputData * tf.log(tf.clip_by_value(layer[LN + 1], 1e-10, 1.0))
    )

    # 方差
    mse = tf.reduce_mean(tf.square(outputData - layer[LN + 1]))
    mse_ = tf.reduce_mean(tf.square(data_before_transfer - data_after_transfer))

    tf.add_to_collection('losses', mse)

    loss = tf.add_n(tf.get_collection('losses'))
    # loss= mse
    # train_step = tf.train.AdadeltaOptimizer().minimize(loss)
    train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss, global_step=global_step)
    # 创建会话运行TensorFlow程序
    with tf.Session() as sess:
        last_loss = 0  # 记录上一次loss
        no_impro = 0
        init_op = tf.global_variables_initializer()
        # 初始化变量
        sess.run(init_op)
        '''
        for _ in range(LN + 2):
            print("第%d层参数" % _)
            print(sess.run(w[_]))
            print("第%d层偏置值" % _)
            print(sess.run(biases[_]))
            print("\n")
        '''
        # time0 = time.time()
        for i in range(STEPS):
            # 每次选取batch_size个样本进行训练
            # start = (i * batch_size) % Train_Num
            # end = min(start + batch_size, Train_Num)
            start = 0
            end = batch_size
            # 通过选取的样本训练神经网络并更新参数
            sess.run(
                train_step,
                feed_dict={inputData: X[start:end], outputData: Y[start:end]}
            )
            if i % 1000 == 0:
                # 每隔一段时间计算所有数据的交叉熵并输出
                total_loss = sess.run(
                    loss,
                    feed_dict={inputData: X, outputData: Y}
                )
                mse_total = sess.run(
                    mse,
                    feed_dict={inputData: X, outputData: Y}
                )

                print("%d steps, loss:%g ,\t mse:%g" % (i, total_loss, mse_total))
                # print("TIME per step %g"%((time.time()-time0)/(i+1)))
                # '''
                if np.abs(last_loss - total_loss) < 0.00000005:
                    no_impro += 1
                    # print("enough accuracy")
                    if no_impro > 5:
                        break
                else:
                    no_impro = 0
                # '''
                last_loss = total_loss
                if u_break == 1:
                    # print("current learning rate %f" %(learning_rate))
                    break

        print("\n\n")
        '''
        for _ in range(LN + 2):
            print("第%d层参数" % _)
            print(sess.run(w[_]))
            print("第%d层偏置值" % _)
            print(sess.run(biases[_]))
            print("\n")
        '''
        result_global = sess.run(   # 全体拟合结果 训练集+测试集
            layer[LN + 1],
            feed_dict={inputData: IC}
        )

        Influence_T_LOCAL = [[[1.0 for i in range(AP_NUM)] for i in range(Y_SIZE)] for j in range(X_SIZE)]
        Influence_T_GLOBAL = [[[1.0 for i in range(AP_NUM)] for i in range(Y_SIZE)] for j in range(X_SIZE)]

        for i in range(X_SIZE*Y_SIZE):
            x = int(i/X_SIZE)
            y = i % X_SIZE
            Influence_T_GLOBAL[x][y][1] = result_global[i][0]+0.5                    # 更新全部值
            if (np.square(x - center_x) + np.square(center_y - y)) <= np.square(r):  # 只更新内部的值
                Influence_T_LOCAL[int(x)][int(y)][1] = result_global[i][0] + 0.5
        print()

        for x in range(X_SIZE):
            for y in range(Y_SIZE):
                if (np.square(x - center_x) + np.square(center_y - y)) <= np.square(r):  # 标记局部
                    print('%8fL' % (Influence_T_LOCAL[x][y][1] - 0.5), end='\t')
                else:
                    print('%8f' % (Influence_T_LOCAL[x][y][1] - 0.5), end='\t')
            print()
        print()
        print()
        for x in range(X_SIZE):
            for y in range(Y_SIZE):
                if (np.square(x - center_x) + np.square(center_y - y)) <= np.square(r):  # 标记局部
                    print('%8fL' % (Influence[x][y][1] - 0.5), end='\t')
                else:
                    print('%8f' % (Influence[x][y][1] - 0.5), end='\t')
            print()
        print()
        print()
        for x in range(X_SIZE):
            for y in range(Y_SIZE):
                if (np.square(x - center_x) + np.square(center_y - y)) <= np.square(r):  # 标记局部
                    print('%8fL' % (Influence_T_GLOBAL[x][y][1] - 0.5), end='\t')
                else:
                    print('%8f' % (Influence_T_GLOBAL[x][y][1] - 0.5), end='\t')
            print()

        RSS_LOCAL = [[[0.0 for i in range(AP_NUM)] for j in range(Y_SIZE)] for k in range(X_SIZE)]
        RSS_GLOBAL = [[[0.0 for i in range(AP_NUM)] for j in range(Y_SIZE)] for k in range(X_SIZE)]

        for x in range(X_SIZE):
            for y in range(Y_SIZE):
                sig = RSS_[x][y][1] * Influence_T_LOCAL[x][y][1]
                sig0 = RSS_[x][y][1] * Influence_T_GLOBAL[x][y][1]
                if sig > 0.0:
                    RSS_LOCAL[x][y][1] = np.log10(sig) * 10
                if sig0 > 0.0:
                    RSS_GLOBAL[x][y][1] = np.log10(sig0) * 10

        i0 = 0
        for x in range(X_SIZE):
            for y in range(Y_SIZE):
                i = x * X_SIZE + y
                OC_TRAINED_LOCAL[i][0] = RSS_LOCAL[x][y][1] / -100.0
                OC_TRAINED_GLOBAL[i][0] = RSS_GLOBAL[x][y][1] / -100.0
                if (np.square(x - center_x) + np.square(center_y - y)) <= np.square(r):
                    OC_TRAINED_LOCAL_ONLY[i0][0] = RSS_LOCAL[x][y][1] / -100.0
                    i0 += 1

        m = sess.run(
            mse_,
            feed_dict={data_before_transfer: OC_NIGHT, data_after_transfer: OC_DAY}
        )
        print("Original global mse on all data is %g" % m)

        m0 = sess.run(
            mse_,
            feed_dict={data_before_transfer: OC_NIGHT_LOCAL_ONLY, data_after_transfer: OC_DAY_LOCAL_ONLY}
        )
        print("Original local mse on all data is %g" % m0)

        ml = sess.run(
            mse_,
            feed_dict={data_before_transfer: OC_TRAINED_LOCAL_ONLY, data_after_transfer: OC_DAY_LOCAL_ONLY}
        )
        print("Trained local mse on all data is %g" % ml)

        m1 = sess.run(
            mse_,
            feed_dict={data_before_transfer: OC_TRAINED_LOCAL, data_after_transfer: OC_DAY}
        )
        print("Local trained and local adjust mse on all data is %g" % m1)

        m2 = sess.run(
            mse_,
            feed_dict={data_before_transfer: OC_TRAINED_GLOBAL, data_after_transfer: OC_DAY}
        )
        print("Local trained and global adjust mse on all data is %g" % m2)

        # draw_3D.draw_3D(Influence, X_SIZE, Y_SIZE)
        # draw_3D.draw_3D(Influence_T_LOCAL, X_SIZE, Y_SIZE)
        # draw_3D.draw_3D(Influence_T_GLOBAL, X_SIZE, Y_SIZE)

        for x in range(X_SIZE):
            for y in range(Y_SIZE):
                for a in range(AP_NUM):
                    RSS_DAY[x][y][a] = RSS_DAY[x][y][a] * -100.0
        for x in range(X_SIZE):
            for y in range(Y_SIZE):
                for a in range(AP_NUM):
                    RSS_NIGHT[x][y][a] = RSS_NIGHT[x][y][a] * -100.0

        # draw_3D.draw_3D(RSS_DAY, X_SIZE, Y_SIZE)
        # draw_3D.draw_3D(RSS_LOCAL, X_SIZE, Y_SIZE)
        # draw_3D.draw_3D(RSS_NIGHT, X_SIZE, Y_SIZE)
