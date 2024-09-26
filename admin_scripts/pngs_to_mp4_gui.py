#!/home/villares/thonny-env/bin/python

from pathlib import Path

import FreeSimpleGUI as sg    # precisa instalar o PySimpleGUI (pode ser no pip install ou no Thonny "packages")
import imageio              # precisa instalar:
# precisa instalar pip install imageio[ffmpeg]


default_output = Path.home() / 'out.mp4'
L_FONT = ('Courier', 20)
I_FONT = ('Courier', 16)

# Define the GUI layout
layout = [
    [sg.Text('Input folder:', font=L_FONT)],
    [sg.InputText(font=I_FONT), sg.FolderBrowse(font=I_FONT)],
    [sg.Text('Output file:', font=L_FONT)],
    [sg.InputText(default_text=default_output, font=I_FONT), sg.FileSaveAs(font=I_FONT)],
    [sg.Text('Frame duration (milliseconds):', font=L_FONT), sg.InputText(default_text='200', font=I_FONT, size=(6, 1))],
    [sg.Button('Create MP4', font=L_FONT), sg.Button('Cancel', font=L_FONT)]
]

# Create the GUI window
window = sg.Window('Create GIF', layout)

# Run the GUI event loop
while True:
    # Get the next GUI event
    event, values = window.read()

    # Exit the event loop if the window was closed or the Cancel button was clicked
    if event in (None, 'Cancel'):
        break

    # Create the GIF if the Create GIF button was clicked
    if event == 'Create MP4' and values:
        # Get the input and output values from the GUI
        input_dir = values[0] 
        output_file = values[1]
        duration = int(values[2]) if values[2] else 200
        dir_path = Path(input_dir)
        # Create the GIF if there are any images
        try:
            fps = 1000 / duration
            # Load the PNG images from the input folder
            images = [imageio.v3.imread(file_path) for file_path
                  in sorted(dir_path.iterdir())
                  if file_path.suffix.lower() == '.png']
            if images:
                #imageio.imwrite(output_file, images, fps=fps)
                writer = imageio.v2.get_writer(output_file, fps=fps)
                for img in images:
                  writer.append_data(img)
                writer.close()
                sg.popup(f'MP4 saved as:\n{output_file}')
            else:
                sg.popup(f'No PNG images found at:\n{dir_path}')
        except Exception as e:
            if str(e).startswith('all input arrays'):
                sg.popup('Select only images of same size.')
            else:    
                sg.popup(str(e))
# Clean up the GUI
window.close()
