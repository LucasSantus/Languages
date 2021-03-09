print("Progressão Aritmética")

print("="*30)
print("     PROGRESSÃO ARITMÉTICA     ")
print("="*30)

termo = int(input("Informe o Primeiro Termo: "))
razao = int(input("Informe a Razão: "))
cont = termo + (10 - 1) * razao
for a in range(termo, cont + razao, razao):

    print("{} ->".format(a), end=' ')

print("Acabou, e Todo Mundo Morreu.")
