function TY = OSELM_get_value(TrainingData_File, TestingData_File, nHiddenNeurons, ActivationFunction, N0, Block)
% 一次性初始并增量直接输出最终结果
% 参数介绍参考 OSELM.m
rand('state',sum(100*clock));
train_data=load(TrainingData_File); test_data=load(TestingData_File);
T=train_data(:,1); P=train_data(:,2:size(train_data,2));
TV.T=test_data(:,1); TV.P=test_data(:,2:size(test_data,2));
clear train_data test_data;

nTrainingData=size(P,1); 
nTestingData=size(TV.P,1);
nInputNeurons=size(P,2);

P0=P(1:N0,:); 
T0=T(1:N0,:);

IW = rand(nHiddenNeurons,nInputNeurons)*2-1;
switch lower(ActivationFunction)
    case{'rbf'}
        Bias = rand(1,nHiddenNeurons);
%        Bias = rand(1,nHiddenNeurons)*1/3+1/11;     %%%%%%%%%%%%% for the cases of Image Segment and Satellite Image
%        Bias = rand(1,nHiddenNeurons)*1/20+1/60;    %%%%%%%%%%%%% for the case of DNA
        H0 = RBFun(P0,IW,Bias);
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

M = pinv(H0' * H0);
beta = pinv(H0) * T0;
clear P0 T0 H0;

%%%%%%%%%%%%% step 2 Sequential Learning Phase
for n = N0 : Block : nTrainingData
    if (n+Block-1) > nTrainingData
        Pn = P(n:nTrainingData,:);    Tn = T(n:nTrainingData,:);
        Block = size(Pn,1);             %%%% correct the block size
        clear V;                        %%%% correct the first dimention of V 
    else
        Pn = P(n:(n+Block-1),:);    Tn = T(n:(n+Block-1),:);
    end
    
    switch lower(ActivationFunction)
        case{'rbf'}
            H = RBFun(Pn,IW,Bias);
        case{'sig'}
            H = SigActFun(Pn,IW,Bias);
        case{'sin'}
            H = SinActFun(Pn,IW,Bias);
        case{'hardlim'}
            H = HardlimActFun(Pn,IW,Bias);
    end    
    M = M - M * H' * (eye(Block) + H * M * H')^(-1) * H * M; 
    beta = beta + M * H' * (Tn - H * beta); 
end   
clear Pn Tn H M;

switch lower(ActivationFunction)
    case{'rbf'}
        HTrain = RBFun(P, IW, Bias);
    case{'sig'}
        HTrain = SigActFun(P, IW, Bias);
    case{'sin'}
        HTrain = SinActFun(P, IW, Bias);
    case{'hardlim'}
        HTrain = HardlimActFun(P, IW, Bias);
end
Y=HTrain * beta;
clear HTrain;

%%%%%%%%%%% Performance Evaluation
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
