#!/home/villares/thonny-env/bin/python

"""
When called from the CL looks for images in CWD and renames the
first found image stem to the folder name. By design this will skip
renaming if some image has name that starts with the folder name,
like "folder name plus appended chars", so beware!

This can also be used to rename non-image files if they are passed as
arguments.
"""

# from tkinter import messagebox  # for debugging only
from pathlib import Path
import sys

def try_renaming_first_image(path):
    dir_name = path.name
    # Get image looking files from directory
    imgs = [item for item in sorted(path.iterdir())
            if item.is_file() and is_img_ext(item.name)]
    # "Good names" are those that start with the directory name!
    good_names = [path_imagem for path_imagem in imgs
                  if path_imagem.name.startswith(dir_name)]
    if good_names:
        print('You already have some good image names!')
    elif imgs:
        # Vai renomear a primeira imagem para ficar com o nome da pasta
        # e não tem checagem de sobreescrever pois se houvesse uma
        # imagem com o mesmo nome teria aparecido em good_names!
        first_found_image = imgs[0]  
        new_name = dir_name + first_found_image.suffix
        first_found_image.rename(new_name)
        print(f'{first_found_image.name} -> {new_name}')
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
        path = Path(args[0]).resolve()
        if not path.exists():
            print('Invalid argument.')
            exit()
    if path.is_dir():
        try_renaming_first_image(path)
    else: # will rename file passed as argument
        new_name = path.parent.name + path.suffix
        if (path.parent / new_name).exists():
            print('There was a file already with the new name, nothing was done.')
        else:        
            path.rename(new_name)
            print(f'{path.name}  -> {new_name}')
        # messagebox.showinfo('', f'{path.name} -> {new_name}')

