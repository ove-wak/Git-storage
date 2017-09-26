function [IW, Bias, M, beta] = OSELM_increase_study(Data_File,IW, Bias, M, beta, ActivationFunction, times)
% 2017-09-16
% ove-wak
% oselm之增量学习#单AP
% 输入:
% Data_File:增量学习的训练数据所在的文件
% IW:随机生成输入层到隐藏层之间的权值,为前一次结果的输出
% Bias:随机生成隐层节点的偏置参数,为前一次结果的输出
% M:在最终结果中没有含义,是根据数学算式推出在后续增量学习中方便计算的中间值,为前一次结果的输出
% beta:连接隐层节点和输出节点的权值,为前一次结果的输出
% ActivationFunction:隐藏层激活函数类型
% times:增量倍数,默认为1,当中间有nodata的增量时,times++
%
% 输出:
% IW:随机生成输入层到隐藏层之间的权值,一整次增量学习过程中要保持该参数不变,因此传递下去
% Bias:随机生成隐层节点的偏置参数,一整次增量学习过程中要保持该参数不变,因此传递下去
% M:在最终结果中没有含义,是根据数学算式推出在后续增量学习中方便计算的中间值
% beta:连接隐层节点和输出节点的权值,后续增量学习中用到此参数
% 2017-09-17
% 1.可通过输入时效性w的倍数来减除衰减模型的影响,但波动会不会太大?
% 解决方法:将w设置为1-2之间的数.
% 2.目前对于模型衰减采用的方式是直接随机输入晚上的一部分数据,因为输出的是变化系数,也就是使其变化系数越来越趋近一个稳定值

if nargin == 6
    times = 1;
end
train_data=load(Data_File);
T=train_data(:,1); P=train_data(:,2:size(train_data,2));
nTrainingData=size(P,1); 
clear train_data;
switch lower(ActivationFunction)
    case{'rbf'}
        H = RBFun(P,IW,Bias);
    case{'sig'}
        H = SigActFun(P,IW,Bias);
    case{'sin'}
        H = SinActFun(P,IW,Bias);
    case{'hardlim'}
        H = HardlimActFun(P,IW,Bias);
end    
% Y = eye(n) 返回n乘n单一矩阵
% M的求法与原论文中的公式不一样,说白了M=pinv(K)
% 但是尚未验证两种公式的一致性,只能根据训练结果来选择
M = M - M * H' * (eye(nTrainingData) + H * M * H')^(-1) * H * M; 
% K = K + H'* H % K与M,两个中间值根据训练结果优劣选一个
%beta = beta + M * H' * (T - H * beta); %%未增加时效性的结果
w = 1.5;%%%% 使用该语句时要给w初始化
beta = beta + times * w * M * H' * (T - H * beta); 
% beta = beta + times * w * pinv(K) * H' * (T - H * beta); 
clear T P nTrainingData H;
