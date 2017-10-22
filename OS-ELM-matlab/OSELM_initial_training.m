function [IW, Bias, M, beta, TrainingTime] = OSELM_initial_training(Data_File, nHiddenNeurons, ActivationFunction)
% 2017-09-16
% ove-wak
% OSELM_initial_training
% oselm֮����ѵ��#��AP
% ����:
% Data_File:����ѵ����ѵ���������ڵ��ļ�
% nHiddenNeurons:���ز���Ԫ����
% ActivationFunction:���ز㼤�������
% ���� nHiddenNeurons ҪС�� Data_File �������ݵ� size 
%
% ���:
% IW:�����������㵽���ز�֮���Ȩֵ,һ��������ѧϰ������Ҫ���ָò�������,��˴�����ȥ
% Bias:�����������ڵ��ƫ�ò���,һ��������ѧϰ������Ҫ���ָò�������,��˴�����ȥ
% M:�����ս����û�к���,�Ǹ�����ѧ��ʽ�Ƴ��ں�������ѧϰ�з��������м�ֵ
% beta:��������ڵ������ڵ��Ȩֵ,��������ѧϰ���õ��˲���
% TrainingTime:ѵ��ʱ��

train_data=load(Data_File);
T0=train_data(:,1); P0=train_data(:,2:size(train_data,2));% T0 Ϊ���, P0Ϊ����,Ŀǰ�������Ϊ������
clear train_data;
nInputNeurons=size(P0,2);
start_time_train=cputime;
IW = rand(nHiddenNeurons,nInputNeurons)*2-1;% �����������㵽���ز�֮���Ȩֵ

switch lower(ActivationFunction)
    case{'rbf'}
        Bias = rand(1,nHiddenNeurons); % ������ѡ����������Լ�����ڵ���Ŀ�����������ڵ��ƫ�ò���
%        Bias = rand(1,nHiddenNeurons)*1/3+1/11;     %%%%%%%%%%%%% for the cases of Image Segment and Satellite Image
%        Bias = rand(1,nHiddenNeurons)*1/20+1/60;    %%%%%%%%%%%%% for the case of DNA
        H0 = RBFun(P0,IW,Bias); % H0��ʾ����ڵ�����
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

% pinv(a)����α������������invֻ�ܶԷ������棬pinv(a)���ԶԷǷ������档
% pinv(a)=inv(a'*a)*a'
M = pinv(H0' * H0); % M �����ս����û�к���,�Ǹ�����ѧ��ʽ�Ƴ��ں�������ѧϰ�з��������м�ֵ
% K = H0' * H0; % K��M,�����м�ֵ����ѵ���������ѡһ��
beta = pinv(H0) * T0; % betaΪ��������ڵ������ڵ��Ȩֵ,elm��Ҫ����ѵ���˲���,������С���˷�,�˴������α��
clear P0 T0 H0;
end_time_train=cputime;
TrainingTime = end_time_train-start_time_train;  

