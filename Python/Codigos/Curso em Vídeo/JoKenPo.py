print("JOKENPO")

from random import randint
from time import sleep

itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)

print("""
[0] - PEDRA 
[1] - PAPEL  
[2] - TESOURA 
""")

jogador = int(input("Sua Jogada: "))

print("\033[0;32mJO\033[m")
sleep(1)
print("\033[0;32mKEN\033[m")
sleep(1)
print("\033[0;32mPOOOO!!\033[m")

print("\033[0;37m-=\033[0;32m"*20)
print("\033[0;32mComputador Jogou {}\033[m".format(itens[computador]))
print("\033[0;32mJogador Jogou {}\033[m".format(itens[jogador]))
print("\033[0;37m-=\033[0;32m"*20)

if computador == 0:
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("COMPUTADOR VENCE")
    else:
        print("Jogada Inválida!")

elif computador == 1:
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCE")
    else:
        print("Jogada Inválida!")

elif computador == 2:
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print("COMPUTADOR VENCE")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("Jogada Inválida!")

else:
    print("Jogada Inválida!")
