print("Calculo de Desconto")

produto = float(input("Valor do Produto: "))
desconto = float(input("Valor do Desconto: "))

print("O Produto com valor R${},Adicionado Desconto de {}%, Seu Preço Será R${}".format(produto,desconto,produto-(produto*(desconto/100))))
