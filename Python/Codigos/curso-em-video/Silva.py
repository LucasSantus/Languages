print("Silva")

nome = str(input("Insira seu Nome Completo: ")).strip()

ok = "SILVA" in nome.upper()

if ok == True:
    print("Você Tem Silva no Nome!")

else:
    print("Você Não Tem Silva no Nome!")
