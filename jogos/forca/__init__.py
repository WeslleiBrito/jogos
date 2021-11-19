from interface.grafico import boneco, preenchendo_letras
import unidecode


def jogo():
    enforcou = False
    acertou = False
    palavra_secreta = gera_secreta()
    palavra_real = palavra_secreta[1]
    palavra_secreta = palavra_secreta[0]

    encontrada = 0
    erros = 0
    msg = 'Palavra Secreta: '
    i = []
    pontuacao = 1000
    rodadas = len(palavra_secreta)
    rd = 0
    letras_encontradas = preenchendo_letras(palavra_secreta)

    while not acertou and not enforcou:
        if rd > 0:
            chute = str(input('\nDigite uma letra ou o nome: ')).strip().lower()
        else:
            chute = str(input('Digite uma letra ou o nome: ')).strip().lower()
            rd = 1
        chute = unidecode.unidecode(chute)
        if len(chute) == 1:
            for index, letra in enumerate(palavra_secreta):
                letra = letra.lower()
                letra = unidecode.unidecode(letra)
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
                print(f'Game Over. A palavra secreta é: {palavra_real}')
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


def pontos(letras_e, palavra_s, pontuacao, rodadas):
    bonus = 10
    if letras_e == palavra_s and rodadas <= 0:
        bonus = 0
    else:
        bonus = bonus * rodadas
    print(f'{"Pontuação:":15}{pontuacao:>4}\n{"Bonus:":15}{bonus:>4}\n{"Total:":15}{pontuacao + bonus:>4}')


def gera_secreta():
    from random import randint
    lista_palavras = []
    lista_letras = []
    with open('palavras.txt', encoding='utf-8') as arquivo:
        for palavra in arquivo:
            lista_palavras.append(palavra.strip())

    computador = randint(0, len(lista_palavras) - 1)
    palavra_secreta = lista_palavras[computador]
    palavra_secreta_real = palavra_secreta
    for letra in palavra_secreta:
        lista_letras.append(letra)
    for indice, letra in enumerate(lista_letras):
        lista_letras[indice] = unidecode.unidecode(letra)
    palavra_secreta = ''.join(lista_letras).lower()
    return [palavra_secreta, palavra_secreta_real]


if __name__ == '__main__':
    jogo()
