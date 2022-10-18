function validado = validacao(tabela, w, qtd_linhas)
d = (qtd_linhas:1);
for i = 1:qtd_linhas
    d(i,1) = w(1)*tabela(i,1) + w(2)*tabela(i,2) + w(3)*tabela(i,3) + w(4)*tabela(i,4);
end
validado = d;
end