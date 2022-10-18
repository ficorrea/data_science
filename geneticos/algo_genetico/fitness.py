# -*- coding: utf-8 -*-


class Fit():

    def fitness(individuo):
        valor = 9 + int(individuo[1]) * int(individuo[4])
        valor -= int(individuo[22]) * int(individuo[13])
        valor += int(individuo[23]) * int(individuo[3])
        valor -= int(individuo[20]) * int(individuo[9])
        valor += int(individuo[35]) * int(individuo[14])
        valor -= int(individuo[10]) * int(individuo[25])
        valor += int(individuo[15]) * int(individuo[16])
        valor += int(individuo[2]) * int(individuo[32])
        valor += int(individuo[27]) * int(individuo[18])
        valor += int(individuo[11]) * int(individuo[33])
        valor -= int(individuo[30]) * int(individuo[31])
        valor -= int(individuo[21]) * int(individuo[24])
        valor += int(individuo[34]) * int(individuo[26])
        valor -= int(individuo[28]) * int(individuo[6])
        valor += int(individuo[7]) * int(individuo[12])
        valor -= int(individuo[5]) * int(individuo[8])
        valor += int(individuo[17]) * int(individuo[19])
        valor -= int(individuo[0]) * int(individuo[29])
        valor += int(individuo[22]) * int(individuo[3])
        valor += int(individuo[20]) * int(individuo[14])
        valor += int(individuo[25]) * int(individuo[15])
        valor += int(individuo[30]) * int(individuo[11])
        valor += int(individuo[24]) * int(individuo[18])
        valor += int(individuo[6]) * int(individuo[7])
        valor += int(individuo[8]) * int(individuo[17])
        valor += int(individuo[0]) * int(individuo[32])
        return valor
