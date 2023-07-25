import numpy as np
from PIL import Image
import py5

# https://pt.wikipedia.org/wiki/Ficheiro:Mappa_Topographico_do_Municipio_de_S%C3%A3o_Paulo_-_Folha_37,_Acervo_do_Museu_Paulista_da_USP.jpg
#img_path = '/home/villares/GitHub/sketch-a-day/2023/sketch_2023_07_21/mapa.jpg'

img_a = img_b = img_c = None

def setup():
    global img
    py5.size(1200, 400)
    img_path = 'sample.png'
    img = py5.load_image(img_path)
    img.load_np_pixels()
    print(img.np_pixels.shape)
   
def draw():
    global t
    t = py5.remap(py5.mouse_x, 0, py5.width, 0, 255)
    for i in range(3):
        img_array = img.np_pixels[:, :, i + 1]
        py5.image(apply_threshold(img_array, t, img_a), i * 400, 0, 400, 400)

def apply_threshold(img_array, threshold, dst=None):    
    new_array = np.where(img_array > threshold, 255, 0)
    return py5.create_image_from_numpy(new_array, bands='L', dst=dst)
    
def key_pressed():
    py5.save_frame(f'{t}.png')
    
py5.run_sketch()