import os
import re


def extrair_bacterias(pasta: str, arquivo: str, pasta_saida: str,
                      arquivo_saida: str, bacterias: list):

    caminho_completo = f'{pasta}/ARTIGO-{arquivo}.txt'
    caminho_saida = f'{pasta_saida}/{arquivo_saida}.txt'

    lista_bacterias = []

    with open(caminho_completo, 'r') as txt:
        conteudo = txt.readlines()
        for linha in conteudo:
            for bacteria in bacterias:
                bac_re = re.findall(fr'{bacteria}\s[a-zA-z]+', linha)
                for bac in bac_re:
                    if bac not in lista_bacterias:
                        lista_bacterias.append(bac)

    with open(caminho_saida, 'w') as txt:
        for especie in lista_bacterias:
            txt.write(especie)
            txt.write('\n')

    os.remove(caminho_completo)
