function [TestingTime,TestingAccuracy] = OSELM_test(Data_File,IW, Bias, beta, ActivationFunction)
% 2017-09-16
% ove-wak
% OSELM_test
% oselm֮����#��AP
% ����:
% Data_File:�����������ڵ��ļ�
% IW:�����������㵽���ز�֮���Ȩֵ,��֮ǰ������л�ȡ
% Bias:�����������ڵ��ƫ�ò���,��֮ǰ������л�ȡ
% beta:��������ڵ������ڵ��Ȩֵ,��֮ǰ������л�ȡ
% ActivationFunction:���ز㼤�������
%
% ���:
% TestingTime:ѵ��ʱ��
% TestingAccuracy:ѵ��Ч�� 

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
TestingAccuracy=sqrt(mse(TV.T - TY)) % ����ĺ���:���������,��rmse=sqrt(sum((TV.T - TY).^2)/n)=sqrt(mse(TV.T - TY))  
