%Samp3_5
clf     %清除图形框的内容
N=100;dt=1;   %设置最大点数
n=0:N-1; t=n*dt;   %给出时间序列
xn=cos(2*pi*0.24*t)+cos(2*pi*0.26*t);  %给出原始信号的值序列
Xk=dfs(xn,N);      %对原始信号进行Fourier变换
magXk=abs(Xk);phaXk=angle(Xk);   %求出Fourier变换的振幅和相位
subplot(2,2,1),plot(t,xn); xlabel('时间/s')  %绘出原始信号
title('原始信号(N=100)');
xx=idfs(Xk,N);      %Fourier逆变换
x=real(xx);         %取变换后的实部，如做实验可以验证其虚部为零
subplot(2,2,2),plot(t,x),xlabel('时间/s'),title('运用Fourier逆变换得到的合成信号')
k=0:length(magXk)-1;
subplot(2,1,2),plot(k/(N*dt),magXk*2/N); %绘出Fourier变换的振幅谱，频率采用（3-17）
%采用真实振幅[（3-23）式]绘图
xlabel('频率/Hz');ylabel('振幅');
title(' X(k)振幅(N=100)');
