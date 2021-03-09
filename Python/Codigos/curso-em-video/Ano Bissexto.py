print("Ano Bissexto")

from datetime import date

ano = int(input("Que Ano Deseja Analizar? Coloque 0 para o Ano Atual: "))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("{} É BISSEXTO!".format(ano))

else:
    print("{} NÃO É BISSEXTO!".format(ano))
