function wajustado = pctr(tabela, w, epoca, d, aprendizagem, qtd_linhas)
while 1
    erro = 'F';
    for i = 1:qtd_linhas
        u = (w(1)*tabela(i,1) + w(2)*tabela(i,2) + w(3)*tabela(i,3) + w(4)*tabela(i,4));
        y = sinal(u);
        if y ~= d(i)
            w(1) = w(1) + aprendizagem * (d(i) - y) * tabela(i, 1);
            w(2) = w(2) + aprendizagem * (d(i) - y) * tabela(i, 2);
            w(3) = w(3) + aprendizagem * (d(i) - y) * tabela(i, 3);
            w(4) = w(4) + aprendizagem * (d(i) - y) * tabela(i, 4);
            erro = 'V';
        end
    end
    epoca = epoca + 1;
    if erro == 'F' || epoca == 1000
        break;
    end    
end
fprintf('Epocas: %d\n', epoca)
fprintf('Wajustado: \n'); disp(w(2:4))
fprintf('Theta: '); disp(w(1))
wajustado = w;
% disp(y)
end

function y = sinal(a)  
if a >= 0
    y = 1;
end
if a < 0
    y = -1;
end
end