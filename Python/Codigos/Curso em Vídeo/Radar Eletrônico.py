 print("Radar Eletrônico")

velocidade = float(input("Insira sua Velocidade: "))

if velocidade > 80:
    print("\033[0;31mMULTADO!! VOCÊ RECEBERÁ UMA MULTA DE R${:.2f}\033[m".format((velocidade-80)*7))
else:
    print("\033[0;34mTENHA UM BOM DIA, DIRIJA COM SEGURANÇA\033[m")

