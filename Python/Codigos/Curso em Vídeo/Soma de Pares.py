print("Soma de Pares")

soma = 0;
cont = 0
for a in range(0, 6):
    valor = int(input("Insira o {}º Valor:".format(a + 1)))
    if valor == 0:
        continue

    if valor % 2 == 0:
        soma += valor
        cont += 1

print("{} Números Pares, Soma: {}".format(cont, soma))
