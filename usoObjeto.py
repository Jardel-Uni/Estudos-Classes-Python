class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def unir_nomes(self):
        self.nome_completo = self.nome +" "+ self.sobrenome
        print(f"O nome completo é {self.nome_completo}.")

primero_Nome = "Jardel" 
segundo_Nome = "Lima"
pessoa = Pessoa(primero_Nome, segundo_Nome)

print(pessoa.nome)
print(pessoa.sobrenome)
pessoa.unir_nomes()

outra_Pessoa = Pessoa("Jamille", "Moura")
print(outra_Pessoa.nome)
print(outra_Pessoa.sobrenome)
outra_Pessoa.unir_nomes()