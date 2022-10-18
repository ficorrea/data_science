function valido = validar(tabela, w)
qtd_linhas = size(tabela, 1);
y3 = (qtd_linhas:1);
w1 = w(1:3);
w2 = w(4:6);
w3 = w(7:9);
for i = 1:qtd_linhas
    l1 = w1 * tabela(i,:)';
    y1 = tanh(l1);

    l2 = w2 * tabela(i,:)';
    y2 = tanh(l2);

    l3 = w3 * [-1 y1 y2]';

    % Aproximação
    y3(i) = l3;

end
valido = y3;
end
