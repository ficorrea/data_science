# -*- coding: utf-8 -*-

import random


class Gerar():
    
    def gera(num_populacao, num_cromossomo):
        x = 0
        populacao = []
        cromossomo = []
        while x in range(num_populacao):
            for i in range(num_cromossomo):
                cromossomo.append(random.randint(0, 1))
            populacao.append(cromossomo)
            cromossomo = []
            x += 1
        return populacao

