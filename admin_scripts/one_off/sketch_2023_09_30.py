import PIL.Image
import py5

from zipfile import ZipFile

def setup():
    py5.size(896, 768)
    y = x = 0
    icon_imgs = {}
    with ZipFile('icons.zip') as icons:
        for f in sorted(icons.namelist()[1:]):
            img = PIL.Image.open(icons.open(f))
            py5image = py5.convert_image(img)
            py5.image(py5image, x, y)
            suf = f.split('/')[1].split('.')[0]
            print(suf)
            icon_imgs[suf] = py5image
            x += 64
            if x > py5.width - 64:
                x = 0
                y += 64
            
py5.run_sketch()