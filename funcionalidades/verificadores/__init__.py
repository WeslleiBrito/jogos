def recebe_int(msg):
    while True:
        valor = str(input(msg))
        try:
            valor = int(valor)
        except:
            print('\033[1;31mDigite apenas números inteiros.\033[0m')
        else:
            return valor
