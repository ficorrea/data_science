# -*- coding: utf-8 -*-

from populacao import Populacao
from grafico import Grafico

# Variáveis do sistema
##########################################
tamanho_populacao = 100
tamanho_gene = 10
valor_peso = 50
numero_filhos = tamanho_populacao // 2
tamanho_maximo_geracoes = 100
elitismo = True
numero_individuos_elitismo = 3
porcentagem_mutacao = 0.05
roleta = True
torneio = False
numero_individuos_torneio = 5
##########################################

pop = Populacao()
graf = Grafico()
maximos = []
medios = []
minimos = []


def main():
    u"""Método principal."""
    i = 0
    geracao = 1
    peoples = pop.cria_populacao(tamanho_populacao, tamanho_gene, valor_peso)

    while i < tamanho_maximo_geracoes:

        # Seleciona os melhores para elitismo ou os
        # melhores da metade da população
        if elitismo is True:
            peoples = pop.elitismo_sobreviventes(
                peoples, numero_individuos_elitismo
            )

            new_peoples = pop.cria_populacao(
                ((tamanho_populacao // 2) - len(peoples)),
                tamanho_gene, valor_peso
            )

            peoples = peoples + new_peoples

        else:
            peoples = pop.elitismo_sobreviventes(peoples, len(peoples) // 2)

        # Gera filhos
        filhos = pop.gerar_filhos(
            peoples, numero_filhos, roleta, torneio,
            numero_individuos_torneio, valor_peso
        )
        if filhos == 0:
            break

        # Aplica mutação nos filhos gerados
        filhos_mutados = pop.mutacao(filhos, porcentagem_mutacao, valor_peso)

        # Insere os filhos na população
        peoples = peoples + filhos_mutados

        # Armazena os valores máximos e mínimos
        # da população para plotagem do gráfico
        maximos.append(int(max(pop.fitness_populacao(peoples))))
        minimos.append(int(min(pop.fitness_populacao(peoples))))
        medios.append((maximos[i] + minimos[i]) // 2)

        # Printa os valores máximos, médios e mínimos de cada geração
        print(
            '%dª geracao: máximo: %d | médio: %d | mínimo: %d'
            % (geracao, maximos[i], medios[i], minimos[i])
        )
        geracao += 1
        i += 1

    # Plota o gráfico
    graf.plotar(tamanho_maximo_geracoes, minimos, medios, maximos)


if __name__ == '__main__':
    main()
