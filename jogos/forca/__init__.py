from interface.grafico import boneco, preenchendo_letras
import unidecode

def jogo():
    enforcou = False
    acertou = False
    palavra_secreta = gera_secreta()
    print(palavra_secreta)
    encontrada = 0
    erros = 0
    msg = 'Palavra Secreta: '
    i = []
    pontuacao = 1000
    rodadas = len(palavra_secreta)
    letras_encontradas = preenchendo_letras(palavra_secreta)

    while not acertou and not enforcou:
        chute = str(input('\nDigite uma letra ou o nome: ')).strip().lower()
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
            palavra_secreta.lower()
            lista_palavra = []
            for ltr in palavra_secreta:
                lista_palavra.append(ltr)
            for indice in range(len(lista_palavra)):
                lista_palavra[indice] = unidecode.unidecode(palavra_secreta[indice])
            lista_palavra = ''.join(lista_palavra)
            if palavra_secreta == lista_palavra:
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
    with open('palavras.txt', encoding='utf-8') as arquivo:
        for palavra in arquivo:
            lista_palavras.append(palavra.strip())

        computador = randint(0, len(lista_palavras) - 1)
        palavra_secreta = lista_palavras[computador]
        return palavra_secreta


if __name__ == '__main__':
    jogo()
