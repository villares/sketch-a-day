#!/home/villares/thonny-env/bin/python

# reads folder
# finds missing folders from last_done
# gets images, checks image types
# build markdown for entries
## TO DO:
# [ ] BUG FIX: GUI preview does not show the right image!
# [ ] BUG FIX: RSS feed is still broken
# [X] find last entry for me
# [X] insert new entries in propper place
# [/] use GUI or CL arguments to set tool
#     [X] improve GUI (add image to the dialog!)
#     [ ] add the CL arguments, why haven't you!!! (argparse!)
# [/] use GUI or CL arguments to set Markdown comments
# [ ] insert docstrings as text on .md file
# [ ] use CL arguments to commit and push README.md
# [ ] Protect against missing svglib & cairo lab? #*!todo
# [x] Added clumsy mastodon posting
# 2024
# Added a call to generate_index_for_logseq.py
# 2025
# Updated image_helpers to use pathlib...

import sys
from pathlib import Path
from io import BytesIO
from os import listdir
from itertools import takewhile
from time import sleep

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM  #*!todo

import FreeSimpleGUI as sg
sg.set_options(element_padding=(10, 10))

from image_helpers import get_image_names, image_as_png_bytes
from toot_publisher import toot
from generate_index_for_logseq import generate_sketch_a_day_index

print(f'Running on: {sys.executable}') # for debug

gui_mode = True  # default

# YEAR and base_paths to sketch-a-day folder are set manually, hard-coded
YEAR = '2025'   
USER, REPO = 'villares', 'sketch-a-day'
MAIN_SITE = 'https://abav.lugaralgum.com/sketch-a-day'
SPONSOR_LINK = 'https://www.paypal.com/donate/?hosted_button_id=5B4MZ78C9J724'
REPO_MAIN_URL = f'https://github.com/{USER}/{REPO}/tree/main'
RAW_CONTENT = f'https://raw.githubusercontent.com/{USER}/{REPO}/main'
TOOT_DEFAULT = (
    'Code at: {}\n'
    f'More sketch-a-day: {MAIN_SITE}\n'
    f'If you like this, support my work: {SPONSOR_LINK}\n'
    )
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
        'freesimplegui': '[[FreeSimpleGUI](https://github.com/spyoungtech/FreeSimpleGui)]',
        'raylib-python':'[[raylib-python](https://electronstudio.github.io/raylib-python-cffi/README.html)]',
        'ursina': '[[ursina](https://www.ursinaengine.org/)]',
    }

tag_dict = {'py5': '#Processing #Python #py5 #CreativeCoding' }

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
    global last_done_message
    change_log = []
    # open the readme markdown index
    with open(readme_path, 'rt') as readme:
        readme_as_lines = readme.readlines()
    # find date of the first image seen in the readme
    last_done = most_recent_entry(readme_as_lines)
    last_done_message = 'Last entry: ' + last_done
    print(last_done_message)
    change_log.append(last_done_message)
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
            comment = description = None
            default_tool = 'py5'
            if img.name.startswith(folder):
                if gui_mode:
                    dialog_result = ask_tool_comment(folder, img, default_tool)
                    tool, comment, do_toot, image_caption, toot_text = dialog_result
                entry_text = build_entry(folder, img, tool, comment, image_caption)
                if do_toot:
                    image_path = year_path / folder / img
                    tags = tag_dict.get(tool, ' #CreativeCoding')
                    try:
                        status = toot(comment + ' ' + toot_text + ' ' + tags, image_path, image_caption)
                        status = status[:10]
                    except Exception as e:
                        status = e
                    change_log.append(f'Mastodon: {status}')
                readme_as_lines.insert(insert_point - 3, entry_text)
                adding_message = 'Adding: ' + folder
                print(adding_message)
                change_log.append(adding_message)
                break
    # overwrite the readme markdown index
    with open(readme_path, 'wt') as readme:
        content = ''.join(readme_as_lines)
        readme.write(content)
    # TODO show all changes on GUI
    generate_sketch_a_day_index()
    adding_message = 'Regenerated logseq index.'
    print(adding_message)
    change_log.append(adding_message) 
    if gui_mode:
        clipped_log = (entry[32:] for entry in change_log)
        sg.popup('Changes:' if len(change_log) > 1 else 'No changes:', '\n'.join(clipped_log))
    
def ask_tool_comment(folder, img, default_tool):
    image_path = year_path / folder / img
    if img.suffix.lower().endswith('svg'):  #*!todo
        drawing = svg2rlg(image_path)
        cur_width, cur_height = drawing.width, drawing.height
        dpi = min(600 / cur_height * 72, 600 / cur_width * 72)
        io_bytes = BytesIO()
        renderPM.drawToFile(drawing, io_bytes, fmt="PNG", dpi=dpi)
        png_bytes = io_bytes.getvalue()
    else:
        png_bytes, metadata = image_as_png_bytes(image_path, (600, 600)) #, resize=new_size)
    link = f'{REPO_MAIN_URL}/{YEAR}/{folder}'
    window = sg.Window(f'{img}', [
        [sg.Image(key='-IMAGE-', data=png_bytes)],
        [sg.T('Tool   '), sg.Combo(list(tools), default_value=default_tool,
                                   size=(40,22), key='-TOOL-')],
        [sg.T('Caption'), sg.Multiline(key='-DESCRIPTION-', size=(40,4))],
        [sg.T('Coment'), sg.Multiline(key='-COMMENT-', size=(40,4))],
        [sg.T('For Mastodon'), sg.Multiline(key='-MASTODON-',default_text=TOOT_DEFAULT.format(link), size=(40,4))],
        [sg.B('OK'), sg.B('Cancel'), sg.Checkbox('Post to Mastodon',
                                                 key='--TOOT--')],
        [sg.T(f'Running on: {sys.executable}')] # for debug
        ],font='Fixedsys')
    #window['-IMAGE-'].update(data=png_bytes)
    event, values = window.read(close=True)    
    if event is None or event == 'Cancel':
        print('Cancelled.')
        if gui_mode: sg.popup('Cancelled:', last_done_message)
        exit()
    return (
        values['-TOOL-'],
        values['-COMMENT-'],
        values['--TOOT--'],
        values['-DESCRIPTION-'],
        values['-MASTODON-'],
        )

def build_entry(folder, image_filename, tool=None, comment=None, image_caption=None):
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

