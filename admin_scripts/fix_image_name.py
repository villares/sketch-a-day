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
    
imagens_boas = [nome for nome in nomes_arquivos
                if nome_pasta in nome
                and is_img_ext(nome)]
if imagens_boas:
    print("Não precisei fazer nada!")
else:
    imagens = [file_name for file_name
               in nomes_arquivos
               if is_img_ext(file_name)]
#     print(imagens[0] if imagens
#           else "não tem imagens!")
    nome_imagem = imagens[0] if imagens else None
    if nome_imagem:
        ext = nome_imagem.split('.')[-1]
        novo_nome = nome_pasta + '.' + ext
        os.rename(nome_imagem, novo_nome)
    else:
        print("Não encontrei imagens!")
    #print(os.path.join(cwd, file_name))