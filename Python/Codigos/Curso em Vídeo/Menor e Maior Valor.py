print("Menor e Maior Valor")

menor = 0; maior = 0

qntd = int(input("Quantos Números Seram Adicionados: "))

for a in range(0, qntd):
    num = int(input("Insira os Valores: "))

    if num < menor or menor == 0:
        menor = num
    if num > maior:
        maior = num

print("O Valor Maior é: {}".format(maior))
print("O Valor Menor é: {}".format(menor))
