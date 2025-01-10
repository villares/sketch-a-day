#!/home/villares/thonny-env/bin/python

"""
When called from the CL looks for images in CWD and renames
first found image with folder name. This might skip renaming
if some image name starts with the folder name (even images
with name equal to folder name plus appended chars, which could
be a problem).

TODO:
[X] add this to terminal aliases
[X] Where am I?
[X] Use pathlib instead of os & os.path
[ ] Test try_renaming_first_image() outside CWD
"""

from pathlib import Path
from tkinter import messagebox  # for debug
import sys


def try_renaming_first_image(path):
    dir_name = path.name
    # Filter images from directory;
    imgs = [item for item in sorted(path.iterdir())
            if item.is_file() and is_img_ext(item.name)]
    # "Good names" start with the directory name (even if not the same)!
    good_names = [path_imagem for path_imagem in imgs
                  if path_imagem.name.startswith(dir_name)]
    if good_names:
        print('You already have some good image names!')
    elif imgs:
        # vai renomear a primeira para ficar com o nome da pasta
        first_found_image = imgs[0]  
        ext = first_found_image.suffix
        new_name = dir_name + ext
        first_found_image.rename(new_name)
        print(f'{first_found_image.name}  -> {new_name}')
    else:
        print('No images found!')


def is_img_ext(file_name):
    """
    Return True if file_name ends with some
    image-like extensions (add/remove the ones you like).
    """
    return Path(file_name).suffix.lower() in (
        '.jpg', '.jpeg', '.png',
        '.tif', '.tiff', '.tga',
        '.gif', '.webp', '.svg', 
    )

if __name__ == '__main__':
    args = sys.argv[1:]
    if not args:
        path = Path.cwd()
    else:
        path = Path(args[0])
    if path.is_dir():
        try_renaming_first_image(path)
    else: # will rename file passed as argumen 
        new_name = path.parent.name + path.suffix
        path.rename(new_name)
        # messagebox.showinfo(f'{first_found_image.name}  -> {new_name}')

