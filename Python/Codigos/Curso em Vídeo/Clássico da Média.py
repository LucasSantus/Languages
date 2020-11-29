print("Clássico da Média")

n1 = float(input("Insira a 1ª Nota: "))
n2 = float(input("Insira a 2ª Nota: "))

media = (n1 + n2)/2
print("1ª Nota: {}\n2ª Nota: {}\nMédia: {}".format(n1, n2, media))
if media <= 5:
    print("VOCÊ SE LASCOU!")
elif media < 7:
    print("VOCÊ ESTÁ DE RECUPERAÇÃO!")
elif media <= 10:
    print("PARABENS, VOCÊ PASSOU!")
else:
    print("NOTA INVÁLIDA!")
