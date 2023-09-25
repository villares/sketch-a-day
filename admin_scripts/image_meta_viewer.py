#!/home/villares/miniconda3/bin/python

"""
Based on: PytSimpleGUI demo for displaying any format of image file. 
2022 - Alexandre B A Villares - I just added some PNG metadata viewing 
                                for use with villares.helpers.save_png_with_src()
                                github.com/villares/villares/
2023 - Alexandre B A Villares - Moved from os.path to pathlib.Path
                                and added folders to the list!

https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Image_Elem_Image_Viewer_PIL_Based.py
Copyright 2020 PySimpleGUI.org
LGPLv3 https://github.com/PySimpleGUI/PySimpleGUI/blob/master/license.txt    
"""

import PySimpleGUI as sg
# import PySimpleGUIQt as sg
from pathlib import Path

import PIL.Image
import io

def image_as_png_bytes(file_path, resize=None):
    """
    Open an image file and convert it into PNG formated bytes, resize optional.
    Return tuple (bytes, <dict from PIL.Image.info>)
    """
    img = PIL.Image.open(file_path)
    cur_width, cur_height = img.size
    if resize:
        new_width, new_height = resize
        scale = min(new_height / cur_height, new_width / cur_width)
        img = img.resize(
            (int(cur_width * scale), int(cur_height * scale)),
            #PIL.Image.ANTIALIAS, # broken
        )
    with io.BytesIO() as bio:
        img.save(bio, format='PNG')
        return bio.getvalue(), img.info

cwd = Path.cwd()

# --------------------------------- Define Layout ---------------------------------
# First the window layout...
left_col = [
    [sg.Text('Folder'),
     sg.In(size=(25, 1), default_text=cwd, enable_events=True, key='-FOLDER-'),
     sg.FolderBrowse(),],
    # PSG will put FolderBrowser() result into "In" field!
    [sg.Listbox(values=[], enable_events=True, size=(60, 20), key='-FILE LIST-')],
    [sg.Text('Resize to'),
     sg.In(key='-W-', size=(5, 1), default_text='500'),  # I added the 500 default
     sg.In(key='-H-', size=(5, 1), default_text='500'),],
    ]
images_col = [
    [sg.Text('Loaded from the list:')],
    [sg.Text(size=(40, 1), key='-TOUT-')],
    [sg.Image(key='-IMAGE-')],  # Produces a "no data" warning at first
    ]
third_col = [
    [sg.Multiline(key='-CODE-', size=(50, 20), disabled=True, font='Consolas 10')],
    [sg.Multiline(key='-OTHER-', size=(50, 20), disabled=True, font='Consolas 10')],
    ]
# ----- Full layout -----
layout = [
    [sg.Column(left_col, element_justification='c'),
     sg.VSeperator(),
     sg.Column(images_col, element_justification='c'),
     sg.VSeperator(),
     sg.Column(third_col, element_justification='c'),]
    ]
# --------------------------------- Create Window ---------------------------------

def update_list(folder):
    try:
        file_list = list(folder.iterdir())  # get list of files in folder
    except:
        file_list = []
    fnames = ['↰ ' + folder.parent.name] + [f.name if f.is_file() else '↳ ' + f.name
              for f in file_list if f.name[0] != '.' and
              f.is_dir() or f.name.lower().endswith((
                  '.png', '.jpg', 'jpeg', 'webp',
                  '.tif', 'tiff', '.bmp', '.gif',
                  ))
              ]
    window['-FILE LIST-'].update(fnames)

if __name__ == '__main__':
    sg.ChangeLookAndFeel('BlueMono')
    window = sg.Window('Multiple Format Image Viewer',
                       layout, resizable=True, font='Consolas 10')
    while True:  # run the event loop
        event, values = window.read()
        folder = Path(values['-FOLDER-'])
        #print(event, values)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == '-FOLDER-':
            # Folder name was filled in, make a list of files in the folder
            update_list(folder)
        elif event == '-FILE LIST-' and values['-FILE LIST-']:  # A file was chosen
            item = values['-FILE LIST-'][0]
            try:
                if item.startswith('↰ '):
                    filepath = folder.parent
                else:
                    filepath = folder / item.strip('↳ ')
                if filepath.is_file():
                    window['-TOUT-'].update(filepath)
                    if values['-W-'] and values['-H-']:
                        new_size = int(values['-W-']), int(values['-H-'])
                    else:
                        new_size = None
                    png_bytes, metadata = image_as_png_bytes(filepath, resize=new_size)
                    window['-IMAGE-'].update(data=png_bytes)
                    window['-CODE-'].update(metadata.pop('code', ''))
                    window['-OTHER-'].update('\n'.join(f'{k}: {v}'
                                                       for k, v in metadata.items()))
                elif filepath.is_dir():
                    print('dir')
                    window['-FOLDER-'].update(str(filepath))
                    update_list(filepath)
            except Exception as e:
                print(f'** Error {e} **')  # failed loading the file or updating the image

    window.close()   # Close & Exit

