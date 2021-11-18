from random import randint
from interface.grafico import boneco


def pontos(letras_e, palavra_s, pontuacao, rodadas):
    bonus = 10
    if letras_e == palavra_s and rodadas <= 0:
        bonus = 0
    else:
        bonus = bonus * rodadas
    print(f'{"Pontuação:":15}{pontuacao:>4}\n{"Bonus:":15}{bonus:>4}\n{"Total:":15}{pontuacao + bonus:>4}')


def jogo():
    enforcou = False
    acertou = False
    palavras = ['banana', 'games', 'pesquisa', 'historia', 'educação', 'modelo', 'impressora',
                'lampada', 'formiga', 'zoologico', 'paises', 'mundo', 'janeiro', 'felicidade']
    computador = randint(0, len(palavras) - 1)
    palavra_secreta = palavras[computador]
    encontrada = 0
    erros = 0
    msg = 'Palavra Secreta: '
    i = []
    pontuacao = 1000
    rodadas = len(palavra_secreta)
    letras_encontradas = ['_' for index in palavra_secreta]
   
    while not acertou and not enforcou:
        chute = str(input('\nDigite uma letra ou o nome: ')).strip().lower()
        if len(chute) == 1:
            for index, letra in enumerate(palavra_secreta):
                if chute == letra:
                    i.append(index)
                    encontrada = 1

            if encontrada == 0 or chute in letras_encontradas:
                erros += 1
                boneco(erros, len(palavra_secreta), msg)
                pontuacao -= 20
            else:
                if erros != 0:
                    boneco(erros, len(palavra_secreta), msg)
                pontuacao -= 10
            rodadas -= 1

            for lt in i:
                letras_encontradas[lt] = palavra_secreta[lt]
            i.clear()

            if erros == 6:
                print(f'Game Over\nA palavra secreta é: {palavra_secreta}')
                enforcou = True
            else:
                encontrada = 0
                print(msg, end='')
                for descobertas in letras_encontradas:
                    print(descobertas, end='')
            unidas = ''.join(letras_encontradas)
            if unidas == palavra_secreta:
                print()
                pontos(unidas, palavra_secreta, pontuacao, rodadas)
                acertou = True
        else:
            if palavra_secreta == chute:
                print('Você venceu a partida')
                pontos(''.join(letras_encontradas), palavra_secreta, pontuacao, rodadas)
                acertou = True
            else:
                print(f'Game Over\nA palavra secreta é: {palavra_secreta}')
                enforcou = True


if __name__ == '__main__':
    jogo()
