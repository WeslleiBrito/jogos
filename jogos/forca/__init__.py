from random import randint
from interface.grafico import boneco


def pontos(letras_e, palavra_s, pontuacao):
    bonus = 10
    restante = abs(letras_e - palavra_s)
    if restante != 0:
        bonus = bonus * restante
    else:
        bonus = bonus * palavra_s
    print(f'{"Pontuação:":15}{pontuacao:>4}\n{"Bonus:":15}{bonus:>4}\n{"Total:":15}{pontuacao + bonus:>4}')


def jogo():
    enforcou = False
    acertou = False
    palavras = ['banana', 'games', 'pesquisa', 'historia', 'educação', 'modelo', 'impressora',
                'lampada', 'formiga', 'zoologico', 'paises', 'mundo', 'janeiro', 'felicidade']
    computador = randint(0, len(palavras) - 1)
    palavra_secreta = palavras[computador]
    letras_encontradas = []
    encontrada = 0
    erros = 0
    msg = 'Palavra Secreta: '
    i = []
    pontuacao = 1000
    rodadas = 0
    for index in range(0, len(palavra_secreta)):
        letras_encontradas.append('_')
    print(palavra_secreta)
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

            for lt in i:
                letras_encontradas[lt] = palavra_secreta[lt]
            i.clear()

            if erros == 6:
                print('Game Over')
                enforcou = True
            else:
                if letras_encontradas == palavra_secreta:
                    pontos(len(letras_encontradas), len(palavra_secreta), pontuacao)
                    acertou = True
                else:
                    encontrada = 0
                    print(msg, end='')
                    for descobertas in letras_encontradas:
                        print(descobertas, end='')
        else:
            if palavra_secreta == chute:
                print('Você venceu a partida')
                pontos(len(letras_encontradas), len(palavra_secreta), pontuacao)
                acertou = True
            else:
                print(f'Game Over\nA palavra secreta é: {palavra_secreta}')
                enforcou = True
        rodadas += 1


if __name__ == '__main__':
    jogo()
