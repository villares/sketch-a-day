from os import listdir
from os.path import join


def get_image_names(base, folder, word=None):
    """
    Return a list of image names from a directory
    named folder at base/folder by default only
    if name contains the folder name.
    Use word='' to get any images, irrespective of name.
    """
    word = word if word is not None else folder
    contents = listdir(join(base, folder))
    image_files = [f for f in contents if is_img_ext(f) and word in f]
    return image_files


def is_img_ext(file_name):
    """
    Return True if file_name ends with
    one of the valid_extensions.
    """
    ext = file_name.split('.')[-1]
    valid_extensions = (
        'jpg',
        'png',
        'jpeg',
        'gif',
        'tif',
        'tga',
        'svg',
    )
    return ext.lower() in valid_extensions


def remove_transparency(im, bg_colour=(255, 255, 255)):
    from PIL import Image

    # Only process if image has transparency (http://stackoverflow.com/a/1963146)
    if im.mode in ('RGBA', 'LA') or (
        im.mode == 'P' and 'transparency' in im.info
    ):

        # Need to convert to RGBA if LA format due to a bug in PIL (http://stackoverflow.com/a/1963146)
        alpha = im.convert('RGBA').split()[-1]

        # Create a new background image of our matt color.
        # Must be RGBA because paste requires both images have the same format
        # (http://stackoverflow.com/a/8720632  and  http://stackoverflow.com/a/9459208)
        bg = Image.new('RGBA', im.size, bg_colour + (255,))
        bg.paste(im, mask=alpha)
        return bg

    else:
        return im
