function [IW, Bias, M, beta] = OSELM_increase_study(Data_File,IW, Bias, M, beta, ActivationFunction, times)
% 2017-09-16
% ove-wak
% oselm֮����ѧϰ#��AP
% ����:
% Data_File:����ѧϰ��ѵ���������ڵ��ļ�
% IW:�����������㵽���ز�֮���Ȩֵ,Ϊǰһ�ν�������
% Bias:�����������ڵ��ƫ�ò���,Ϊǰһ�ν�������
% M:�����ս����û�к���,�Ǹ�����ѧ��ʽ�Ƴ��ں�������ѧϰ�з��������м�ֵ,Ϊǰһ�ν�������
% beta:��������ڵ������ڵ��Ȩֵ,Ϊǰһ�ν�������
% ActivationFunction:���ز㼤�������
% times:��������,Ĭ��Ϊ1,���м���nodata������ʱ,times++
%
% ���:
% IW:�����������㵽���ز�֮���Ȩֵ,һ��������ѧϰ������Ҫ���ָò�������,��˴�����ȥ
% Bias:�����������ڵ��ƫ�ò���,һ��������ѧϰ������Ҫ���ָò�������,��˴�����ȥ
% M:�����ս����û�к���,�Ǹ�����ѧ��ʽ�Ƴ��ں�������ѧϰ�з��������м�ֵ
% beta:��������ڵ������ڵ��Ȩֵ,��������ѧϰ���õ��˲���
% 2017-09-17
% 1.��ͨ������ʱЧ��w�ı���������˥��ģ�͵�Ӱ��,�������᲻��̫��?
% �������:��w����Ϊ1-2֮�����.
% 2.Ŀǰ����ģ��˥�����õķ�ʽ��ֱ������������ϵ�һ��������,��Ϊ������Ǳ仯ϵ��,Ҳ����ʹ��仯ϵ��Խ��Խ����һ���ȶ�ֵ

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
% Y = eye(n) ����n��n��һ����
% M������ԭ�����еĹ�ʽ��һ��,˵����M=pinv(K)
% ������δ��֤���ֹ�ʽ��һ����,ֻ�ܸ���ѵ�������ѡ��
M = M - M * H' * (eye(nTrainingData) + H * M * H')^(-1) * H * M; 
% K = K + H'* H % K��M,�����м�ֵ����ѵ���������ѡһ��
%beta = beta + M * H' * (T - H * beta); %%δ����ʱЧ�ԵĽ��
w = 1.5;%%%% ʹ�ø����ʱҪ��w��ʼ��
beta = beta + times * w * M * H' * (T - H * beta); 
% beta = beta + times * w * pinv(K) * H' * (T - H * beta); 
clear T P nTrainingData H;
