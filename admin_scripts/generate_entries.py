#! /usr/bin/python3

# reads folder
# finds missing folders from last_done
# gets images, checks image types
# build markdown for entries
## TO DO:
# [ ] BUG FIX: GUI preview does not show the right image!
# [ ] BUG FIX: RSS feed is stikk broken
# [X] find last entry for me
# [X] insert new entries in propper place
# [/] use GUI or CL arguments to set tool
#     [X] improve GUI (add image to the dialog!)
#     [ ] add the CL arguments, why haven't you!!! (argparse!)
# [/] use GUI or CL arguments to set Markdown comments
# [ ] insert docstrings as text on .md file
# [ ] use CL arguments to commit and push README.md
# [ ] Protect against missing svglib & cairo lab? #*!todo 

import sys
from pathlib import Path
from io import BytesIO
from os import listdir
from itertools import takewhile
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM  #*!todo

from helpers import get_image_names, image_as_png_bytes

import createRSS

import PySimpleGUI as sg
sg.set_options(element_padding=(10, 10))

gui_mode = True  # default

# YEAR and base_paths to sketch-a-day folder are set manually, hard-coded
YEAR = '2023'   
USER, REPO = 'villares', 'sketch-a-day'
REPO_MAIN_URL = f'https://github.com/{USER}/{REPO}/tree/main'
RAW_CONTENT = f'https://raw.githubusercontent.com/{USER}/{REPO}/main'
# base_path = "/Users/villares/sketch-a-day" # 01046-10 previously
base_path = Path(f'/home/{USER}/GitHub/{REPO}/')
year_path = base_path / YEAR

tools = {
        'pde': '[[Processing Java](https://processing.org)]',
        'pyde': '[[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]',
        'flat': '[[Python + flat](https://xxyxyz.org/flat)]',
        'pyp5js': '[[pyp5js](https://berinhard.github.io/pyp5js/)]',
        'py5': '[[py5](https://py5coding.org/)]',
        'shoebot': '[[shoebot](http://shoebot.net/)]',
        'pyxel': '[[pyxel](https://github.com/kitao/pyxel/blob/master/README.md)]',
        'tk': '[tkinter]',
        'freecad': '[[FreeCAD](https://freecadweb.org)]',
        'pyscript': '[[pyscript](https://pyscript.net)]',
        'pysimplegui': '[[PySimpleGUI](https://www.pysimplegui.org/)]',
    }


if year_path.is_dir():
    sketch_folders = [folder.name for folder in year_path.iterdir()]
else:
    sketch_folders = []  # for the benefit of next_day.py
    print(f"{__file__}: Couldn't find the sketch-a-day year folder!")

readme_path = base_path / 'docs' / 'README.md'

def most_recent_entry(readme_as_lines):
    entry_images = (
        line[line.find(YEAR) : line.find(']')]
        for line in readme_as_lines
        if '![' in line
    )
    try:
        return next(entry_images)[:10]
    except StopIteration:
        return 'Something wrong. No dated images found!'
    
def main(args):

    # open the readme markdown index
    with open(readme_path, 'rt') as readme:
        readme_as_lines = readme.readlines()
    # find date of the first image seen in the readme
    last_done = most_recent_entry(readme_as_lines)
    print('Last entry: ' + last_done) # add popup?
    # find folders after the last_done one (folders start with ISO date)
    rev_sorted_folders = sorted(sketch_folders, reverse=True)
    not_done = lambda f: last_done not in f
    new_folders = [folder for folder in takewhile(not_done, rev_sorted_folders)]
    # find insertion point
    insert_point = 3 # in case lines is empty
    for insert_point, line in enumerate(readme_as_lines):
        if last_done in line:
            break
    # iterate on new folders
    for folder in reversed(new_folders):
        imgs = get_image_names(year_path, folder)
        # insert entry if matching image found
        for img in imgs:
            tool = comment = None
            if img.split('.')[0].startswith(folder):
                if gui_mode:
                    tool, comment = ask_tool_comment(folder, img)
                entry_text = build_entry(folder, img, tool, comment)
                readme_as_lines.insert(insert_point - 3, entry_text)
                print('Adding: ' + folder)
                #if gui_mode: sg.popup('Adding', folder)
                break
    # overwrite the readme markdown index
    with open(readme_path, 'wt') as readme:
        content = ''.join(readme_as_lines)
        readme.write(content)

def ask_tool_comment(folder, img):
    image_path = year_path / folder / img
    if img.lower().endswith('svg'):  #*!todo
        drawing = svg2rlg(image_path)
        cur_width, cur_height = drawing.width, drawing.height
        dpi = min(600 / cur_height * 72, 600 / cur_width * 72)
        io_bytes = BytesIO()
        renderPM.drawToFile(drawing, io_bytes, fmt="PNG", dpi=dpi)
        png_bytes = io_bytes.getvalue()
    else:
        png_bytes, metadata = image_as_png_bytes(image_path, (600, 600)) #, resize=new_size)
    window = sg.Window(f'{img}', [
        [sg.Image(key='-IMAGE-', data=png_bytes)],
        [sg.T('Tool   '), sg.Combo(list(tools), default_value='py5', s=(40,22), k='-TOOL-')],
        [sg.T('Comment'), sg.Multiline(key='-COMMENT-', s=(40,4))],
        [sg.B('OK'), sg.B('Cancel')]
        ],font='Fixedsys')
#    window['-IMAGE-'].update(data=png_bytes)
    event, values = window.read(close=True)    
    if event == 'Cancel':
        exit()
    return values['-TOOL-'], values['-COMMENT-']

def build_entry(folder, image_filename, tool=None, comment=None):
    """
    Return a string with markdown formated
    for the sketch-a-day index page entry
    of image (for a certain year).
    """
    folder_path = year_path / folder
    if not tool:
        tools_mentioned = (t for t in tools.keys() if t in image_filename.lower())
        try:
            tool = next(tools_mentioned)
        except StopIteration:
            tool = 'py5'
            for f in listdir(folder_path):
                if 'pyde' in f:
                    tool = 'pyde'
                elif 'pde' in f:
                    tool = 'pde'
    
    if comment is None:
        docstring = search_docstring(folder_path)
        if docstring:
            comment = '\n\n' + docstring
        else:
            comment = ''
    else:
        comment = '\n\n' + comment
        
    link = f'{REPO_MAIN_URL}/{YEAR}/{folder}'
    
    return f"""
---

### {folder}

![{folder}]({RAW_CONTENT}/{YEAR}/{folder}/{image_filename})

[{folder}]({link}) {tools.get(tool,'['+tool+']')}{comment}
"""

def search_docstring(folder):
    """
    Not implemented yet.
    """
    return None


if __name__ == '__main__':
    args = sys.argv[1:]
    if '-nogui' in args or '-NG' in args:
        gui_mode = False
    # print(sys.version_info)
    main(args)
    createRSS.main([
        'README.md',
        '2022.md',
        ])
