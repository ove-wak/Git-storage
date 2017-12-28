function TY = OSELM_get_value(TrainingData_File, TestingData_File, nHiddenNeurons, ActivationFunction, N0, Block)
% Usage: OSELM(TrainingData_File, TestingData_File, Elm_Type, NumberofHiddenNeurons, ActivationFunction, N0, Block)
% OR:    [TrainingTime, TestingTime, TrainingAccuracy, TestingAccuracy] = OSELM(TrainingData_File, TestingData_File, Elm_Type, NumberofHiddenNeurons, ActivationFunction, N0, Block)
%
% Input:
% TrainingData_File     - Filename of training data set
% TestingData_File      - Filename of testing data set
% Elm_Type              - 0 for regression; 1 for (both binary and multi-classes) classification
% nHiddenNeurons        - Number of hidden neurons assigned to the OSELM
% ActivationFunction    - Type of activation function:
%                           'rbf' for radial basis function, G(a,b,x) = exp(-b||x-a||^2)
%                           'sig' for sigmoidal function, G(a,b,x) = 1/(1+exp(-(ax+b)))
%                           'sin' for sine function, G(a,b,x) = sin(ax+b)
%                           'hardlim' for hardlim function, G(a,b,x) = hardlim(ax+b)
% N0                    - Number of initial training data used in the initial phase of OSLEM, which is not less than the number of hidden neurons
% Block                 - Size of block of data learned by OSELM in each step
%
% Output: 
% TrainingTime          - Time (seconds) spent on training OSELM
% TestingTime           - Time (seconds) spent on predicting all testing data
% TrainingAccuracy      - Training accuracy: 
%                           RMSE for regression or correct classification rate for classifcation
% TestingAccuracy       - Testing accuracy: 
%                           RMSE for regression or correct classification rate for classifcation
%
% MULTI-CLASSE CLASSIFICATION: NUMBER OF OUTPUT NEURONS WILL BE AUTOMATICALLY SET EQUAL TO NUMBER OF CLASSES
% FOR EXAMPLE, if there are 7 classes in all, there will have 7 output
% neurons; neuron 5 has the highest output means input belongs to 5-th class
%
% Sample1 regression: OSELM('mpg_train', 'mpg_test', 0, 25, 'rbf', 75, 1);
% Sample2 classification: OSELM('segment_train', 'segment_test', 1, 180, 'sig', 280, 20);


%%%%%%%%%%% Load dataset
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
    beta = beta + M * H' * (Tn - H * beta);  %%%%时效性参数可加在该部分
    %beta = beta + w * M * H' * (Tn - H * beta); %%%%使用该语句时要给w初始化
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
