"""
    Lab (Modelando uma Pessoa)

    Problema: Modelar uma classe Pessoa para representar
    suas características através dos atributos e seus
    comportamentos através dos métodos.
"""
class Pessoa:
    def __init__(self, cor, altura, peso, sexo):
        self.cor = cor
        self.altura = altura
        self.peso = peso
        self.sexo = sexo

    def andar(self):
        print("Passeando no bosque...")

    def falar(self):
        print("Bla bla bla...")

pessoa = Pessoa('morena', 1.7, 60, 'feminino')
pessoa.falar()
