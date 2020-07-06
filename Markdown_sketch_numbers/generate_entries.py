# reads folder
# finds missing folders from last_done
# gets images, checks image types
# build markdown for entries
## TO DO:
# [X] find last entry for me
# [ ] insert new entries in propper place
# [ ] insert docstrings as text on .md file

from os import listdir
from os.path import isfile, join

from helpers import get_image_files, build_entry

YEAR = "2020"
base_path = "/media/villares/VolumeD/GitHub/sketch-a-day"
year_path = join(base_path,YEAR)
folders = listdir(year_path)

with open(join(base_path, 'README.md')) as readme:
    imagens = (line[line.find(YEAR):line.find(']')]
               for line in readme.readlines()
               if '![' in line)
    last_done = next(imagens)[:10]
    
# find folders after the last_done
new_folders = []
for f in reversed(folders):
    if last_done in f:
        break
    else:
        new_folders.append(f)

for f in new_folders:
    imgs = get_image_files(year_path, f)
    if imgs:
        print(build_entry(imgs[0], YEAR))

    