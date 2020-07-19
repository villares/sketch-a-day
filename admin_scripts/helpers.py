from os import listdir
from os.path import isfile, join

def get_image_names(base, folder, word=None):
    """
    Return a list of image names from a directory
    named folder at base/folder by default only
    if name contains the folder name.        
    """
    word = word or folder
    contents = listdir(join(base, folder))
    image_files = [f for f in contents
                   if is_img_ext(f)
                   and word in f]
    return image_files

def is_img_ext(file_name):
    """
    Return True if file_name ends with
    one of the valid_ext extensions.
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
    Return a string with markdown formated
    for the sketch-a-day index page entry
    of image (for a certain year).
    """ 
    name, ext = image.split('.')
    return """
---

![{0}]({2}/{0}/{0}.{1})

[{0}](https://github.com/villares/sketch-a-day/tree/master/{2}/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(name, ext, year)

def remove_transparency(im, bg_colour=(255, 255, 255)):
    from PIL import Image
    # Only process if image has transparency (http://stackoverflow.com/a/1963146)
    if im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info):

        # Need to convert to RGBA if LA format due to a bug in PIL (http://stackoverflow.com/a/1963146)
        alpha = im.convert('RGBA').split()[-1]

        # Create a new background image of our matt color.
        # Must be RGBA because paste requires both images have the same format
        # (http://stackoverflow.com/a/8720632  and  http://stackoverflow.com/a/9459208)
        bg = Image.new("RGBA", im.size, bg_colour + (255,))
        bg.paste(im, mask=alpha)
        return bg

    else:
        return im
    
