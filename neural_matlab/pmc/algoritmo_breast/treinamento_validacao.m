% Variáveis básicas
aprendizagem = 0.3;
epoca = 0;
precisao = 1e-7;
y_inicial = zeros(size(d_train,1),1);

% Criação dos W's
w1 = rand(1, 11);
w2 = rand(1, 11);
w3 = rand(1, 3);

% Treinamento
[y_ajustado, w_ajustado] = treinar(x_train, d_train, y_inicial, w1, w2, w3, precisao, aprendizagem, epoca);

% Validacao
w1 = w_ajustado(1:11);
w2 = w_ajustado(12:22);
w3 = w_ajustado(23:25);
y_validado = validar(x_val, w1, w2, w3)';
taxa = taxa_classificacao(d_val, y_validado);

