% Gera dados da fun��o para treinamento e valida��o

clear;
close all;
clc;

% gera fun��es
x = 0 : 0.01 : 2*pi;
f1 = sin(x);
f2 = cos(x);
f3 = x;
a = [-pi 0.565 2.657 0.674];
F = a(1) + a(2)*f1 + a(3)*f2 + a(4)*f3;

% �ndices permutados randomicamente
idc = randperm(size(x,2));

% �ndice de treinamento
idc_t = sort(idc(1:round(size(x,2)*0.8)));

% �ndice de valida��o
idc_v = sort(idc(round(size(x,2)*0.8)+1:end));

% dados de treinamento
xt = [f1(idc_t)' f2(idc_t)' f3(idc_t)' F(idc_t)'];

% dados de valida��o
xv = [f1(idc_v)' f2(idc_v)' f3(idc_v)' F(idc_v)'];

figure
%subplot(2,1,1);
plot(xt(:,4));
%legend('yt');
%subplot(2,1,2);
%plot(xv(:,4),'r');
%legend('yv');

