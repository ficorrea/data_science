# -*- coding: utf-8 -*-

import random
from individuo import Individuo


class Populacao():
    u"""Classe para manipulação da população."""

    def __init__(self):
        u"""Inicialização do objeto indivíduo."""
        self.ind = Individuo()

    def cria_populacao(self, tamanho, genes, valor_peso):
        u"""Cria a população e leva em consideração o valor do peso."""
        i = 0
        populacao = []
        while i < tamanho:
            individuo = self.ind.cria_individuo(genes, valor_peso)
            if individuo is None:
                pass
            else:
                populacao.append(individuo)
                i += 1
        return populacao

    def fitness_populacao(self, populacao):
        u"""Armazena o fitness de todos os indivíduos da população
            em um lista de mesma ordem."""
        valores = []
        for i in range(len(populacao)):
            valores.append(self.ind.fitness(populacao[i]))
        return valores

    def selecao_validos(self, populacao, valor_peso):
        u"""Verifica e armazena os indivíduos que são válidos."""
        validos = []
        for i in range(len(populacao)):
            validar = self.ind.validar(populacao[i], valor_peso)
            if validar is True:
                validos.append(populacao[i])
            else:
                pass
        return validos

    def selecao_roleta(self, populacao):
        u"""Seleciona o melhor indivíduo pelo índice de aptidão."""
        valores = self.fitness_populacao(populacao)
        total = 0
        soma = 0
        x = 0
        for i in range(len(valores)):
            total = total + valores[i]
        r = random.randint(0, total)
        while soma <= r:
            if x >= len(populacao):
                x = len(populacao) - 1
                break
            individuo = populacao[x]
            soma = soma + valores[x]
            x += 1
        return individuo

    def selecao_torneio(self, populacao, numero_individuos):
        u"""Seleciona o melhor indivíduo escolhido aleatoriamente
            na população."""
        pop = []
        sorteados = self.ind.sorteia_individuos(populacao, numero_individuos)
        for i in range(numero_individuos):
            pop.append(populacao[sorteados[i]])
        valores = self.fitness_populacao(pop)
        return pop[valores.index(max(valores))]

    def elitismo_sobreviventes(self, populacao, numero_individuos):
        u"""Seleciona a quantidade desejada de individuos de melhor fitness da
            população."""
        pop = populacao[:]
        valores = []
        selecionados = []
        x = 0
        valores = self.fitness_populacao(pop)
        while x < numero_individuos:
            posicao = valores.index(max(valores))
            selecionados.append(pop[posicao])
            valores.pop(posicao)
            pop.pop(posicao)
            x += 1
        return selecionados

    def gerar_filhos(self, populacao, prole, roleta, torneio,
                     numero_individuos, valor_peso
                     ):
        u"""Método de geração de descendentes por seleção roleta ou torneio."""
        x = 0
        filhos = []
        # Verifica o tipo de método escolhido
        if roleta is True and torneio is True:
            print(
                'Erro no método gerador: Defina ativo somente'
                ' um dos métodos de seleção!'
            )
            return 0
        elif roleta is False and torneio is False:
            print(
                'Erro no método gerador: Defina um método'
                ' de seleção para continuar!'
            )
            return 0
        # Executa a geração de filhos com a quantidade escolhida
        while x < prole:
            if roleta is True:
                gerador1 = self.selecao_roleta(populacao)
                gerador2 = self.selecao_roleta(populacao)
            elif torneio is True:
                gerador1 = self.selecao_torneio(populacao, numero_individuos)
                gerador2 = self.selecao_torneio(populacao, numero_individuos)
            gene1 = gerador1[0:len(gerador1) // 2]
            gene2 = gerador2[0:len(gerador2) // 2]
            valido = self.ind.validar(gene1 + gene2, valor_peso)
            if valido is True:
                filhos.append(gene1 + gene2)
                x += 1
            else:
                pass
        return filhos

    def mutacao(self, populacao, porcentagem, valor_peso):
        u"""Método de mutação, variando de acordo com a porcentagem."""
        x = 0
        while x < len(populacao):
            # Seleciona o indivíduo de populacao
            mutado = populacao[x]
            for i in range(len(mutado)):
                # Efetua a comparacao com a porcentagem e se menor ou igual
                # executa a mutação
                comparacao = round(random.random(), 2)
                if comparacao <= porcentagem:
                    if mutado[i] == 1:
                        mutado[i] = 0
                    else:
                        mutado[i] = 1
                else:
                    pass
            valido = self.ind.validar(mutado, valor_peso)
            if valido is True:
                populacao[x] = mutado
                x += 1
            else:
                pass
        return populacao

    def peso_populacao(self, populacao):
        u"""Armazena o peso de todos os indivíduos da população
            em um lista de mesma ordem."""
        valor = []
        for i in range(len(populacao)):
            valor.append(self.ind.validar(populacao[i]))
        return valor
