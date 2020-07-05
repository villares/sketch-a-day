from os import listdir
from os.path import isfile, join

def name_image_files(base, folder):
    contents = listdir(join(base, folder))
    image_files = [f for f in contents
                   if is_img_ext(f)
                   and folder in f]
    return image_files

def is_img_ext(file_name):
    ext = file_name.split('.')[-1]
    # extensões dos formatos de imagem que o Processing aceita!
    valid_ext = ('jpg',
                 'png',
                 'jpeg',
                 'gif',
                 'tif',
                 'tga',
                 )
    return ext.lower() in valid_ext

def build_entry(image, year):
    name, ext = image.split('.')
    return """
---

![{0}]({2}/{0}/{0}.{1})

[{0}](https://github.com/villares/sketch-a-day/tree/master/{2}/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(name, ext, year)
    