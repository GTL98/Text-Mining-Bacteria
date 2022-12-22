def extracao_texto(especies: list, pasta_destino: str, nome_arquivo: str):
    caminho = f'{pasta_destino}/ARTIGO-{nome_arquivo}.txt'
    with open(caminho, 'w') as doc:
        for especie in especies:
            doc.write(especie)
            doc.write('\n')
