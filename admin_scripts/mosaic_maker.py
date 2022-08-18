#! /usr/bin/python3

from os import listdir
from os.path import isfile, join

from PIL import Image

from helpers import get_image_names, remove_transparency

YEAR = "2022"
base_path = "/home/villares/GitHub/sketch-a-day/"
year_path = join(base_path,YEAR)
folders = listdir(year_path)


images = []
for folder in sorted(folders):
    folder_path = join(year_path, folder)
    f_images = get_image_names(year_path, folder)
    if f_images and not f_images[0].lower().endswith('svg'):
        img_path = join(folder_path, f_images[0])
        img = Image.open(img_path)
        if img.format == 'GIF' and img.is_animated:
            continue
        images.append(img)
        
thumb_size = (200, 200)
x = y = 0
bg = Image.new('RGB',
               (1200, 1200),
               (0, 0, 0))

#n = None # degub with 5
#for img in images[:n]:
from random import sample, seed
seed(3)
images_sample = sample(images, 80)
print(len(images_sample))

for img in images_sample:
    img.thumbnail(thumb_size, Image.Resampling.BICUBIC)    
    bg.paste(img, (x, y))
    x += 200
    if x >= 2000:
        x = 0
        y += 200
    if y == 1200:
        break
    
bg.save('36from{}.png'.format(YEAR))
    

        
