data = importdata('dados_treinamento.txt', ' ');
validacao = importdata('dados_validacao.txt', ' ');
bias = (30:1);
for i = 1:30
    bias(i, 1) = -1;
end
x_train = [bias(1:30, 1) data(1:30, 1:3)];
d = data(1:30, 4);
aprendizagem = 0.1;
epoca = 0;
qtd_linhas = 30;
