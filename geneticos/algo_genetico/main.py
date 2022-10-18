# -*- coding: utf-8 -*-

import statistics
import matplotlib.pyplot as graf
from gera import Gerar as geracao
from fitness import Fit as fit
from cruzamento import Cruzar as cruza
from selecao import Selecionar as selecionado
from mutacao import Muta as muta
from cruzamento_roleta import Cruzar_Roleta as roleta

banco_dados = []


def armazenar_dados(populacao):
    individuo = []
    valores = []
    for i in range(len(populacao)):
        individuo = populacao[i]
        valores.append(fit.fitness(individuo))
    return valores


def gerar_grafico():
    ymedia = []
    ymaximo = []
    yminimo = []
    x = list(range(0, len(banco_dados)))
    for i in range(len(banco_dados)):
        ymedia.append(round(statistics.mean(banco_dados[i]), 0))
        ymaximo.append(max(banco_dados[i]))
        yminimo.append(min(banco_dados[i]))
    graf.title('TP - Algoritmo Genético')
    graf.xlabel('Iterações')
    graf.ylabel('Resultados')
    graf.plot(x, ymaximo, label='Fitness Máximos')
    #graf.plot(x, ymedia, label='Fitness Médios')
    #graf.plot(x, yminimo, label='Fitness Mínimos')
    graf.legend(loc='upper left')
    graf.show()


def main():
    num_individuos = 10
    num_cromossomos = 36
    num_filhos = num_individuos // 2
    populacao = []
    a = 0

    while a < 100:
        populacao = geracao.gera(num_individuos, num_cromossomos)
        b = 0
        while b < 100:
            filhos = cruza.cruzamento(populacao, num_cromossomos, num_filhos)
            filhos_roleta = roleta.cruzamento_roleta(populacao, num_cromossomos, num_filhos)
            filhos = filhos + filhos_roleta
            filhos = muta.mutados(filhos, num_cromossomos)
            populacao = populacao + filhos
            populacao = selecionado.selecionados(num_individuos, populacao)
            #banco_dados.append(armazenar_dados(populacao))
            b += 1
        banco_dados.append(armazenar_dados(populacao))
        a += 1
    gerar_grafico()

if __name__ == "__main__":
    main()
