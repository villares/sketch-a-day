from __future__ import unicode_literals
from collections import Counter

add_library('WordCram')

size(700, 400)
background(100, 100, 200)

with open('data/texto.txt', 'r') as arquivo:
    linhas_brutas = arquivo.readlines()
    
palavras = []
for linha in linhas_brutas:
    linha = unicode(linha.strip(), 'utf8') # remove espaços finais, iniciais \n 
    linha = linha.replace('.', '').replace(',', '').replace('!', '')
    linha = linha.replace('?', '').replace(';', '').replace(':', '')
    palavras_linha = linha.split() # separa no espaços
    for palavra in palavras_linha:
        if len(palavra) > 4:
            if palavra.endswith('s'):
                palavra = palavra[:-1]
            palavras.append(palavra)

contador = Counter(palavras)
lista_palavras = [Word(w, number) for w, number in contador.items()]

# Pass in the sketch (the variable "this"), so WordCram can draw to it.
wordcram = WordCram(this).fromWords(lista_palavras) # Pass in the words to draw.
# Now we've created our WordCram, we can draw it:
wordcram.drawAll()
