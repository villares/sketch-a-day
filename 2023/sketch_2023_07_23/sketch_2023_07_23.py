import numpy as np
from PIL import Image
import py5

# https://pt.wikipedia.org/wiki/Ficheiro:Mappa_Topographico_do_Municipio_de_S%C3%A3o_Paulo_-_Folha_37,_Acervo_do_Museu_Paulista_da_USP.jpg
#img_path = '/home/villares/GitHub/sketch-a-day/2023/sketch_2023_07_21/mapa.jpg'

def setup():
    global temp_img
    py5.size(800, 800)
    img_path = 'sample.png'
    img = py5.load_image(img_path)
    temp_img = py5.create_image(img.width, img.height, py5.RGB)

    for n in range(5, 23):
        apply_threshold(img, n * 10)



def apply_threshold(img, threshold):
    img.load_np_pixels()
    img_array = img.np_pixels
    new_array = np.where(img_array > threshold, 255, 0)
    temp_img.set_np_pixels(new_array, bands='RGB')
    temp_img.save(f'{threshold}.png')

    
py5.run_sketch()