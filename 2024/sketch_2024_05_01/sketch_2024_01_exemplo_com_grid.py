imagens = []
w, h = 80, 55  # largura e altura do espaço para cada imagem

def setup():
    global colunas, linhas
    size(880, 550)
    colunas, linhas = width // w, height // h
    print(f'Posições na grade: {colunas * linhas}')

def draw():
    background(0)
    # Desenha grade com `imagens` com colunas fixas de largura `w`,
    # imagens mais largas são sobrepostas pela pr
    contador = 0
    for c in range(colunas):
        x=c * w
        for l in range(linhas):
            y=l * h
            if contador < len(imagens):
                nome, img = imagens[contador]
                fator = h / img.height
                image(img, x, y, img.width * fator, img.height * fator)
                contador += 1
                
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
            img = load_image(caminho_imagem)
            print(f'imagem {caminho_imagem.name} carregada.')
            imagens.append((caminho_imagem.name, img))
        print(f'Número de imagens: {len(imagens)}')

def lista_imagens(caminho_pasta):
    """
    Devolve uma a lista dos caminhos (objetos pathlib.Path) dos arquivos com 
    extensões de imagem no nome, encontrados iterando itens de `caminho_pasta`.
    """
    caminho_pasta = Path(caminho_pasta) # Garante um objeto pathlib.Path
    extensoes_validas = ('.jpg', '.png', '.jpeg', '.gif', '.tif', '.tga')
    lista_caminhos = []
    try:
        for caminho_imagem in caminho_pasta.iterdir():
            if caminho_imagem.is_file() and caminho_imagem.suffix.lower() in extensoes_validas:
                lista_caminhos.append(caminho_imagem)
    except Exception as e:
        print(e)
    return lista_caminhos