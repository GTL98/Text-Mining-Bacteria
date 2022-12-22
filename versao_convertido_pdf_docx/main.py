from time import perf_counter
from extrair_fonte import extrair_italico
from extrair_bacterias import extrair_bacterias


def main():
    pasta_docx = 'arquivos_docx'
    pasta_saida = 'arquivos_saida'
    nome_arquivo = ''
    tempo_inicial = perf_counter()
    especies = extrair_italico(pasta_docx, nome_arquivo)
    extrair_bacterias(especies, pasta_saida, nome_arquivo)
    tempo_final = perf_counter() - tempo_inicial
    print(f'Arquivo ARTIGO-{nome_arquivo}.txt criado com sucesso!')
    print(f'Tempo esperado: {tempo_final:.2f} segundos.')


if __name__ == '__main__':
    main()
