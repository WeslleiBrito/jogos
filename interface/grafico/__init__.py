from time import sleep


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


def boneco(erros, espaco, msg):

    espaco = espaco + len(msg) + 3
    b = chr(92)
    desenho = ['O', '/', '|', b, '/', b]
    if erros >= 1:
        print(f'{desenho[0]}'.rjust(espaco))
        sleep(0.5)
    if erros >= 2:
        print(f'{desenho[1]}'.rjust(espaco - 1), end='')
        sleep(0.5)
    if erros >= 3:
        print(f'{desenho[2]}', end='')
        sleep(0.5)
    if erros >= 4:
        print(f'{desenho[3]}')
        sleep(0.5)
    if erros >= 5:
        print(f'{desenho[4]}'.rjust(espaco - 1), end='')
        sleep(0.5)
    if erros >= 6:
        print(f'{desenho[5]:}'.rjust(2))

    if 2 <= erros <= 3 or erros == 5:
        print()


def preenchendo_letras(tamanho):
    linhas = ['_' for index in tamanho]
    return linhas


def nome_jogo(nome):
    b = 'Bem-Vindo ao jogo da '
    tamanho = len(nome) + len(b) + 10
    print('-' * tamanho)
    print('|', end='')
    print(f'{b+nome}'.center(tamanho - 2), end='')
    print('|')
    print('-' * tamanho)


if __name__ == '__main__':
    boneco(6, 6, 'Palavra secreta')
