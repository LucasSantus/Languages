import math
print("Seno, Cosseno, Tangente")

angulo = int(input("Informe o Ângulo: "))

seno = math.sin(math.radians(angulo))
coss = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))

print("Ângulo {}°\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}".format(angulo, seno, coss, tang))