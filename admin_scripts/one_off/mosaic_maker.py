#!/home/villares/miniconda3/bin/python
from random import sample, seed
from os import listdir
from pathlib import Path

from PIL import Image

MAX_IMAGES = 37
RND_SEED = 3
width, height = 1200, 1200 # final image size
thumb_size = (200, 200)
YEAR = "2022"
base_path = Path("/home/villares/GitHub/sketch-a-day/")
year_path = base_path / YEAR
folders = sorted(year_path.iterdir())

def has_image_ext(file_name):
    """
    Return True if file_name ends with
    one of the valid_extensions.
    """
    valid_extensions = (
        'jpg',
        'png',
        'jpeg',
        'gif',
        'tif',
        'tga',
#        'svg',
    )
    extension = Path(file_name).suffix.lower()[1:]
    return extension in valid_extensions

def save_mosaic(folders):
    images = []
    for folder in folders:
        f_images = [f for f in folder.iterdir() if has_image_ext(f)
                    and folder.name in f.name]
        if f_images and not f_images[0].name.lower().endswith('svg'):
            img_path = folder / f_images[0]
            img = Image.open(img_path)
            if img.format == 'GIF' and img.is_animated:
                continue # skip GIFs... 
            images.append(img)
           
    bg = Image.new('RGB',
                   (width, height),
                   (0, 0, 0))
    seed(RND_SEED)
    images_sample = sample(images, MAX_IMAGES)

    x = y = n = 0
    #N = None # degub with 5
    #for img in images[:N]:
    for img in images_sample:
        img.thumbnail(thumb_size, Image.Resampling.BICUBIC)    
        bg.paste(img, (x, y))
        n += 1
        x += thumb_size[0]
        if x >= width:
            x = 0
            y += thumb_size[1] # fixed height
        if n == MAX_IMAGES or y >= height:
            break
        
    bg.save(f'{n}_images_from_{YEAR}.png')
    
save_mosaic(folders)
        
