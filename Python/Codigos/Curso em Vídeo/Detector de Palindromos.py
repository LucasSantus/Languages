print("Detector de Palindromo")

frase = str(input("Digite uma Frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = junto[::-1]
print("O Inverso de {} é {}".format(junto, inverso))
if inverso == junto:
    print("Temos um Palíndromo")
else:
    print("Não Temos um Palíndromo")
