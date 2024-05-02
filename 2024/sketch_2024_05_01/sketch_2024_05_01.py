imagens = []

h = 125

def setup():
    global colunas, linhas
    size(750, 625)

def draw():
    background(0)
    x = y = 0
    for nome, img in reversed(imagens):
        fator = h / img.height
        if x + img.width * fator > width:
            x=0
            y += h
        image(img, x, y, img.width * fator, img.height * fator)
        x += img.width * fator
                
    if not imagens:   # if len(imagens) == 0:
        text_size(20)
        text("aperte 'o' para selecionar uma pasta\n"  # note ausência da vírgula aqui
             "aperte a barra de espaço para limpar a grade",
             100, 100)

def key_pressed():
    if key == 'o':
        select_folder("Selecione uma pasta", adicionar_imagens)
    if key == ' ':
        imagens[:] = []  # esvazia a lista de imagens
    if key == 'p':
        save_frame('####.png')

def adicionar_imagens(caminho_pasta):
    """Callback que será chamado pela função select_folder() do py5"""
    if caminho_pasta == None:
        print('Seleção cancelada.')
    else:
        print(f'Pasta selecionada: {caminho_pasta.name}')
        for caminho_imagem in lista_imagens(caminho_pasta):
            try:
                img = load_image(caminho_imagem)
                print(f'imagem {caminho_imagem.name} carregada.')
                imagens.append((caminho_imagem.name, img))
            except Exception as erro:
                print(f'*{erro}*')
                break 
        print(f'Número de imagens: {len(imagens)}')

def lista_imagens(caminho):
    """
    Devolve uma a lista dos caminhos (objetos pathlib.Path) dos arquivos com 
    extensões de imagem no nome, encontrados iterando itens de `caminho_pasta`.
    """
    extensoes_validas = ('.jpg', '.png', '.jpeg', '.gif', '.tif', '.tga')
    if caminho.is_dir():
        lista_caminhos = []
        for item in caminho.iterdir():
            lista_caminhos.extend(lista_imagens(item))
        return lista_caminhos
    elif caminho.is_file() and caminho.suffix.lower() in extensoes_validas:
        return [caminho]
    else:
        return []