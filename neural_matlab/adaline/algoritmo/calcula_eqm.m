function eqm_calculado = calcula_eqm(tabela, w, qtd_linhas)
[linhas, colunas] = size(tabela(:, 1:4));
qtd_amostras = linhas * colunas;
eqm_temp = 0;
for i = 1:qtd_linhas
    u = (w(1)*tabela(i,1) + w(2)*tabela(i,2) + w(3)*tabela(i,3) + w(4)*tabela(i,4));
    eqm_temp = eqm_temp + (tabela(i,5) - u)^2;
end
eqm_calculado = eqm_temp / qtd_amostras;
end