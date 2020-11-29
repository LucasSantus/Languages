print("IMC")

peso = float(input("Insira seu Peso: (Kg)"))
altura = float(input("Insira sua Altura: (M)"))

imc = peso / (altura ** 2)

if imc <= 18.5:
    print("Abaixo do Peso").upper()
elif imc <= 25:
    print("Peso Ideal").upper()
elif imc <= 30:
    print("Sobrepeso").upper()
elif imc <= 40:
    print("Obesidade").upper()
else:
    print("Obesidade Mórbida").upper()

print("O PESO DA PESSOA: {}".format(imc))
