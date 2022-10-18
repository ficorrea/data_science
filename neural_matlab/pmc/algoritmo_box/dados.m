% Manipulação dos datasets de treinamento e validação

% Treinamento
x_train = Xt(:, 1:2);
d_train = Xt(:, 3);

% Validação
x_val = Xv(:, 1:2);
d_val = Xv(:, 3);

% Normalizacao dos dados
x_train = normalizacao(x_train);
d_train = normalizacao(d_train);
x_val = normalizacao(x_val);
d_val = normalizacao(d_val);

% Inclusao do bias
bias = ones(size(Xt, 1), 1) * -1;
x_train = [bias x_train];

bias = ones(size(Xv, 1), 1) * -1;
x_val = [bias x_val];