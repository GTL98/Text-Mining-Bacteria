from pdf_to_txt import extrair_linhas_pdf
from extrair_bacterias import extrair_bacterias


def main():
    pasta_pdf = 'arquivos_pdf'
    pasta_txt = 'arquivos_txt'
    pasta_bacterias = 'arquivos_bacterias'

    arquivo_pdf = input(str('Digite o arquivo PDF sem a extensão .pdf: '))
    arquivo_bacterias = input(str('Digite o nome do arquivo das bactérias sem a extensão .txt: '))
    entrada_bacterias = input(str('Digite a(s) bactéria(s) desejda(s) com somente 1 vígula entre elas: '))
    bacterias = entrada_bacterias.split(',')

    extrair_linhas_pdf(pasta_pdf, arquivo_pdf, pasta_txt, 'arquivo_txt')
    extrair_bacterias(pasta_txt, 'arquivo_txt', pasta_bacterias, arquivo_bacterias, bacterias)

    print(f'Arquivo {arquivo_bacterias}.txt criado com sucesso!')


if __name__ == '__main__':
    main()
