function normalizado = normalizacao(tabela)
[qtd_linhas, qtd_colunas] = size(tabela);
xmax = max(max(tabela));
xmin = min(min(tabela));
for i = 1:qtd_linhas
    for j = 1:qtd_colunas
        tabela(i, j) = 2 * ((tabela(i, j) - xmin) / (xmax - xmin)) - 1;
    end
end
normalizado = tabela;
end