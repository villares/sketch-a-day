#!/home/villares/miniconda3/bin/python

import os
import re
import sys
import subprocess

from datetime import datetime, timedelta
from pathlib import Path
from shutil import copytree

import generate_entries
from image_helpers import is_img_ext

print(sys.executable) # for debug

# Get the current sketch-a-day folders using the generate_entries module
rev_sorted_folders = sorted(generate_entries.sketch_folders, reverse=True)
if not rev_sorted_folders:
    print('No folders found!')
    exit()
last_folder = rev_sorted_folders[0]  # the most recent sketch folder
# find ISO formated date in folder name (but with '_' instead of '-') 
match = re.search(r'\d{4}_\d{2}_\d{2}', last_folder)
previous_date_string = match.group()
# Convert it to a datetime object
date = datetime.fromisoformat(previous_date_string.replace('_', '-'))
next_day = date + timedelta(days=1)  # calculates the next day!
# Convert it back to string and place inside a new folder name
new_date_string = str(next_day)[:10].replace('-', '_')
new_folder_name = last_folder.replace(previous_date_string, new_date_string)
keep_images = erase_code = False
open_folder = True
open_file = False
use_cwd = False
for arg in sys.argv[1:]:
    if arg.startswith('cn'):
        name_len = 10 + len(arg) - 2
        new_folder_name = new_folder_name[: new_folder_name.find(new_date_string) + name_len]
    elif arg.startswith('add-'):
        new_folder_name += arg[4:]
    elif arg == 'ec':
        erase_code = True
    elif arg == 'ki':
        keep_images = True
    elif arg == 'no':
        open_folder = False
    elif arg == 'of':
        open_file = True
    elif arg == 'cwd':
        use_cwd = True        
    else:
        print("""usage:
        cn        : for "clean name", stop filename after date.
        cn[X...]  : add any characters after cn to preserve some sufix.
        add-XX    : to add sufix, type it after `add-`, i.e. `add-py5`.
        ec        : erase content from files
        ki        : keep images
        no        : do not open folder
        of        : open file
        cwd       : use files from current folder
        """)
        exit()
# Rebuild the full folder paths
base_path = Path(generate_entries.year_path)
src_folder = base_path / last_folder
new_folder = base_path / new_folder_name
if use_cwd:
    src_folder = Path.cwd()
# Create a new folder, copy of the most recent one, but with new name
copytree(src_folder, new_folder)
print(f'{new_folder_name} folder created')
# Go through the new folder, remove images, rename files to new date
file_to_open = ''
for file in new_folder.iterdir():
    if is_img_ext(file.name):
        if not keep_images:
            os.remove(file)
            print(f'{file.name} image removed')
    elif last_folder in file.name:
        if file.is_file():
            new_name = file.name.replace(last_folder, new_folder_name)
            new_path = new_folder / new_name         
            os.rename(file, new_path)
            print(f'{file.name} file renamed to {new_name}')
            file_to_open = new_path
            if erase_code:
                open(new_path, 'w').close()
                print(f'{new_name} content removed')

if open_file and file_to_open:
    subprocess.Popen(["xdg-open", file_to_open])
elif open_folder:
    subprocess.Popen(["xdg-open", new_folder])
