% Variáveis básicas
aprendizagem = 0.4;
epoca = 0;
precisao = 1e-12;
y_inicial = zeros(size(d_train,1),1);

% Criação dos W's
w = rand(1, 9);

% Treinamento
[y_ajustado, w_ajustado] = treinar(x_train, d_train, y_inicial, w, precisao, aprendizagem, epoca);

% Validacao
y_validado = validar(x_val, w_ajustado);
w1 = w_ajustado(1:3);
w2 = w_ajustado(4:6);
w3 = w_ajustado(7:9);
eqm_validacao = erro(x_val, d_val, y_ajustado, w1, w2, w3);
fprintf("EQM validação: %.3f\n", eqm_validacao);

% Exibe dados
subplot(2,1,1);
plot(Xt(:,3));
title('Dados de Treinamento');
subplot(2,1,2);
plot(y_validado,'r');
title('Dados de Valida��o');