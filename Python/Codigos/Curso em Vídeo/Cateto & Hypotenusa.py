print("Cateto e Hypotenuza")

import math

Cto = float(input("Insira o Cateto Oposto: "))
Cta = float(input("Insira o Cateto Adjacente: "))
Hyp = math.hypot(Cto, Cta)

print("Hypotenuza: {:.2f}".format(Hyp))
