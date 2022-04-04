"""
    Lab (Tabuada Impressa)

    ** [DESAFIO] **
    Problema: Criar uma tabuada do 1-20 e imprimir na tela
    no seguinte formato: ( 20 x 20 = 400 )
"""
for x in range(10): # [0,1,2,3,4,5,6,7,8,9]
    for y in range(10): # [0,1,2,3,4,5,6,7,8,9]
        print(x, 'x', y, '=', x*y)
