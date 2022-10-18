function [backpropagation, w1_new, w2_new, w3_new] = backpro(tabela, d, w1, w2, w3, aprendizagem)

qtd_linhas = size(tabela,1);
y3 = (qtd_linhas:1);

for i = 1:qtd_linhas
    %% Fase Forward
    l1 = w1 * tabela(i,:)';
    y1 = tanh(l1);

    l2 = w2 * tabela(i,:)';
    y2 = tanh(l2);

    l3 = w3 * [-1 y1 y2]';

    % Classificação
    y3(i) = tanh(l3);

    %% Fase Backward
    % Classificação
    delta3 = (d(i) - y3(i)) * (1 - y3(i)^2);

    w3 = w3 + (aprendizagem * delta3 * [-1 y1 y2]);
    
    delta2 = sum(delta3 * w3) * (1 - y2.^2);
    w2 = w2 + (aprendizagem * delta2 * tabela(i,:));

    delta1 = sum(delta3 * w3) * (1 - y1.^2);
    w1 = w1 + (aprendizagem * delta1 * tabela(i,:));
end
backpropagation = y3;
w1_new = w1;
w2_new = w2; 
w3_new = w3;
end


    
