print("Aumentos Multiplos")

salario = float(input("Insira o seu Salário: "))

if salario <= 1250:
    print("Você Terá Aumento de 15%, Receberá R${}".format((salario*0.15)+salario))
else:
    print("Você Terá Aumento de 10%, Receberá R${}".format((salario * 0.10)+salario))
