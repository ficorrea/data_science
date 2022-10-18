# -*- coding: utf-8 -*-

import random
from fitness import Fit as fit


class Cruzar_Roleta():

    def cruzamento_roleta(populacao, cromossomo, filhos):

        total = 0
        valor = 0
        x = 0
        filhos_gerados = []
        p_acumulado = []

        for i in range(len(populacao)):
            total = fit.fitness(populacao[i]) + total
        for i in range(len(populacao)):
            p_acumulado.append(round(fit.fitness(populacao[i]) / total, 2))
            valor = p_acumulado[i] + valor
            p_acumulado[i] = (round(valor, 2))
        while x < filhos:
            filho = []
            num1 = round(random.random(), 2)
            num2 = round(random.random(), 2)
            selecionado = selecionar_pai(p_acumulado, num1)
            pai1 = populacao[selecionado]
            selecionado = selecionar_pai(p_acumulado, num2)
            pai2 = populacao[selecionado]
            for i in range(cromossomo):
                vetor = round(random.random(), 2)
                if vetor > 0.5:
                    filho.append(pai1[i])
                else:
                    filho.append(pai2[i])
            filhos_gerados.append(filho)
            x += 1
        return filhos_gerados


def selecionar_pai(lista, numero):

    selecao = 0
    x = 0

    while lista[x] <= numero:
        selecao = x
        if x == len(lista) - 1:
            break
        else:
            x += 1

    return selecao
