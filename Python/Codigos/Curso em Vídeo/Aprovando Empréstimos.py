print("Aprovando Empréstimos")

casa = float(input("O Valor da Casa: "))
salario = float(input("Salário do Comprador: "))
ano = int(input("Anos de Financiamento: "))
prestacao = casa/(ano*12)
print("PARA PAGAR R${:.2f} NA CASA EM {} ANO(S) A PRESTAÇÃO SERÁ DE R${:.2f}".format(casa, ano, prestacao))
if prestacao <= salario * 0.30:
    print("EMPRÉSTIMO CONCEDIDO!")
else:
    print("EMPRÉSTIMO NEGADO!")
