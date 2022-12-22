from random import choice

letras = 'abcdefghijklmnopqrstuvABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789\n '
lista_letras = [letra for letra in letras]

texto = ''
contador = 0
for i in range(len(letras)*100):
    texto += choice(letras)

with open('teste.txt', 'w') as txt:
    txt.write(texto)
