% Gera dados para aproxima��o da s�rie Box-Jenkins

close all;
clear;
clc;

% Carrega dados da s�rie temporal
ts = load('box_jenkins.txt');

nd = size(ts,1); % n�mero de dados
nc = size(ts,2); % n�mero de coordenadas dos dados

X = ts;
Xt = zeros(200, 3);
Xv = zeros(90, 3);

% Dados para treinamento
start = 1;
Xt(:, 1) = X(start:start+200-1,1); % x(t-4)
start = start + 3;
Xt(:, 2) = X(start:start+200-1,2); % y(t-1)
start = start + 1;
Xt(:, 3) = X(start:start+200-1,2); % y(t)

% Dados para  valida��o
start = 203;
Xv(:, 1) = X(start:start+90-1,1); % x(t-4)
start = start + 3;
Xv(:, 2) = X(start:start+90-1,2); % y(t-1)
start = start + 1;
Xv(:, 3) = X(start:start+90-1,2); % y(t)

