# from __future__ import unicode_literals

circulos = []

def setup():
    size(400, 400)
    fill(100, 100, 255)
    println(u"Tecle 'W' para gravar e 'L' para carregar dados de um arquivo texto")

def draw():    
    background(0)
    for circulo in circulos:
        x, y, tamanho = circulo
        ellipse(x, y, tamanho, tamanho)

def mouseDragged():
    circulo = (mouseX, mouseY, random(20, 40))
    circulos.append(circulo)

def keyPressed():
    if key =='w' or key == 'W':
        selectOutput("Salvar como:", "salvar_circulos")   # Argumentos: título, função chamada na conclusão           
    if key == 'l' or key == 'L':
        selectInput("Escolha um arquivo:", "carregar_circulos")      
    if key == ' ':
        circulos[:] = []
    if key == 's':
        saveFrame("sketch_2020_05_03a.png")

def salvar_circulos(arquivo):
    if arquivo == None:
        print("Gravação cancelada.")
    else:
        path_arquivo = arquivo.getAbsolutePath()
        if not path_arquivo.endswith('.txt'):
            path_arquivo += '.txt'
        linhas = []
        for circulo in circulos:
                x, y, tamanho = circulo
                linhas.append(u'{} {} {}'.format(x, y, tamanho))            
        saveStrings(path_arquivo, linhas)    

def carregar_circulos(arquivo):
    if arquivo == None:
        print(u"Seleção cancelada.")
    else:
        path_arquivo = arquivo.getAbsolutePath()
        print("Arquivo selecionado: " + path_arquivo)
        linhas = loadStrings(path_arquivo)
        for linha in linhas:
            str_x, str_y, str_tamanho = linha.split()
            circulo = float(str_x), float(str_y), float(str_tamanho)
            circulos.append(circulo) 

            
        # from io import open # usando este quebra
        # if not path_arquivo.endswith('.txt'):
        #     path_arquivo += '.txt'
        # with open(path_arquivo, 'w') as f:  # acrescentando encoding='utf-8' quebra :(
        #     # print file_out <_io.TextIOWrapper name=u'/home/villares/a.txt' 
        #     for circulo in circulos:
        #         x, y, tamanho = circulo
        #         f.write('{} {} {} #é\n'.format(x, y, tamanho))
