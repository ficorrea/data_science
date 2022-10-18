function taxa = taxa_classificacao(d, d_validado)
qtd_linhas = size(d, 1);
total_certas = 0;
for i = 1:qtd_linhas
    if d(i) == d_validado(i)
        total_certas = total_certas + 1;
    end
end
taxa = total_certas / qtd_linhas;
fprintf("Taxa de classificação correta: %.3f\n", taxa);
end