function error = erro(tabela, d, y, w1, w2, w3)

qtd_linhas = size(tabela, 1);

%% Erro quadrático
y_new = 0;
y1 = (qtd_linhas:1);
y2 = (qtd_linhas:1);
y3 = (qtd_linhas:1);

for i = 1:qtd_linhas
   y1(i) = w1 * tabela(i,:)';
   y2(i) = w2 * tabela(i,:)';
   y3(i) = w3 * [-1 y1(i) y2(i)]'; 
   y_new = y_new  + (y3(i) * (d(i) - y(i))^2);
end
e = 0.5 * y_new;

%% Erro quadrático médio
[linhas, colunas] = size(tabela);
p = linhas * colunas;
em = 1 / p * e;
error = em;
end
