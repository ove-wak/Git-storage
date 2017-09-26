function [IW, Bias, M_less, beta_less] = OSELM_increase_study_nodata(Data_File,IW, Bias, M, beta, ActivationFunction)
% 目前nodata时直接随机输入晚上的数据
% 因此该方法与OSELM_increase_study暂时一样
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
%betaless = beta + w * M * H' * (T - H * beta); %%%%使用该语句时要给w初始化
clear T P nTrainingData H;
%%如果输入为空,模型衰减,衰减这两个字不好理解啊,M跟beta的自动减改如何减
%%直接输入晚上的数据可不可以??