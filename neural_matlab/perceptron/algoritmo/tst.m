function teste_validacao = tst(w, tabela_teste, qtd_linhas, theta)
for i = 1:qtd_linhas
    u = (w(1) * tabela_teste(i, 1) + w(2) * tabela_teste(i, 2) + w(3) * tabela_teste(i, 3)) - theta;
    % tabela_teste(i, 6) = u;
    y = sinal(u);
    tabela_teste(i, 4) = y;
end
teste_validacao = tabela_teste(:, :);
end

function y = sinal(a)
if a >= 0
    y = 1;
end
if a < 0
    y = -1;
end
end