from __future__ import unicode_literals , division

imagens = []
w, h = 80, 55

def setup():
    global colunas, linhas
    size(880, 550)
    colunas, linhas = width // w, height // h
    print('Posições na grade: ' + str(colunas * linhas))
    
def draw():
    background(0)
    contador = 0
    # Desenha uma grade com as imagens na lista `imagens`
    for c in range(colunas):
        x = c * w
        for l in range(linhas):
            y = l * h
            if contador < len(imagens):
                img = imagens[contador][1]
                fator = h / img.height
                image(img, x, y, img.width * fator, img.height * fator)
                contador += 1
    
def keyPressed():
    if key == 'o':
        selectFolder("Selecine uma pasta:", "adicionar_imagens")
    if key == ' ':
        imagens[:] = []
    if key == 'p':
        saveFrame('####.png')

def adicionar_imagens(selection):
    if selection == None:
        print("Seleção cancelada.")
    else:
        dir_path = selection.getAbsolutePath()
        print("Pasta selecionada: " + dir_path)
        for file_name, file_path in lista_imagens(dir_path):
            img = loadImage(file_path)
            img_name = file_name.split('.')[0]
            print("imagem " + img_name + " carregada.")
            imagens.append((img_name, img))
        print('Número de imagens: ' + str(len(imagens)))


def lista_imagens(dir=None):
    """
    Devolve uma a lista de tuplas com os nomes dos arquivos de imagem e os caminhos
    completos para cada uma das images na pasta `dir` ou na pasta /data/ do sketch.
    Requer a função imgext() para decidir quais extensões aceitar.
    """
    from os import listdir
    from os.path import isfile, join
    data_path = dir or sketchPath('data')
    try:
        f_list = [(f, join(data_path, f)) for f in listdir(data_path)
                  if isfile(join(data_path, f))
                  and imgext(f)]
    except Exception as e:
        print("Erro ({0}): {1}".format(e.errno, e.strerror))
        return []
    # print f_list
    return f_list

def imgext(file_name):
    extensions = ('.jpg',
                  '.png',
                  '.jpeg',
                  '.gif',
                  '.tif',
                  '.tga',
                  )
    for ext in extensions:
        if file_name.endswith(ext):
            return True
    return False
