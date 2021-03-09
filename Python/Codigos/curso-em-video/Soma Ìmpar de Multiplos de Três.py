print("Soma Ìmpar de Multiplos de Três")

soma = 0; cont = 0
for a in range(1, 501, 2):
    if a % 3 == 0:
        soma += a
        cont += 1

print("A soma dos {} valores solicitados é {}".format(cont, soma))
