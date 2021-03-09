import random

print("Sorteando Itens")

n1 = input("Insira o 1° Item: ")
n2 = input("Insira o 2° Item: ")
n3 = input("Insira o 3° Item: ")
n4 = input("Insira o 4° Item: ")

list = [n1, n2, n3, n4]
random.shuffle(list)
print(list)
