function [IW, Bias, M_less, beta_less] = OSELM_increase_study_nodata(Data_File,IW, Bias, M, beta, ActivationFunction)
% Ŀǰnodataʱֱ������������ϵ�����
% ��˸÷�����OSELM_increase_study��ʱһ��
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
M_less = M - M * H' * (eye(nTrainingData) + H * M * H')^(-1) * H * M; %%?
beta_less = beta + M_less * H' * (T - H * beta);
%betaless = beta + w * M * H' * (T - H * beta); %%%%ʹ�ø����ʱҪ��w��ʼ��
clear T P nTrainingData H;
%%�������Ϊ��,ģ��˥��,˥���������ֲ�����Ⱑ,M��beta���Զ�������μ�
%%ֱ���������ϵ����ݿɲ�����??