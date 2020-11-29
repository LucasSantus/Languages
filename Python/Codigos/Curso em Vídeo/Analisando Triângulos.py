print("Analisando Triangulos 2.0")

num_one = int(input("Insira o 1º Valor: "))
num_two = int(input("Insira o 2º Valor: "))
num_tree = int(input("Insira o 3º Valor: "))

if num_one < num_two + num_tree and num_two < num_one + num_tree and num_tree < num_one + num_two:
    print("AS RETAS PODEM FORMAR O ", end="")
    if num_one == num_two == num_tree:
        print("TRIÂNGULO EQUILATERO!")
    elif num_one != num_two != num_tree != num_one:
        print("TRIÂNGULO ESCALENO!")
    else:
        print("TRIÂNGULO ISÓSCELES!")
else:
    print("AS RETAS NÃO PODEM FORMAR TRAINGULOS")