print("Reajuste Salarial")

salario = float(input("Insira o Salário: "))
aumento = int(input("Insira o Aumento: "))
print("O salário de R${}, Terá seu aumento para R${:.2f}".format(salario, salario+(salario*(aumento/100))))

