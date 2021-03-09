print("Primeiro e Ultimo Nome")

nome = str(input("Insira seu Nome Completo:")).strip()

divid = nome.split()

print("Prazer em te Conhecer")
print("Primeiro Nome: {}".format(divid[0]))
print("Ùltimo Nome: {}".format(divid[len(divid)-1]))
