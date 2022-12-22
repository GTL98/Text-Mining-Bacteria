import os
from docx import Document


def encontrar_italico(pasta_saida: str):
    arquivo = ''
    for doc in os.listdir(pasta_saida):
        arquivo = doc
    documento = Document(f'{pasta_saida}/{arquivo}')
    italico = []

    for paragrafo in documento.paragraphs:
        for linha in paragrafo.runs:
            if linha.italic:
                if linha.text.strip() not in italico:
                    italico.append(linha.text.strip())

    for arquivo in os.listdir(pasta_saida):
        os.remove(f'{pasta_saida}/{arquivo}')

    return italico
