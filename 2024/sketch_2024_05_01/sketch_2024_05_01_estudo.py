from pathlib import Path

imagens = []  # lista vazia que vai receber tuplas (nome-string, objetos-Py5Image)

def setup():
    size(500, 500)
        
def draw():
    pass

def key_pressed():
    if key == 'o':
        select_folder("Selecione uma pasta", carregar_imagens)
    if key == ' ':
        imagens[:] = []  # esvazia a lista de imagens

def carregar_imagens(caminho_pasta):
    if caminho_pasta == None:
        print('Seleção cancelada.')
    else:
        print(f'Pasta selecionada: {caminho_pasta.name}')
        for caminho_imagem in lista_imagens(caminho_pasta):
            img = load_image(caminho_imagem)
            print(f'imagem {caminho_imagem.name} carregada.')
            imagens.append((caminho_imagem.name, img))
        print(f'Número de imagens: {len(imagens)}')
        
def lista_imagens(caminho):
    extensoes_validas = ('.jpg', '.png', '.jpeg', '.gif', '.tif', '.tga')
    lista_caminhos = []
    if caminho.is_file() and caminho.suffix.lower() in extensoes_validas:
        lista_caminhos.append(caminho)
    elif caminho.is_dir():
        for item in caminho.iterdir():
            lista_caminhos.extend(lista_imagens(item))
    return lista_caminhos
