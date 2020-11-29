print("Preço da Passagem")

distancia = float(input("Insira a Distância da Viagem:" ))
print("Você Está Prestes a Iniciar sua Viagem de {} KM".format(distancia))

if distancia <= 200:
    print("O Valor da Sua Viagem: R${:.2f}". format(distancia*0.50))
else:
    print("O Valor da Sua Viagem: R${:.2f}".format(distancia * 0.45))
