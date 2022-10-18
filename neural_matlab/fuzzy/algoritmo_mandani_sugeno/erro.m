function eqm = erro(x, y, y_imp)
colunas = size(x,2);
em = 1 / colunas * sum((y - y_imp).^2); 
eqm = em;
end