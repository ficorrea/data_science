function [treino, w] = treinar(tabela, d, y_ajustado, w, precisao, aprendizagem, epoca)
w1 = w(1:3);
w2 = w(4:6);
w3 = w(7:9);
em_anterior = erro(tabela, d, y_ajustado, w1, w2, w3);
while 1
    [y_ajustado, w_ajustado] = backpro(tabela, d, w1, w2, w3, aprendizagem);
    w1 = w_ajustado(1:3);
    w2 = w_ajustado(4:6);
    w3 = w_ajustado(7:9);
    em_atual = erro(tabela, d, y_ajustado, w1, w2, w3);
    epoca = epoca + 1;
    if abs(em_atual - em_anterior) <= precisao
        break;
    elseif epoca == 1000
        break;
    else
        em_anterior = em_atual;
    end
end
fprintf("EQM: "); disp(em_atual);
treino = y_ajustado;
w = [w_ajustado];
end
    