import interface.grafico as grafico
import funcionalidades.verificadores as verificar
import jogos.adivinhacao as adv
import jogos.forca as forca
titulo_abertura = 'Bem-vindo ao MAXGAME'
opcoes = ['Adivinhação', 'Forca', 'Sair']

while True:
    grafico.linha(len(titulo_abertura))
    grafico.titulo(titulo_abertura, len(titulo_abertura))
    grafico.titulo('JOGOS', len(titulo_abertura))
    grafico.menu(opcoes)
    grafico.linha(len(titulo_abertura))
    escolha = verificar.recebe_int('\033[1;36mEscolha seu jogo:\033[0m ')
    if 0 <= escolha <= len(opcoes):
        if escolha == 1:
            print('Jogando Adivinhação')
            adv.jogo()
        elif escolha == 2:
            print('Jogando Forca')
            forca.jogo()
        break
    else:
        print(f'\033[1;31mVocê pode escolher de 0 a {len(opcoes) - 1}\033[0m')


