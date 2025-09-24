#Classe, objeto, atributo e metodo;

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.status = False
    
    def ligar(self):
        self.ligado = True
        print(f"O carro {self.modelo} está ligado")

    def desligar(self):
        self.ligado = False
        print(f"O carro {self.modelo} está desligado")
    

meu_carro = Carro("Honda Civic", "Civic Type-R", 2024 )

print(f"Marca: {meu_carro.marca}")
print(f"Modelo: {meu_carro.modelo}")
print(f"Ano: {meu_carro.ano}")
print(f"Estado: {meu_carro.status}")

meu_carro.ligar()
meu_carro.desligar()


