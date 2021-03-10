class Carro():
  def __init__(self, consumo, capacidade):
    self.capacidade = capacidade
    self.consumo = consumo
    self.litros = 0

  def mover(self, km):
    gasto = km / self.consumo

    if self.litros >= gasto:
      self.litros -= gasto
    else:
      self.litros = 0

  def gasolina(self):
    return self.litros

  def abastecer(self, litros):
    if (self.litros + litros) >= self.capacidade:
      self.litros = self.capacidade
    elif (self.litros + litros) < self.capacidade:
      self.litros = self.litros + litros
    else:
      print('O tanque está cheio!')