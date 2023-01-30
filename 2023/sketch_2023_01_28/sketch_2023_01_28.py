# Portuguese stopwords
# https://gist.githubusercontent.com/alopes/5358189/raw/2107d809cca6b83ce3d8e04dbd9463283025284f/stopwords.txt

from random import sample

def setup():
    global palavras
    size(800, 800)
    palavras = load_strings('stopwords.txt')
    no_loop()
    text_size(40)
    fill(0)

def draw():
    for i in range(5):
        escolhas = sample(palavras, 5)
        linha = ' '.join(escolhas)
        text(linha, 100, 100 + i * 40)
        
def key_pressed():
    redraw()