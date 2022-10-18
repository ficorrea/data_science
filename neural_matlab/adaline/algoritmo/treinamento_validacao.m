%Valores padrão
aprendizagem = 0.01;
epoca = 0;
precisao = 1e-12;

%Treinamento
w = rand(1,4);
fprintf('Ws iniciais: %0.3f\t%0.3f\t%0.3f\n', w(2:4));
w_ajustado = adl(x_train, w, epoca, aprendizagem, precisao, qtd_linhas_treino);

%Validacao
valido = validacao(x_valido, w_ajustado, qtd_linhas_valido);
plot(valido);

%Calculo do EQM
validado = [x_valido valido];
erro_quadratico_medio = erro(y_valido_original, validado, w_ajustado);
fprintf('Erro quadratico medio: %0.4f\n', erro_quadratico_medio);