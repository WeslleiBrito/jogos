def linha(t):
    li = '-' * (t + 4)
    return print('\033[1;33m' + li + '\033[0m')


def titulo(msg, tamanho):
    return print('\033[1;32m' + msg.center(tamanho + 4) + '\033[0m')


def menu(lista):
    for i, texto in enumerate(lista):
        if len(lista) - 1 != i:
            posicao = i + 1
        else:
            posicao = 0
        print(f'\033[1;35m[{posicao}] - {texto}\033[0m')


def niveis(lista):
    for i, texto in enumerate(lista):
        posicao = i + 1
        print(f'\033[1;35m[{posicao}] - {texto}\033[0m')


def resumo_adivinhacao(tentativas, pontos, bonus, total):
    print('Resumo da Partida:')
    print('{:<15}{:>5}'.format("Tentativas:", tentativas))
    print('{:<15}{:>5}'.format("Pontos:", pontos))
    print('{:<15}{:>5}'.format("Bonus:", bonus))
    print('{:<15}{:>5}'.format("Total:", total))
