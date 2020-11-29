print("Analisando Triangulos")

num_one = int(input("Insira o 1º Valor: "))
num_two = int(input("Insira o 2º Valor: "))
num_tree = int(input("Insira o 3º Valor: "))

if num_one < num_two + num_tree and num_two < num_one + num_tree and num_tree < num_one + num_two:
    print("AS RETAS PODEM FORMAR TRAINGULOS")
else:
    print("AS RETAS NÃO PODEM FORMAR TRAINGULOS")
