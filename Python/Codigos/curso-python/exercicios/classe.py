class Computador():
    def __init__(self, marca, memoria_ram, placa_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_video = placa_video

    def Ligar(self):
        print("Estou Ligando!")

    def Desligar(self):
        print("Estou Desligando")

    def ExibirInformacoes(self):
        print(self.marca, self.memoria_ram, self.placa_video)

    pass

computer = Computador()