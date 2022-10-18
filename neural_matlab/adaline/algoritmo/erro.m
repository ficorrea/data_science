function erro_quadratico = erro(y_treino, y_validado, w)
qtd_linhas = size(y_validado, 1);
eqm = 0;
n = 0;
y = 0;
for i = 1:qtd_linhas
    n = n + (w(1)*y_validado(i,1) + w(2)*y_validado(i,2) + w(3)*y_validado(i,3) + w(4)*y_validado(i,4));
    y = y + (y_validado(i, 5) - y_treino(i, 1));
end
eqm = (1/n) * y;
erro_quadratico = eqm;
end