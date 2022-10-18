% Gera dados para classifica��o de dados com a base de dados BCW

close all;
clear;
clc;

% Carrega a base de dados
load 'breast_cancer_wisconsin_data.txt' -ASCII;

% Separa padr�es em vetores X e Y
X = breast_cancer_wisconsin_data(:,1:10); % padr�es
Y = breast_cancer_wisconsin_data(:,11); % r�tulos das classes

% Troca r�tulos 2 e 4 por 0 e 1
for (i = 1 : size(Y,1))
    if (Y(i) == 2)
        Y(i) = 0;
    end
    if (Y(i) == 4)
        Y(i) = 1;
    end
end

nc1 = 458; % n�mero de padr�es da classe 0
nc2 = 241; % n�mero de padr�es da classe 1
nc = nc1 + nc2;

idc = randperm(nc); % �ndices permutados aleatoriamente
X = X(idc,:); % dados de entrada distribuidos randomicamente
Y = Y(idc); % dados de sa�da distribuidos randomicamente

% Dados de treinamento
Xt = [X(idc(1:round(0.8*end)),:) Y(idc(1:round(0.8*end)))];
% Dados de valida��o
Xv = [X(idc(round(0.8*end)+1:end),:) Y(idc(round(0.8*end)+1:end))];
