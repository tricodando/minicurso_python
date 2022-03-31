"""
    Lab (Se Aprovado)

    Problema: Exibir na tela por meio de mensagens se um
    aluno foi aprovado, reprovado ou ficou de recuperação.

    Casos:
        Aprovado if (nota >= 7)
        Recuperação if (nota > 5 and nota < 7)
        Reprovado if (nota <= 5)
"""
nota = float(input("Digite a nota: "))

if (nota >= 7):
    print("Aluno aprovado!")
elif (nota > 5 and nota < 7):
    print("Aluno de recuperação!")
else:
    print("Aluno reprovado!")
