#!/home/villares/miniconda3/bin/python

import PySimpleGUI as sg    # precisa installar o PySimpleGUI (pode ser no pip install ou no Thonny "packages")
from pathlib import Path
from PIL import Image, GifImagePlugin

# Define the GUI layout
layout = [
    [sg.Text('Input folder:'), sg.InputText(), sg.FolderBrowse()],
    [sg.Text('Output file:'), sg.InputText(default_text='out.gif'), sg.FileSaveAs()],
    [sg.Text('Frame duration (ms):'), sg.InputText(default_text='200')],
    [sg.Button('Create GIF'), sg.Button('Cancel')]
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
    if event == 'Create GIF' and values:
        print(values)
        # Get the input and output values from the GUI
        input_dir = values[0] 
        output_file = values[1]
        duration = int(values[2]) if values[2] else 200

        # Load the PNG images from the input folder
        images = [Image.open(file_path) for file_path
                  in sorted(Path(input_dir).iterdir())
                  if file_path.suffix.lower() == '.png']

        # Create the GIF if there are any images
        if images:
            images[0].save(
                output_file,
                save_all=True, append_images=images[1:],
                optimize=True,
                duration=duration,
                disposal=2,
                loop=0
                )
            sg.popup('GIF created successfully!')
        else:
            sg.popup('No PNG images found!')

        # Close the window
        window.close()

# Clean up the GUI
window.close()
