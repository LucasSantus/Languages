print("Primeira e Ultima Ocorrencia de String")

frase = str(input("Insira uma Frase: ")).upper()

print("A letra A aparece {} vezes".format(frase.count("A")))
print("A Primeira Letra A Aparece na Posição {}".format(frase.find("A")+1))
print("A Ultima Letra A Aparece na Posição {}".format(frase.rfind("A")+1))
