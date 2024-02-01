#!/home/villares/miniconda3/bin/python

from pathlib import Path

from PIL import Image, GifImagePlugin

from image_helpers import get_image_names, remove_transparency

YEAR = '2024'
base_path = Path('/home/villares/GitHub/sketch-a-day/')
year_path = base_path / YEAR

images = []
for folder in sorted(year_path.iterdir()):
    f_images = get_image_names(year_path, folder.name)
    if f_images:
        img_path = folder / f_images[0]
        images.append(Image.open(img_path))
        
thumb_size = (800, 400)
n = None # degub with 5
thumbs = []
for img in images[:n]:

    if img.format == 'GIF' and img.is_animated:
        p = img.getpalette()
        img.seek(img.n_frames // 2)
        if not img.getpalette():
            try:
                img.putpalette(p)
            except ValueError:
                pass
        img = img.convert('RGBA')
        print('gif')
        
    img.thumbnail(thumb_size, Image.BICUBIC)
    img = remove_transparency(img)
    
    bg = Image.new('RGB', thumb_size, (0, 0, 0))
    print(img.size)
    iw, bw = img.size[0], bg.size[0]
    if  iw < bw:
        x = (bw - iw) // 2
    else:
        x = 0
    ih, bh = img.size[1], bg.size[1]
    if  ih < bh:
        y = (bh - ih) // 2
    else:
        y = 0     
    bg.paste(img, (x, y))
    thumbs.append(bg)

thumbs[0].save('export{}.gif'.format(YEAR),
               save_all=True, append_images=thumbs,
               optimize=True,
               duration=500,
               loop=0)
    

        
