% Manipulação dos datasets de treinamento e validação

% Treinamento
d_train = Xt(:, 11);

% Validação
d_val = Xv(:, 11);

% Normalizacao dos dados
x_train_1 = normalizacao(Xt(:, 1));
x_train_2 = normalizacao(Xt(:, 2:10));
x_val_1 = normalizacao(Xv(:, 1));
x_val_2 = normalizacao(Xv(:, 2:10));

% Inclusao do bias
bias = ones(size(Xt, 1), 1) * -1;
x_train = [bias x_train_1 x_train_2];

bias = ones(size(Xv, 1), 1) * -1;
x_val = [bias x_val_1 x_val_2];