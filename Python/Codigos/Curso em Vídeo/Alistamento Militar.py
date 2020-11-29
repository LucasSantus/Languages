print("Alistamento Militar")

from datetime import date

nascimento = int(input("Ano do Nascimento: "))

tod = date.today().year
ano = tod - nascimento
if ano < 18:
    print("Faltam {} Ano(S) Para Você se Alistar".format(18 - ano))
elif ano == 18:
    print("Ja Está Na Hora de se Alistar!")
else:
    print("Você se Alistou no Ano {}".format(nascimento + 18))
    print("Seu tempo de Alistar ja Passou!")
