"""
    Lab (Shell Interativo)

    Problema: Criar um loop com a estrutura 'while' e
    deixar a função do cálculo de IMC mais interativa
"""
def imc(peso, altura):
    imc = peso / (altura**2)
    if imc < 18.5:
        print("Classificação: Magreza")
    elif imc >= 18.5 and imc <= 24.9:
        print("Classificação: Normal")
    elif imc >= 25 and imc <= 29.9:
        print("Classificação: Sobrepeso")
    elif imc >= 30 and imc <= 39.9:
        print("Classificação: Obesidade")
    else:
        print("Classificação: Obesidade Grave")

while True:
    peso = float(input("Digite o peso: "))
    altura = float(input("Digite a altura: "))
    imc(peso, altura)

    opc = input("Digite 0 para sair ou enter para continuar: ")
    if opc == "0":
        break
