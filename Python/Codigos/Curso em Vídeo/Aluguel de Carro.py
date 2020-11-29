print("Aluguel de Carro")

dia = int(input("Por quantos dias o carro foi alugado: "))
km = float(input("Quantos Km percorridos: "))

somaDia = dia * 60
somaKm = km * 0.15

print("Por ter utilizado o veículo por {} dias, percorrido {} km, o preço ficará em R${:.2f}".format(dia, km, somaDia + somaKm))
