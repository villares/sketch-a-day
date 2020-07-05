# read folder
# find missing entries
# check image types
# build markdown
# insert in propper place

from os import listdir
from os.path import isfile, join

from helpers import name_image_files, build_entry

last_done = '2020_06_21' 
YEAR = "2020"
base_path = "/media/villares/VolumeD/GitHub/sketch-a-day"
year_path = join(base_path,YEAR)
folders = listdir(year_path)

new_folders = []
for f in reversed(folders):
    if last_done in f:
        break
    else:
        new_folders.append(f)
        
for f in new_folders:
    img = name_image_files(year_path, f)
    if img:
        print(build_entry(img[0], YEAR))
    

sl = (
    ("sketch_2020_06_18a", ".gif"),
    ("sketch_2020_06_17a", ".png"),
    ("sketch_2020_06_16a", ".gif"),
    ("sketch_2020_06_15a", ".gif"),
 
)
# for s, OUTPUT in sl:
#     SKETCH_NAME = s
#     str(

