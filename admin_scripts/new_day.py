#! /usr/bin/python3

# [ ] add this to terminal aliases
# check last folder...
# doplicate/rename new folder
# remove images
# rename file

import os
from helpers import is_img_ext

cwd = os.getcwd()
nome_pasta = os.path.split(cwd)[-1]
# nomes_arquivos = sorted(os.listdir(cwd))
# # Procura imagens no diretório corrente
# nomes_imagens = [file_name for file_name in nomes_arquivos
#                 if is_img_ext(file_name)]
# # Imagens boas são as que tem o mesmo nome da pasta!
# imagens_boas = [nome_imagem for nome_imagem in nomes_imagens
#                 if nome_imagem.startswith(nome_pasta)]
# if imagens_boas:
#     print('Não precisei fazer nada!')
# elif nomes_imagens:
#     # vai renomear a primeira para ficar com o nome da pasta
#     nome_imagem = nomes_imagens[0]  
#     ext = nome_imagem.split('.')[-1]
#     novo_nome = nome_pasta + '.' + ext
#     os.rename(nome_imagem, novo_nome)
#     print(nome_imagem + ' -> ' + novo_nome)
# else:
#     print('Não encontrei imagens!')
# 