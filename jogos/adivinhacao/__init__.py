import math

import funcionalidades.verificadores as verificar
import interface.grafico as grafico
from random import randint


def jogo():
    sair = 1
    rodadas = [10, 5, 3]
    final = 0
    niveis = ['Fácil', 'Médio', 'Difícil']
    tentativa = 0
    pontuacao = 1000
    bonus = 200
    total = 1200
    grafico.niveis(niveis)
    while sair == 1:
        escolha = verificar.recebe_int('Escolha um dos níveis: ')
        if 1 <= escolha <= len(niveis):
            if escolha == 1:
                final = rodadas[0]
            elif escolha == 2:
                final = rodadas[1]
            else:
                final = rodadas[2]
            sair = 0
        else:
            print(f'Escolha não encontrada, suas opções são entre 1 e {len(niveis)}.')
    computador = randint(1, 50)
    print(computador)
    for c in range(0, final):
        tentativa += 1
        if tentativa == 1:
            t = 'tentativa'
        else:
            t = 'tentativas'
        palpite = verificar.recebe_int(f'Qual seu palpite entre 1 e 50 [{tentativa}/{final}]? ')
        if computador == palpite:
            print(f'Parabéns, você acertou o número secreto em {tentativa} {t}.')
            grafico.resumo_adivinhacao(tentativa, pontuacao, bonus, total)
            break
        else:
            bonus -= 10
            pontuacao -= int(math.fabs(computador - palpite))
            total = pontuacao + bonus
            print(total)
            if computador > palpite:
                sugestao = 'maior'
            else:
                sugestao = 'menor'
            if c != final - 1:
                print(f'Não foi dessa vez, tente novamente com um valor {sugestao}.')
            else:
                print('Infelizmente você esgotou suas tentativas, GAME OVER.')


if __name__ == '__main__':
    jogo()
