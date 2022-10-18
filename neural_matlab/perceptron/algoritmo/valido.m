for i = 1:5
    fprintf('Treinamento: %d\n', i);
    w = rand(1,4);
    fprintf('Ws iniciais: '); disp(w(2:4))
    wajustado = pctr(x_train, w, epoca, d, aprendizagem, qtd_linhas);
    w_final = wajustado(2:4);
    theta_final = wajustado(1);
    teste = tst(w_final, validacao, 10, theta_final);
    fprintf('Validação: \n'); disp(teste) 
    fprintf('**************************************\n');
end
