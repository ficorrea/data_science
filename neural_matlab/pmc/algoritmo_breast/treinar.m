function [treino, w] = treinar(tabela, d, y_ajustado, w1, w2, w3, precisao, aprendizagem, epoca)
em_anterior = erro(tabela, d, y_ajustado, w1, w2, w3);
while 1
    [y_ajustado, w1, w2, w3] = backpro(tabela, d, w1, w2, w3, aprendizagem);
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
w = [w1, w2, w3];
end
    