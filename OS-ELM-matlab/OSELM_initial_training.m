function [IW, Bias, M, beta, TrainingTime] = OSELM_initial_training(Data_File, nHiddenNeurons, ActivationFunction)
% 2017-09-16
% ove-wak
% OSELM_initial_training
% oselm之初次训练#单AP
% 输入:
% Data_File:初次训练的训练数据所在的文件
% nHiddenNeurons:隐藏层神经元个数
% ActivationFunction:隐藏层激活函数类型
% 其中 nHiddenNeurons 要小于 Data_File 所含数据的 size 
%
% 输出:
% IW:随机生成输入层到隐藏层之间的权值,一整次增量学习过程中要保持该参数不变,因此传递下去
% Bias:随机生成隐层节点的偏置参数,一整次增量学习过程中要保持该参数不变,因此传递下去
% M:在最终结果中没有含义,是根据数学算式推出在后续增量学习中方便计算的中间值
% beta:连接隐层节点和输出节点的权值,后续增量学习中用到此参数
% TrainingTime:训练时间

train_data=load(Data_File);
T0=train_data(:,1); P0=train_data(:,2:size(train_data,2));% T0 为输出, P0为输入,目前输出仅能为单参数
clear train_data;
nInputNeurons=size(P0,2);
start_time_train=cputime;
IW = rand(nHiddenNeurons,nInputNeurons)*2-1;% 随机生成输入层到隐藏层之间的权值

switch lower(ActivationFunction)
    case{'rbf'}
        Bias = rand(1,nHiddenNeurons); % 根据所选激活函数类型以及隐层节点数目随机生成隐层节点的偏置参数
%        Bias = rand(1,nHiddenNeurons)*1/3+1/11;     %%%%%%%%%%%%% for the cases of Image Segment and Satellite Image
%        Bias = rand(1,nHiddenNeurons)*1/20+1/60;    %%%%%%%%%%%%% for the case of DNA
        H0 = RBFun(P0,IW,Bias); % H0表示隐层节点的输出
    case{'sig'}
        Bias = rand(1,nHiddenNeurons)*2-1;
        H0 = SigActFun(P0,IW,Bias);
    case{'sin'}
        Bias = rand(1,nHiddenNeurons)*2-1;
        H0 = SinActFun(P0,IW,Bias);
    case{'hardlim'}
        Bias = rand(1,nHiddenNeurons)*2-1;
        H0 = HardlimActFun(P0,IW,Bias);
        H0 = double(H0);
end

% pinv(a)是求伪逆矩阵，逆矩阵函数inv只能对方阵求逆，pinv(a)可以对非方阵求逆。
% pinv(a)=inv(a'*a)*a'
M = pinv(H0' * H0); % M 在最终结果中没有含义,是根据数学算式推出在后续增量学习中方便计算的中间值
% K = H0' * H0; % K与M,两个中间值根据训练结果优劣选一个
beta = pinv(H0) * T0; % beta为连接隐层节点和输出节点的权值,elm主要用来训练此参数,基于最小二乘法,此处求的是伪逆
clear P0 T0 H0;
end_time_train=cputime;
TrainingTime = end_time_train-start_time_train;  

