print("Comparando Números")

num_one = int(input("Insira o 1º Valor: "))
num_two = int(input("Insira o 2º Valor: "))

if num_one > num_two:
    print("O 1º Número é MAIOR")
    print("O 2º Número é MENOR")
elif num_two > num_one:
    print("O 1º Número é MENOR")
    print("O 2º Número é MAIOR")
else:
    print("Os Dois Números Tem o Mesmo TAMANHO!")
