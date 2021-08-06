def read_option(msg): #Trata alguns tipos de erro de digitação
    while True:
        try:
            option = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERROR: Please, enter a valid integer.\033[m')
        except (KeyboardInterrupt):
            print('\n\033[31mUser preferred not to enter a number.\033[m')
            return 0
        else:
            return option


def line (size = 42): #Desenha uma linha para o cabeçalho
    return '~' * size


def cabecalho(): #Mostra o cabeçalho do menu
    print(line())
    print(f'\033[32mSimulator of dice\033[m'.center(42))
    print(line())


def menu(list): #Lista as opções do usuario em forma de menu
    cabecalho()
    c = 1
    for item in list:
        print(f'\033[35m{c}\033[m - \033[36m{item}\033[m')
        c += 1 
    print(line())
    option = read_option('\033[32mYour choice: \033[m') #chama a função para verificar se a entrada do usuário é válida
    return option
