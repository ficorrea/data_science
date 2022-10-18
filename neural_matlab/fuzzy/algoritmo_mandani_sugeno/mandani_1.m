function [ y ] = mandani_1(x)
% ______________________________ mandani_1 _______________________________
% Implementação do sistema de inferencia fuzzy tipo Mandani para 1 entrada
%(baseado no exemplo 4.1 do livro Neuro-fuzzy and Soft Computing)
%
% (c) Prof. Maurílio J. Inácio 2017
% Eng. de Computação / FACIT
%
% [ y ] = mandani_1(x)
%
% y = saida do sistema
% x = variável de entrada
%
% % Implementado em MATLAB ver. 2016a
%
% Parametros das funcoes de pertinencia dos antecedentes
A1 = [1.282 0.741]; % pequeno
A2 = [0.7771 3.31]; % medio
A3 = [1.147 4.67]; % meiogrande
A4 = [0.05584 6.15]; % grande
% Parametros das funcoes de pertinencia dos consequentes
B1 = [0.028 -0.2254]; % pequeno
B2 = [0.0648 -0.07129]; % medio
B3 = [0.105 0.4499]; % meiogrande
B4 = [0.01799 1.01]; % grande
% Geracao das funcoes de pertinencia dos consequentes
y = -0.2172 : 0.01 : 1;
for i = 1 : size(y,2)
    fp_B1(i) = gaussmf(y(i), B1);
    fp_B2(i) = gaussmf(y(i), B2);
    fp_B3(i) = gaussmf(y(i), B3);
    fp_B4(i) = gaussmf(y(i), B4);
end
% Fuzzyficacao
pA1 = gaussmf(x, A1); % pertinencia na funcao A1
pA2 = gaussmf(x, A2); % pertinencia na funcao A2
pA3 = gaussmf(x, A3); % pertinencia na funcao A3
pA4 = gaussmf(x, A4); % pertinencia na funcao A4
% Calculo das regras fuzzy (composicao max-min)
% regra 1: Se X eh pequeno entao Y e grande
w1 = pA1; % forca de disparo da regra 1
fp_B14 = min(w1, fp_B4); % funcao de pertinencia B1 qualificada
% regra 2: Se X eh medio entao Y e pequeno
w2 = pA2; % forca de disparo da regra 2
fp_B21 = min(w2, fp_B1); % funcao de pertinencia B1 qualificada
% regra 3: Se X eh meiogrande entao Y e pequeno
w3 = pA3; % forca de disparo da regra 3
fp_B31 = min(w3, fp_B1); % funcao de pertinencia B1 qualificada
% regra 4: Se X eh grande entao Y e medio
w4 = pA4; % forca de disparo da regra 4
fp_B42 = min(w4, fp_B2); % funcao de pertinencia B1 qualificada
% agregacao das regras
fp_y = max([fp_B14; fp_B21; fp_B31; fp_B42]); % funcao de pertinencia de saida
% Defuzzyficacao
y = defuzz(y, fp_y, 'centroid'); % saida