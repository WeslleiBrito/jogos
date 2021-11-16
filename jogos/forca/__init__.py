from random import randint


def jogo():
    enforcou = False
    acertou = False
    palavras = ['banana', 'games', 'pesquisa', 'historia', 'educação', 'modelo', 'impressora']
    computador = randint(0, len(palavras))
    palavra_secreta = palavras[computador]
    letras_encontradas = []
    print('Palavra Secreta:', '_ ' * len(palavra_secreta))
    for index in range(0, len(palavra_secreta)):
        letras_encontradas.append('_ ')
    print(letras_encontradas)
    print(palavra_secreta)
    while not acertou and not enforcou:
        chute = str(input('Digite uma letra ou o nome: ')).strip().lower()[0]
        if len(chute) == 1:
            for index, letra in enumerate(palavra_secreta):
                if chute == letra:
                    print(f'Encontrei a letra "{letra}" na posição {index}')
                    letras_encontradas[index] = letra
                    print(letras_encontradas)
        else:
            if palavra_secreta == chute:
                print('Você venceu a partida')
        print('jogando...')


if __name__ == '__main__':
    jogo()
