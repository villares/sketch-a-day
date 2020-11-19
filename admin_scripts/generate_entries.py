#! /usr/bin/python3

# reads folder
# finds missing folders from last_done
# gets images, checks image types
# build markdown for entries
## TO DO:
# [X] find last entry for me
# [X] insert new entries in propper place
# [ ] insert docstrings as text on .md file

from os import listdir
from os.path import isfile, join

from helpers import get_image_names, build_entry

YEAR = "2020"
base_path = "/media/villares/VolumeD/GitHub/sketch-a-day"
# base_path = "/Users/villares/sketch-a-day" # 01046-10
year_path = join(base_path, YEAR)
folders = listdir(year_path)
readme_path = join(base_path, 'README.md')

if __name__ == "__main__":
    # open the readme markdown index
    with open(readme_path, 'rt') as readme:
        lines = readme.readlines()   
    # find date of the first image    
    imagens = (line[line.find(YEAR):line.find(']')]
                   for line in lines
                   if '![' in line)
    last_done = next(imagens)[:10]
    print("Last entry: " + last_done)
    # find folders after the last_done
    new_folders = []
    for f in reversed(folders):
        if last_done not in f:
            new_folders.append(f)        
        else:
            break
    # find insertion point
    for insert_point, line in enumerate(lines):
        if last_done in line:
            break
    # iterate on new folders
    for folder in reversed(new_folders):
        if folder.endswith('flat'):
            kind = 'flat'
        else:
            kind = 'pyde'
        imgs = get_image_names(year_path, folder)
        if imgs:  # insert entry if matching image found
            lines.insert(insert_point - 3,
                         build_entry(imgs[0], YEAR, kind))
            print('Adding: '+ folder)
    # overwrite the readme markdown index
    with open(readme_path, 'wt') as readme:
        content = "".join(lines)
        readme.write(content)    
