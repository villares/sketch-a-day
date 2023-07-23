import numpy as np
import cv2
import matplotlib.pyplot as plt

# https://pt.wikipedia.org/wiki/Ficheiro:Mappa_Topographico_do_Municipio_de_S%C3%A3o_Paulo_-_Folha_37,_Acervo_do_Museu_Paulista_da_USP.jpg
img_path = '/home/villares/GitHub/sketch-a-day/2023/sketch_2023_07_21/mapa.jpg'

def apply_threshold(img_array, threshold):
    threshold_applied = []
    for row in img_array:
        threshold_applied.append([])
        for pixel in row:
            if pixel>threshold:
                threshold_applied[len(threshold_applied)-1].append([255, 255, 255])
            else:
                threshold_applied[len(threshold_applied)-1].append([0, 0, 0])
    new_img = np.array(threshold_applied, np.uint8)
    cv2.imwrite(str(threshold)+".jpg", new_img)

img = cv2.imread(img_path, 0)
apply_threshold(img, 210)