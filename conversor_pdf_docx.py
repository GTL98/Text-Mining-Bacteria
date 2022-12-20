import PyPDF2

arquivo = 'Documento sem nome.pdf'
saida = ''

with open(arquivo, 'rb') as f:
    reader = PyPDF2.PdfFileReader(f)
    contador = reader.numPages
    for i in range(contador):
        pagina = reader.pages[i]
        saida += pagina.extract_text()

print(saida)
