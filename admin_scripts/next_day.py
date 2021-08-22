#! /usr/bin/python3
import os
import re
from shutil import copytree
from datetime import datetime, timedelta
import generate_entries
from helpers import is_img_ext

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
# Rebuild the full folder paths
base_path = generate_entries.year_path
src_folder = os.path.join(base_path, last_folder)
new_folder = os.path.join(base_path, new_folder_name)
# Create a new folder, copy of the most recent one, but with new name
copytree(src_folder, new_folder)
print(f'{new_folder_name} folder created')
# Go through the new folder, remove images, rename files to new date
for file_name in os.listdir(new_folder):
    if is_img_ext(file_name):
        os.remove(os.path.join(new_folder, file_name))
        print(f'{file_name} image removed')
    elif previous_date_string in file_name:
        file_path = os.path.join(new_folder, file_name)
        if os.path.isfile(file_path):
            new_name = file_path.replace(previous_date_string, new_date_string)
            os.rename(file_path, new_name)
            print(f'{file_name} file renamed')

