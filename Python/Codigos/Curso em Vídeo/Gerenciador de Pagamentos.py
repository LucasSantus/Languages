print("Gerenciador de Pagamentos")

print("{:=^40}".format(" LOJAS OLIVEIRA "))

valor = float(input("VALOR DAS COMPRAS: "))

print("""MÉTODOS DE PAGAMENTO
Á VISTA DINHEIRO/CHEQUE [1]
A VISTA NO CARTÃO       [2]
2X NO CARTÃO            [3]
3X NO CARTÃO OU MAIS    [4]
""")
opcao = int(input("Sua Opção: "))

if opcao == 1:
    print("DINHEIRO/CHEQUE, CONSEGUE DESCONTO")
    print("VALOR COM DESCONTO DE 10%, PAGARÁ SOMENTE R${}".format(valor - (valor*0.10)))

elif opcao == 2:
    print("CARTÃO, CONSEGUE DESCONTO")
    print("VALOR COM DESCONTO DE 5%, PAGARÁ SOMENTE R${}".format(valor - (valor*0.5)))

elif opcao == 3:
    print("2x CARTÃO, PAGARÁ NORMALMENTE")
    print("PAGARÁ R${} A CADA MÊS TOTALIZANDO R${}".format(valor/2, valor))

elif opcao == 4:
    esc = int(input("Quantas Vezes Deseja Pagar o Valor: "))
    print("{}x CARTÃO, PAGARÁ JUROS".format(esc))
    print("TERÁ QUE PAGAR R${} POR MÊS TOTALIZANDO R${}".format(((valor + (valor*0.20))/esc), valor + (valor*0.20)))

else:
    print("ESCOLHA INVÁLIDA!")