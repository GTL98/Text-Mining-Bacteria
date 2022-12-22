import os
from docx import Document


def extrair_italico(pasta: str, arquivo: str):
    arquivo_usado = ''
    for doc in os.listdir(pasta):
        if doc == f'{arquivo}.docx':
            arquivo_usado = doc

    documento = Document(f'{pasta}/{arquivo_usado}')
    italico = []

    for paragrafo in documento.paragraphs:
        for linha in paragrafo.runs:
            if linha.italic:
                italico.append(linha.text.strip())

    return italico
