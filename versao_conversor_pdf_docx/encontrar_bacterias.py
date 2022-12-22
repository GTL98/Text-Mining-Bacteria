arquivo = 'teste.txt'

bacterias = ['Bacillus subtilis',
             'Helicobacter pylori',
             'Alistipes indistinctus',
             'Escherichia coli',
             'Streptococcus pneumoniae']

with open(arquivo, 'r') as txt:
    conteudo = txt.readlines()
    for linha in conteudo:
        for bacteria in bacterias:
            if bacteria in linha:
                print(bacteria)
