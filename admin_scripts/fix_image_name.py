#!/home/villares/miniconda3/bin/python
"""
When called from the CL looks for images in CWD and renames
first found image with folder name. This might skip renaming
if some image name starts with the folder name (even images
with name equal to folder name plus appended chars, which could
be a problem).

TODO:
[X] add this to terminal aliases
[X] Where am I?
[X] Use pathlib instead of os & os.path
[ ] Test try_renaming_first_image() outside CWD
"""

from pathlib import Path
from image_helpers import is_img_ext
from tkinter import messagebox  # for debug
import sys


def try_renaming_first_image(path):
    nome_pasta = path.name
    itens_diretorio = sorted(path.iterdir())
    # Procura imagens no diretório corrente
    imagens = [item for item in itens_diretorio
                if item.is_file() and is_img_ext(item.name)]
    # Imagens boas são as que tem o mesmo nome da pasta!
    imagens_boas = [path_imagem for path_imagem in imagens
                    if path_imagem.name.startswith(nome_pasta)]
    if imagens_boas:
        print('Não precisei fazer nada!')
    elif imagens:
        # vai renomear a primeira para ficar com o nome da pasta
        primeira_imagem = imagens[0]  
        ext = primeira_imagem.suffix
        novo_nome = nome_pasta + ext
        primeira_imagem.rename(novo_nome)
        print(primeira_imagem.name + ' -> ' + novo_nome)
    else:
        print('Não encontrei imagens!')

if __name__ == '__main__':
    args = sys.argv[1:]
    if not args:
        path = Path.cwd()
    else:
        path = Path(args[0])
    if path.is_dir():
        try_renaming_first_image(path)
    else:
        novo_nome = path.parent.name + path.suffix
        path.rename(novo_nome)
        # messagebox.showinfo("arquivo renomeado para", novo_nome)

