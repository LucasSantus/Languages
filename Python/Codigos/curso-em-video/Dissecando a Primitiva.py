print("Dissecando a Primitiva")

algo = input("Insira Algo: ")
print(f"Tipo Primitivo: {type(algo)}")
print(f"É um Número: {algo.isnumeric()}")
print(f"É Somente Espaços: {algo.isspace()}")
print(f"É Alfabetico: {algo.isalpha()}")
print(f"É Alfanumérico: {algo.isalnum()}")
print(f"Está em Maiusculas: {algo.issuper()}")
print(f"Está em Minusculas: {algo.islower()}")
print(f"Está Capitalizada: {algo.istitle()}")

