from time import perf_counter
from extracao_texto import extracao_texto
from encontrar_fontes import encontrar_italico
from conversor_pdf_docx import conversor_pdf_docx


def main():
    arquivo_pdf = ''
    pasta_arquivo = 'arquivos_pdf'
    pasta_saida = 'arquivo_saida'
    pasta_destino = 'especies_extraidas'
    tempo_inicio = perf_counter()
    conversor_pdf_docx(pasta_arquivo, pasta_saida, arquivo_pdf)
    especies = encontrar_italico(pasta_saida)
    extracao_texto(especies, pasta_destino, arquivo_pdf)
    tempo_final = perf_counter() - tempo_inicio
    print(f'Arquivo ARTIGO-{arquivo_pdf}.txt criado com sucesso!')
    print(f'Tempo esperado: {tempo_final:.2f} segundos')


if __name__ == '__main__':
    main()
