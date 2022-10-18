# -*- coding: utf-8 -*-

import random


class Individuo():
    u"""Classe para manipulação dos indivíduos."""

    def __init__(self):
        u"""Determina pesos e benefícios."""
        # total máximo dos pesos 81
        self.peso = [16, 18, 1, 8, 12, 0, 5, 6, 2, 13]

        # total máximo do benefício 306
        self.beneficio = [32, 20, 25, 11, 35, 50, 47, 34, 19, 33]

    def cria_individuo(self, genes, valor_peso):
        u"""Cria o indivíduo com base no peso."""
        individuo = []
        i = 0
        while i < 1:
            for i in range(genes):
                individuo.append(random.randint(0, 1))
            valido = self.validar(individuo, valor_peso)
            if valido is True:
                i += 1
                return individuo

    def validar(self, ind, valor):
        u"""Valida o peso do indivíduo."""
        valido = 0
        for i in range(len(ind)):
            valido = valido + (self.peso[i] * ind[i])
        if valido <= valor:
            return True
        else:
            return None

    def fitness(self, ind):
        u"""Calcula o fitness."""
        total = 0
        for i in range(len(ind)):
            total = total + (self.beneficio[i] * ind[i])
        return total

    def sorteia_individuos(self, populacao, numero_individuos):
        u"""Escolhe uma quantidade de indivíduos aleatoriamente."""
        i = 0
        sorteados = []
        while i < numero_individuos:
            sorte = random.randint(0, len(populacao) - 1)
            if sorte not in sorteados:
                sorteados.append(sorte)
                i += 1
            else:
                pass
        return sorteados
