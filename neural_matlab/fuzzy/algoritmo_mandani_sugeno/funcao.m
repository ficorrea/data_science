clear;

x = 0 : 0.01 : 2*pi;
y = sin(x)./x;
y(1) = 0;
plot(x,y);

sugeno_fis = readfis('sugeno.fis');
y_sugeno_tool = evalfis(x, sugeno_fis)';

mandani_fis = readfis('mandani.fis');
y_mandani_tool = evalfis(x, mandani_fis)';