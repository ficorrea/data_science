# -*- coding: utf-8 -*-

import random


class Muta():

    def mutados(populacao, cromossomo):
        x = 0
        while x < len(populacao):
            mutado = populacao[x]

            for i in range(cromossomo):
                porcentagem = round(random.random(), 2)
                if porcentagem <= 0.05:
                    if mutado[i] == 1:
                        mutado[i] = 0
                    else:
                        mutado[i] = 1
                else:
                    pass
            populacao[x] = mutado
            x += 1
        return populacao
