import os
import PyPDF2


def extrair_linhas_pdf(pasta: str, arquivo: str, pasta_saida: str, arquivo_saida: str):
    arquivo_usado = ''
    for doc in os.listdir(pasta):
        if doc == f'{arquivo}.pdf':
            arquivo_usado = doc

    caminho_saida = f'{pasta_saida}/ARTIGO-{arquivo_saida}.txt'
    caminho_completo = f'{pasta}/{arquivo_usado}'

    pdf = open(caminho_completo, 'rb')

    leitor_pdf = PyPDF2.PdfFileReader(pdf)

    paginas = leitor_pdf.numPages

    for i in range(paginas):
        obj = leitor_pdf.getPage(i)

        texto = obj.extractText().split("  ")

        with open(caminho_saida, 'a') as txt:
            for j in range(len(texto)):
                txt.write(texto[j])

    pdf.close()
