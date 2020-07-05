from os import listdir
from os.path import isfile, join

def get_image_files(base, folder):
    """
    returns a list of image files from
    a directory named folder at base/folder
    but only if name contains the folder name        
    """    
    contents = listdir(join(base, folder))
    image_files = [f for f in contents
                   if is_img_ext(f)
                   and folder in f]
    return image_files

def is_img_ext(file_name):
    """
    checks if file_name ends with
    one of the valid_ext extensions
    """ 
    ext = file_name.split('.')[-1]
    valid_ext = ('jpg',
                 'png',
                 'jpeg',
                 'gif',
                 'tif',
                 'tga',
                 )
    return ext.lower() in valid_ext

def build_entry(image, year):
    """
    returns a string with markdown formated
    for the sketch-a-day index page entry
    of image (for a certain year)
    """ 
    name, ext = image.split('.')
    return """
---

![{0}]({2}/{0}/{0}.{1})

[{0}](https://github.com/villares/sketch-a-day/tree/master/{2}/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(name, ext, year)
    