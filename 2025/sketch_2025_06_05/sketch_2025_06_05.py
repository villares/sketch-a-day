from pathlib import Path
from random import randint
import io

from PIL import Image

caminho_imagem = 'Apiscina.jpg'
lista_bytes = []
py5image = None

def setup():
    global py5image  # para poder salvar!
    size(800, 400)
    #window_resizable(True) # acho que está com problema se usado com no_loop()!
    #frame_rate(1)
    no_loop()
    carregando_bytes_imagem(caminho_imagem)
    
def carregando_bytes_imagem(imagem):
    global lista_bytes
    try:
        with open(imagem, 'rb') as f:
            lista_bytes = list(f.read())
    except Exception as e:
        print(e)

def draw():
    global py5image
    background(0)
    if lista_bytes:
        comprimento = len(lista_bytes)
        bytes_anteriores = lista_bytes.copy()
        for _ in range(10):
            pos = randint(0, comprimento)
            novo_byte = randint(1, 255)
            lista_bytes[pos] = novo_byte
        stream = io.BytesIO(bytes(lista_bytes))
        try:
            nova_imagem = Image.open(stream)
            py5image = convert_image(nova_imagem)
        except OSError as e:
            lista_bytes[:] = bytes_anteriores
            print(e)
        mostra_imagem()
 
def mostra_imagem():
    if py5image:
        ar = py5image.height / py5image.width        
        nova_largura = height / ar
        if nova_largura > width:
            image(py5image, 0, 0, width, height * ar)
        else:        
            image(py5image, 0, 0, nova_largura, height)
 
def arquivo_selecionado(selection):
    global caminho_imagem
    if selection is None:
        println("Não foi selecionado nenhum arquivo.")
    else:
        (f'Selecionado o arquivo: {selection}')
        caminho_imagem = selection
        carregando_bytes_imagem(caminho_imagem)
        redraw()
        
def key_pressed():
    if key == ' ':
        redraw()
    if key == 's':
        nome = f'{caminho_imagem.stem}-glitch{frame_count}.jpg'
        py5image.save(nome)
        print(f'salvando {nome}')
    if key == 'r':
       carregando_bytes_imagem(caminho_imagem)
       redraw()
    if key == 'i':
       select_input("Selecione uma imagem:", arquivo_selecionado)

