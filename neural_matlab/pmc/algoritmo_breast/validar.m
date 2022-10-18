function valido = validar(tabela, w1, w2, w3)
qtd_linhas = size(tabela, 1);
y3 = (qtd_linhas:1);
for i = 1:qtd_linhas
    l1 = w1 * tabela(i,:)';
    y1 = tanh(l1);

    l2 = w2 * tabela(i,:)';
    y2 = tanh(l2);

    l3 = w3 * [-1 y1 y2]';

    % Classificação
    y3(i) = tanh(l3);
    
    % Ajuste validação
    if y3(i) <= 0.5
        y3(i) = 0;
    else
        y3(i) = 1; 
end

valido = y3;
end
