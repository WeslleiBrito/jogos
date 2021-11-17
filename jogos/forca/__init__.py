from random import randint
from interface.grafico import boneco


def jogo():
    enforcou = False
    acertou = False
    palavras = ['banana', 'games', 'pesquisa', 'historia', 'educação', 'modelo', 'impressora',
                'lampada', 'formiga' 'zoologico', 'paises', 'mundo', 'janeiro', 'felicidade']
    computador = randint(0, len(palavras) - 1)
    palavra_secreta = palavras[computador]
    letras_encontradas = []
    encontrada = 0
    erros = 0
    msg = 'Palavra Secreta: '

    for index in range(0, len(palavra_secreta)):
        letras_encontradas.append('_')
    print(palavra_secreta)
    while not acertou and not enforcou:
        chute = str(input('\nDigite uma letra ou o nome: ')).strip().lower()
        if len(chute) == 1:
            for index, letra in enumerate(palavra_secreta):
                if chute == letra:
                    letras_encontradas[index] = letra
                    encontrada = 1

            if encontrada == 0 or chute in letras_encontradas:
                erros += 1
                boneco(erros, len(palavra_secreta), msg)
            else:
                if erros != 0:
                    boneco(erros, len(palavra_secreta), msg)

            if erros == 6:
                print('Game Over')
                enforcou = True
            else:
                encontrada = 0
                print(msg, end='')
                for descobertas in letras_encontradas:
                    print(descobertas, end='')
        else:
            if palavra_secreta == chute:
                print('Você venceu a partida')
                acertou = True
            else:
                print(f'Game Over\nA palavra secreta é: {palavra_secreta}')
                enforcou = True


if __name__ == '__main__':
    jogo()
