# -*- coding: utf-8 -*-

import random


class Cruzar():

    def cruzamento(populacao, cromossomo, filhos):

        filhos_gerados = []
        indice_pai1 = []
        indice_pai2 = []
        x = 0
       
        pai1 = populacao[0:len(populacao) // 2]
        pai2 = populacao[len(populacao) // 2:len(populacao)]
        indice_pai1 = ordenacao(indice_pai1, pai1)
        indice_pai2 = ordenacao(indice_pai2, pai2)
        while x < filhos:
            filho = []
            gerador1 = pai1[indice_pai1[x]]
            gerador2 = pai2[indice_pai2[x]]
            for i in range(cromossomo):
                vetor = round(random.random(), 2)
                if vetor > 0.5:
                    filho.append(gerador1[i])
                else:
                    filho.append(gerador2[i])
            filhos_gerados.append(filho)
            x += 1
        return filhos_gerados


def ordenacao(lista1, lista2):

    while len(lista1) < len(lista2):
        valor = random.randint(0, len(lista2) - 1)
        if valor not in lista1:
            lista1.append(valor)

    return lista1
