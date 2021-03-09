import random

print("Sorteando Alunos")

n1 = input("Insira o Primeiro Aluno: ")
n2 = input("Insira o Segundo Aluno: ")
n3 = input("Insira o Terceiro Aluno: ")
n4 = input("Insira o Quarto Aluno: ")

lista = [n1, n2, n3, n4]

esc = random.choice(lista)

print("O Escolhido é: {}".format(esc))
