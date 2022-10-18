# -*- coding: utf-8 -*-

import matplotlib.pyplot as grafico


class Grafico():
    u"""Classe para geração de gráficos."""

    def __init__(self):
        u"""Inicialização da classe sem parâmetro."""
        pass

    def plotar(self, escala_x, minimo_y, medio_y, maximo_y):
        u"""Método gerador de gráficos."""
        x = list(range(escala_x))
        yminimo = minimo_y
        ymedio = medio_y
        ymaximo = maximo_y
        grafico.title('AG - Problema Mochila')
        grafico.xlabel('Gerações')
        grafico.ylabel('Resultados')
        grafico.plot(x, ymaximo, label='Fitness Máximo')
        grafico.plot(x, ymedio, label='Fitness Medio')
        grafico.plot(x, yminimo, label='Fitness Mínimo')
        grafico.legend(loc='lower right')
        grafico.show()
