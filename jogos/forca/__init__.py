from random import randint
from interface.grafico import boneco


def jogo():
    enforcou = False
    acertou = False
    palavras = ['banana', 'games', 'pesquisa', 'historia', 'educação', 'modelo', 'impressora']
    computador = randint(0, len(palavras))
    palavra_secreta = palavras[computador]
    letras_encontradas = []
    encontrada = 0
    enf = 0
    atual = ''
    anterior = ''
    print('Palavra Secreta:', '_ ' * len(palavra_secreta))
    for index in range(0, len(palavra_secreta)):
        letras_encontradas.append('_ ')
    print(letras_encontradas)
    print(palavra_secreta)
    while not acertou and not enforcou:
        chute = str(input('Digite uma letra ou o nome: ')).strip().lower()
        if len(chute) == 1:
            for index, letra in enumerate(palavra_secreta):
                if chute == letra:
                    print(f'Encontrei a letra "{letra}" na posição {index}')
                    letras_encontradas[index] = letra
                    print(letras_encontradas)
                    encontrada = 1
                if encontrada == 0:
                    enf += 1
                if enf == 6:
                    print('Game Over')
                    enforcou = True
        else:
            if palavra_secreta == chute:
                print('Você venceu a partida')
        print('jogando...')


if __name__ == '__main__':
    jogo()
