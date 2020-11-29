print("Jogo da Adivinhação")

from random import randint
from time import sleep

comp = randint(0,5)
print("\033[0;34m-=-\033[m"*20)
print("\033[0;36mVou pensar em um número de 0 a 5, Tente adivinhar...\033[m")
print("\033[0;34m-=-\033[m"*20)
print("\033[0;36mEm que Número eu Pensei?\033[m")
jog = int(input("\033[0;36mNúmero Pensado: \033[m"))
print("\033[0;33mPROCESSANDO...\033[m")
sleep(2)
if jog == comp:
    print("\033[0;32mPARABENS, VOCÊ VENCEU!!\033[m")
else:
    print("\033[0;31mVISH, VOCÊ PERDEU!!\033[m")
