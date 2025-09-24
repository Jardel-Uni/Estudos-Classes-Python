class Pessoa:
    # Método construtor: inicializa cada nova instância da classe Pessoa
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo para armazenar o nome
        self.idade = idade  # Atributo para armazenar a idade

    # Método de instância: exibe uma mensagem de apresentação
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Criação de uma instância da classe Pessoa
pessoa1 = Pessoa("João", 25)

# Chamada ao método que apresenta a pessoa
pessoa1.apresentar()