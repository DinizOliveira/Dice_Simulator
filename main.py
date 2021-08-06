#D4, D6, D8, D10, D12, D20 and D100 simulator
from lib.dice import Dice 
from random import randint 
from lib.interface import menu 
from time import sleep 


while True:
    choice = menu(['D4','D6', 'D8', 'D10', 'D12', 'D20', 'D100', 'Exit']) 
    if choice == 8:
        print('exiting...')
        sleep(2)
        break
    else:
        dice = Dice(choice) #Cria a instância do objeto Dado
        print('\033[1;37mdrawing lots...\033[m'.center(42))
        sleep(2)
        print(f'\033[1;100m  {randint(1, dice.max_value)}  \033[m'.center(42))
        sleep(1)
    loop = str(input('\033[32mDo you wish to continue? (Y/N)\033[m\n'))
    sleep(0.5)
    if loop in 'Nn':
        print('\033[32mThanks for participation\033[m')
        sleep(1)
        break

