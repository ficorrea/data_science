% Dados para treinamento e normalização
data_treino = importdata('xt.txt', ' ');
[qtd_linhas_treino, ~] = size(data_treino);
data_treino = normalizacao(data_treino);

% Dados para validação e normalização
data_valido = importdata('xv.txt', ' ');
[qtd_linhas_valido, ~] = size(data_valido);
data_valido = normalizacao(data_valido);

%Inclusao do bias nas tabelas
bias = (qtd_linhas_treino:1);
for i = 1:qtd_linhas_treino
    bias(i, 1) = -1;
end

x_train = [bias data_treino];
x_valido = [bias(1:qtd_linhas_valido, :) data_valido(:, 1:3)];
y_valido_original = data_valido(:, 4);
