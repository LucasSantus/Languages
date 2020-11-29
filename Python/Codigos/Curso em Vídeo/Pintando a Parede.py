print("Pintando a Parede")

largura = float(input("Insira a Largura da Parede: "))
altura = float(input("Insira a Altura da Parede: "))

print("Sua Parede de Dimensão {}x{} e Área {:.2f}m²".format(largura,altura, largura*altura))
print("Utilizara {:.2f} Litros de Tinta".format((largura*altura)/2))
