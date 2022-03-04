# -*- coding: UTF-8 -*-

# From https://github.com/villares/villares/blob/main/file_helpers.py

# 2020-09-25 Added comment with date and URL!
# 2020-11-28 Added sketch_name()
# 2020-12-02 Renamed file_helpers -> helpers, brought in grid() and color.py in
# 2020-12-04 Brought in triangle_area, rect_points, rotate_point, point_in_screen
# 2021-01_26 Reverted 2020-12-04
# 2021_03_05 imgext() -> has_img_ext()
# 2021_06_08 added lerp_tuple()

try:
    lerp
except NameError:
    from py5 import lerp

def adicionar_imagens(selection, imagens=None):
    if imagens is None:
	    imagens = []
    if selection == None:
        print("Seleção cancelada.")
    else:
        dir_path = selection.getAbsolutePath()
        print("Pasta selecionada: " + dir_path)
        for file_name, file_path in lista_imagens(dir_path):
            img = loadImage(file_path)
            img_name = file_name.split('.')[0]
            print("imagem " + img_name + " carregada.")
            imagens.append((img_name, img))
        print('Número de imagens: ' + str(len(imagens)))
    return imagens

def lista_imagens(dir=None):
    """
    Devolve uma a lista de tuplas com os nomes dos arquivos de imagem e os caminhos
    completos para cada uma das images na pasta `dir` ou na pasta /data/ do sketch.
    Requer a função has_image_ext() para decidir quais extensões aceitar.
    """
    from os import listdir
    from os.path import isfile, join
    data_path = dir or sketchPath('data')  # will return error later if no data folder!
    try:
        f_list = [(f, join(data_path, f)) for f in listdir(data_path)
                  if isfile(join(data_path, f)) and has_image_ext(f)]
    except Exception as e:
        print("Erro ({0}): {1}".format(e.errno, e.strerror))
        return []
    return f_list

def has_image_ext(file_name):
        # extensões dos formatos de imagem que o Processing aceita!
        valid_ext = ('jpg', 'png', 'jpeg', 'gif', 'tif', 'tga')
        file_ext = file_name.split('.')[-1]
        return file_ext.lower() in valid_ext

imgext = has_image_ext 

def sketch_name():
    """Return sketch name."""
    from os import path
    sketch = sketchPath()
    return path.basename(sketch)

def random_hue_saturated(bright=None):
    bright = 255 if bright is None else bright
    with pushStyle():
        colorMode(HSB)
        return color(random(256), 255, bright)

def hex_color(s):
    """
    This function allows you to create color from a string with hex notation in Python mode.
    
    On "standard" Processing (Java) we can use hexadecimal color notation #AABBCC
    On Python mode one can use this notation between quotes, as a string in fill(),
    stroke() and background(), but, unfortunately, not with color().
    """
    if s.startswith('#'):
        s = s[1:]
    return color(int(s[:2], 16), int(s[2:4], 16), int(s[4:6], 16))

                
def grid(cols, rows, colSize=1, rowSize=1):
    """
    Returns an iterator that provides coordinate tuples. Example:
    # for x, y in grid(10, 10, 12, 12):
    #     rect(x, y, 10, 10)
    """
    rowRange = range(int(rows))
    colRange = range(int(cols))
    for y in rowRange:
        for x in colRange:
            yield (x * colSize, y * rowSize)

def lerp_tuple(a, b, t):   
    return tuple(lerp_tuple(ca, cb, t) if isinstance(ca, tuple)
                 else lerp(ca, cb, t)             
                 for ca, cb in zip(a, b))
                                    
def memoize(f):
    """Naive memoization."""
    memo = {}
    def memoized_func(*args, **kwargs):
        if args not in memo:
            r = f(*args, **kwargs)
            memo[args] = r
            return r
        return memo[args]
    return memoized_func
