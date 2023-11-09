from pathlib import Path

pasta_inicial = Path.cwd() # Current Working Directory

def parece_imagem(file_name):
    extensoes_validas = (
        'jpg',
        'png',
        'jpeg',
        'gif',
        'tif',
        'tga',
        'svg',
    )
    ext = Path(file_name).suffix.lower()[1:]
    return ext in extensoes_validas

def lista_imagens(pasta):
    """
    Recebe um path de uma pasta/diretório/folder
    devolve uma lista de paths das imagens de dentro.
    """
    imagens = []
    # andar pela pasta    
    for item in sorted(pasta.iterdir()):  # Iterate over directory
        if parece_imagem(item):
            imagens.append(item)
            #print('achei uma imagem')
        elif item.is_dir():
            #print('achei uma sub-pasta')
            sub_imagens = lista_imagens(item)
            # imagens.extend(sub_imagens)
            for sub_imagem in sub_imagens:
                imagens.append(sub_imagem)
    return imagens

caminhos = lista_imagens(pasta_inicial)
for c in caminhos:
    print(c.parent.name, c.name)

    