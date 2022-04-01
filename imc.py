"""
    Lab (IMC - Índice de Massa Corporal)

    Problema: Criar um função que calcula o IMC - Índice
    de Massa Corporal e retornar o resultado.
    IMC = peso / (altura**2)

    Casos:
        Magreza ----------- IMC < 18.5
        Normal ------------ IMC >= 18.5 and IMC <= 24.9
        Sobrepeso --------- IMC >= 25 and IMC <= 29.9
        Obesidade --------- IMC >= 30 and IMC <= 39.9
        Obesidade Grave --- IMC >= 40
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

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc(peso, altura)
