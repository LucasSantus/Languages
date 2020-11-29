print("Analisando Textos")

nome = str(input("Insira seu Nome Completo: "))

print("Seu nome em Maiusculo: {}".format(nome.upper()))
print("Seu nome em Minusculo: {}".format(nome.lower()))
print("O Tamanho do seu Nome: {}".format(len(nome.strip())))
dividido = nome.split()
print("O seu Nome é {} e tem {} letras".format(dividido[0], len(dividido[0])))
