#! /usr/bin/python3

# [X] add this to terminal aliases
# [X] Where am I?
# Look for images
# rename image with folder name
# extra: flag to run generate_entries?

import os
from helpers import is_img_ext

cwd = os.getcwd()
nome_pasta = os.path.split(cwd)[-1]
nomes_arquivos = sorted(os.listdir(cwd))

nomes_imagens = [file_name for file_name in nomes_arquivos
                if is_img_ext(file_name)]
imagens_boas = [nome_imagem for nome_imagem in nomes_imagens
                if nome_pasta in nome_imagem]
if imagens_boas:
    print('Não precisei fazer nada!')
elif nomes_imagens:
    nome_imagem = nomes_imagens[0]
    if nome_imagem:
        ext = nome_imagem.split('.')[-1]
        novo_nome = nome_pasta + '.' + ext
        os.rename(nome_imagem, novo_nome)
else:
    print('Não encontrei imagens!')
