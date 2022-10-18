function conf = mconfusao(treinamento, teste, qtd_linhas)
verdadeiro_positivo = 0;
verdadeiro_negativo = 0;
falso_positivo = 0;
falso_negativo = 0;
for i = 1:qtd_linhas
    if treinamento(i, 4) == 1 && teste(i, 4) == 1
        verdadeiro_positivo = verdadeiro_positivo + 1;
    end
    if treinamento(i, 4) == -1 && teste(i, 4) == 1
        falso_positivo = falso_positivo + 1;
    end
    if treinamento(i, 4) == 1 && teste(i, 4) == -1
        falso_negativo = falso_negativo + 1;
    end
    if treinamento(i, 4) == -1 && teste(i, 4) == -1
        verdadeiro_negativo = verdadeiro_negativo + 1;
    end
end
% matriz_confusao(1:1) = 1;
% matriz_confusao(1:2) = -1;
% matriz_confusao(2:1) = verdadeiro_positivo;
% matriz_confusao(3:1) = falso_positivo;
% matriz_confusao(1:2) = verdadeiro_negativo;
% matriz_confusao(2:1) = falso_negativo;
fprintf('verdadeiro_positivo: '); disp(verdadeiro_positivo)
fprintf('verdadeiro_negativo: '); disp(verdadeiro_negativo)
fprintf('falso_positivo: '); disp(falso_positivo)
fprintf('falso_negativo: '); disp(falso_negativo)
conf = 0;
end
