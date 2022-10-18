function [ z ] = takagi_sugeno_1(x)
% _____________________________ takagi_sugeno_1 _______________________________
% Implementação do sistema de inferência fuzzy tipo Takagi-Sugeno para 1 entrada
% (baseado no exemplo 4.3 do livro Neuro-fuzzy and Soft Computing)
%
% (c) Prof. Maurílio J. Inácio 2017
% Eng. de Computação / FACIT
%
% [ z ] = takagi_sugeno_1(x)
%
% z = saida do sistema
% x = variável de entrada
%
% Implementado em MATLAB ver. R2016a
%
% Parametros das funcoes de pertinencia dos antecedentes
A1 = [1.315 1.6]; % pequeno
A2 = [0.89 3.146]; % medio
A3 = [1 4.342]; % meioalto
A4 = [0.3764 6.63]; %alto
% Fuzzyficacao
pA1 = gaussmf(x, A1); % pertinencia na funcao A1
pA2 = gaussmf(x, A2); % pertinencia na funcao A2
pA3 = gaussmf(x, A3); % pertinencia na funcao A3
pA4 = gaussmf(x, A4); %pertinencia na funcao A4
% Calculo das regras fuzzy (operador produto)
% regra 1: Se X eh pequeno entao Z eh alto
w1 = pA1; % forca de disparo da regra 1
z1 = 1; % constante do consequente 1
% regra 2: Se X eh medio entao Z eh zero
w2 = pA2; % forca de disparo da regra 2
z2 = 0; % constante do consequente 2
% regra 3: Se X eh meioalto entao Z eh negativo
w3 = pA3; % forca de disparo da regra 3
z3 = -0.2172; % constante do consequente 3
% regra 4: Se X eh alto entao Z eh zero
w4 = pA4;
z4 = 0;
% Defuzzyficacao
z = (w1*z1 + w2*z2 + w3*z3 + w4*z4) / (w1 + w2 + w3 + w4); % saida

