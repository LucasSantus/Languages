print("Conversor de Bases")

valor = int(input("Insira um Número: "))

print("""ESCOLHA UMA DAS BASES
  Base BINÁRIA   - [ 1 ] 
   Base OCTAL    - [ 2 ] 
Base HEXADECIMAL - [ 3 ] """)
opcao = int(input("Sua Opção: "))
if opcao == 1:
    print("{} Convertido para Binário: {}".format(valor, bin(valor)[2:]))
elif opcao == 2:
    print("{} Convertido para Binário: {}".format(valor, oct(valor)[2:]))
elif opcao == 3:
    print("{} Convertido para Binário: {}".format(valor, hex(valor)[2:]))
else:
    print("Escolha Inválida!")

