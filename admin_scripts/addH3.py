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
from os.path import join, exists
from itertools import takewhile

from helpers import get_image_names

# YEAR and base_path to sketch-a-day folder are set manually, hard-coded
YEAR = '2022'   
# base_path = "/Users/villares/sketch-a-day" # 01046-10 previously
base_path = '/home/villares/GitHub/sketch-a-day'
year_path = join(base_path, YEAR)
if not exists(year_path):
    sketch_folders = []  # for the benefit of next_day.py
    print(f"{__file__}: Couldn't find the sketch-a-day year folder!")
else:
    sketch_folders = listdir(year_path)
readme_path = join(base_path, 'README.md')

    
def main():
    # open the readme markdown index
    with open(readme_path, 'rt') as readme:
        readme_as_lines = readme.readlines()

    # overwrite the readme markdown index
    with open(readme_path + '.out', 'wt') as readme:
        for line in readme_as_lines:
            if '![' in line:
                readme.write('### {}\n\n'.format(line[2:line.find(']')]))
            readme.write(line)


if __name__ == '__main__':
    main()
