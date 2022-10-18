
for i = 1 : size(x,2)
    [ y_mandani_imp(i) ] = mandani_1(x(i));
end
plot(x,y);
hold on
plot(x,y_mandani_imp, 'r');
hold on
plot(x, y_mandani_tool, 'g');
xlabel('X'); ylabel('Y');
title('Saida do Sistema Fuzzy tipo Mandani');

eqm = erro(x, y, y_mandani_imp);
fprintf('EQM Mandani Implementado:'); disp(eqm)

eqm = erro(x, y, y_mandani_tool);
fprintf('EQM Mandani Toolbox:'); disp(eqm)