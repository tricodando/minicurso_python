"""
    Lab (Colecionando Figurinhas)

    Problema: Criar diferentes estruturas de dados
    para exibir uma coleção de figurinhas.
"""
j1 = ('Alisson', 1)
jogadores = [('Alisson', 1), ('Neymar', 10), ('Coutinho', 11)]
carros = [('Ferrari', 1970), ('Porsche', 1990), ('BMW', 1995)]
jogadores.pop(0)

caixa = {
    'jogadores': jogadores,
    'carros': carros
}

caixa.pop('jogadores')

print(caixa)
