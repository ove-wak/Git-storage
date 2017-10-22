function [TestingTime,TestingAccuracy] = OSELM_test(Data_File,IW, Bias, beta, ActivationFunction)
% 2017-09-16
% ove-wak
% OSELM_test
% oselm之测试#单AP
% 输入:
% Data_File:测试数据所在的文件
% IW:随机生成输入层到隐藏层之间的权值,从之前的输出中获取
% Bias:随机生成隐层节点的偏置参数,从之前的输出中获取
% beta:连接隐层节点和输出节点的权值,从之前的输出中获取
% ActivationFunction:隐藏层激活函数类型
%
% 输出:
% TestingTime:训练时间
% TestingAccuracy:训练效果 

test_data=load(Data_File);
TV.T=test_data(:,1); TV.P=test_data(:,2:size(test_data,2));
clear test_data;
start_time_test=cputime; 
switch lower(ActivationFunction)
    case{'rbf'}
        HTest = RBFun(TV.P, IW, Bias);
    case{'sig'}
        HTest = SigActFun(TV.P, IW, Bias);
    case{'sin'}
        HTest = SinActFun(TV.P, IW, Bias);
    case{'hardlim'}
        HTest = HardlimActFun(TV.P, IW, Bias);
end    
TY=HTest * beta;
clear HTest;
end_time_test=cputime;
TestingTime=end_time_test-start_time_test
TestingAccuracy=sqrt(mse(TV.T - TY)) % 结果的含义:均方根误差,即rmse=sqrt(sum((TV.T - TY).^2)/n)=sqrt(mse(TV.T - TY))  
