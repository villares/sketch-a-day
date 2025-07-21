#!/home/villares/thonny-env/bin/python
"""
A small GUI tool to select a folder and convert all the PNG images inside it into a GIF animation.
It only works if all the images have the same dimensions.
To run this you'll need Python and a few libraries installed.

This script can be copied, modified and distributed without any restrictions.
I offer it with a "public domain dedication" / CC0.

Support my work! Alexandre B A Villares <abav.lugaralgum.com/sketch-a-day>
"""

from pathlib import Path
                                 # You'll need to install these
import FreeSimpleGUI as sg       # `pip install FreeSimpleGUI`
import imageio                   # `pip install imageio`
from pygifsicle import gifsicle  # `pip install pygifsicle`

default_output = 'output.gif'
default_input = Path.cwd()
L_FONT = ('Courier', 20)
I_FONT = ('Courier', 16)
# Define the GUI layout
layout = [
    [sg.Text('Input folder:', font=L_FONT)],
    [sg.Text('Select a folder with PNG images, all with the same dimensions.', font=I_FONT)],
    [sg.InputText(default_text=default_input, font=I_FONT), sg.FolderBrowse(font=I_FONT)],
    [sg.Text('Output file name:', font=L_FONT)],
    [sg.InputText(default_text=default_output, font=I_FONT)],
    [sg.Text('Frame duration (milliseconds):', font=I_FONT), sg.InputText(default_text='200', font=I_FONT, size=(6, 1))],
    [sg.Text('Number of loops (0=forever):', font=I_FONT), sg.InputText(default_text='0', font=I_FONT, size=(3, 1))],
    [sg.Checkbox('Optimize GIF, to N colors:', True, font=I_FONT), sg.InputText(default_text='32', font=I_FONT, size=(3, 1))],
    [sg.Button('Create GIF', font=L_FONT), sg.Button('Cancel', font=L_FONT)]
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
        # Get the input and output values from the GUI
        input_dir = Path(values[0])
        output_file = input_dir / values[1]
        duration = int(values[2]) if values[2] else 200
        loops = int(values[3]) if values[3] else 0
        optimize_checkbox = values[4]
        colors = int(values[5]) if values[5] else 256 
        # Create the GIF if there are any images
        try:
            # Load the PNG images from the input folder
            images = [imageio.v3.imread(file_path) for file_path
                  in sorted(input_dir.iterdir())
                  if file_path.suffix.lower() == '.png']
            print(f'{input_dir.name} has {len(images)} PNG image{"s" if len(images)!=1 else ""}.')
            if images:
                imageio.v3.imwrite(
                output_file,
                images,
                duration=duration,
                loop=loops,
                )
                sg.popup(f'Animation saved as:\n{output_file}')
                # If optimize is checked
                if optimize_checkbox:
                    optimized_file = input_dir / ('optimized_' + values[1])
                    gifsicle(
                        sources=output_file,
                        destination=optimized_file,
                        optimize=True, # Whether to add the optimize flag or not
                        colors=colors, # Number of colors to use
                        options=["--verbose"]
                    ) 
            else:
                sg.popup(f'No PNG images found at\n{input_dir}')
        except Exception as e:
            if str(e).startswith('all input arrays'):
                sg.popup('Select only images of same size.')
            else:    
                sg.popup(str(e))
# Clean up the GUI
window.close()
