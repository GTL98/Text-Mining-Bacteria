import os
from pdf2docx import Converter


def conversor_pdf_docx(caminho_arquivo: str, pasta_saida: str, arquivo_pdf: str):
    cv = Converter(f'{caminho_arquivo}/{arquivo_pdf}.pdf')
    cv.convert(f'{pasta_saida}/{arquivo_pdf}.docx')
    cv.close()
