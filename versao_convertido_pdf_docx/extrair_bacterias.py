def extrair_bacterias(especies: str, pasta: str, nome_arquivo: str):
    caminho = f'{pasta}/ARTIGO-{nome_arquivo}.txt'
    with open(caminho, 'w') as doc:
        for especie in especies:
            if 3 < len(especie) < 20:
                doc.write(especie)
                doc.write('\n')
