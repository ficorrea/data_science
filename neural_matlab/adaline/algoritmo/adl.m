function w_ajustado = adl(tabela, w, epoca, aprendizagem, precisao, qtd_linhas)
u = 0;
eqm_anterior = calcula_eqm(tabela, w, qtd_linhas);
while 1    
    for i = 1:qtd_linhas
        u = (w(1)*tabela(i,1) + w(2)*tabela(i,2) + w(3)*tabela(i,3) + w(4)*tabela(i,4));
        w(1) = w(1) + aprendizagem * (tabela(i,5) - u) * tabela(i, 1);
        w(2) = w(2) + aprendizagem * (tabela(i,5) - u) * tabela(i, 2);
        w(3) = w(3) + aprendizagem * (tabela(i,5) - u) * tabela(i, 3);
        w(4) = w(4) + aprendizagem * (tabela(i,5) - u) * tabela(i, 4);
    end
    eqm_atual = calcula_eqm(tabela, w, qtd_linhas);
    epoca = epoca + 1;
    if abs(eqm_atual - eqm_anterior) <= precisao || epoca == 1000
        break;
    else
        eqm_anterior = eqm_atual;
    end    
end
fprintf('Epocas: %i\n', epoca);
fprintf('W_ajustado: %0.4f\t%0.4f\t%0.4f\n', w(2:4));
fprintf('Theta: %0.4f\n', w(1));
w_ajustado = w;
end
    