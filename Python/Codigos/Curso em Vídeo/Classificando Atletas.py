print("Classificando Atletas")

ano = int(input("Insira o Ano de Nascimento: "))

if ano <= 9:
    print("MIRIM")

elif ano <= 14:
    print("INFANTIL")

elif ano <= 19:
    print("JUNIOR")

elif ano <= 25:
    print("SÊNIOR")

else:
    print("MASTER")


