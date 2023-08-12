#!/home/villares/miniconda3/bin/python

"""
Based on: PytSimpleGUI demo for displaying any format of image file. 
2022 - Alexandre B A Villares - I just added some PNG metadata viewing 
                                for use with villares.helpers.save_png_with_src()
                                github.com/villares/villares/

https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Image_Elem_Image_Viewer_PIL_Based.py
Copyright 2020 PySimpleGUI.org
LGPLv3 https://github.com/PySimpleGUI/PySimpleGUI/blob/master/license.txt    
"""

import PySimpleGUI as sg
# import PySimpleGUIQt as sg
import os

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
            PIL.Image.ANTIALIAS,
        )
    with io.BytesIO() as bio:
        img.save(bio, format='PNG')
        return bio.getvalue(), img.info

cwd = os.getcwd()

# --------------------------------- Define Layout ---------------------------------
# First the window layout...
left_col = [
    [sg.Text('Folder'),
     sg.In(size=(25, 1), default_text=cwd, enable_events=True, key='-FOLDER-'),
     sg.FolderBrowse(),],
    # PSG will put FolderBrowser() result into "In" field!
    [sg.Listbox(values=[], enable_events=True, size=(40, 20), key='-FILE LIST-')],
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

if __name__ == '__main__':
    sg.ChangeLookAndFeel('BlueMono')
    window = sg.Window('Multiple Format Image Viewer',
                       layout, resizable=True, font='Consolas 10')
    while True:  # run the event loop
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == '-FOLDER-':
            # Folder name was filled in, make a list of files in the folder
            folder = values['-FOLDER-']
            try:
                file_list = os.listdir(folder)  # get list of files in folder
            except:
                file_list = []
            fnames = [f for f in file_list
                      if os.path.isfile(os.path.join(folder, f))
                      and f.lower().endswith(('.png', '.jpg', 'jpeg',
                                              '.tiff', '.bmp', '.gif'))]
            window['-FILE LIST-'].update(fnames)
        elif event == '-FILE LIST-' and values['-FILE LIST-']:  # A file was chosen
            try:
                filename = os.path.join(values['-FOLDER-'],
                                        values['-FILE LIST-'][0])
                window['-TOUT-'].update(filename)
                if values['-W-'] and values['-H-']:
                    new_size = int(values['-W-']), int(values['-H-'])
                else:
                    new_size = None
                png_bytes, metadata = image_as_png_bytes(filename, resize=new_size)
                window['-IMAGE-'].update(data=png_bytes)
                window['-CODE-'].update(metadata.pop('code', ''))
                window['-OTHER-'].update('\n'.join(f'{k}: {v}'
                                                   for k, v in metadata.items()))
            except Exception as e:
                print(f'** Error {e} **')  # failed loading the file or updating the image

    window.close()   # Close & Exit

