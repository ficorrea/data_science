# -*- coding: utf-8 -*-

from fitness import Fit as fit


class Selecionar():

    def selecionados(num_ind, populacao):
        x = 0
        valores = []
        selecao = []
        valores = fitness_geral(populacao)
        while x < num_ind:
            indice = valores.index(max(valores))
            selecao.append(populacao[indice])
            valores.pop(indice)
            populacao.pop(indice)
            x += 1
        return selecao


def fitness_geral(populacao):
    valor = []
    for i in range(len(populacao)):
        valor.append(fit.fitness(populacao[i]))
    return valor
