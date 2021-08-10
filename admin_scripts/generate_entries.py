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

from helpers import get_image_names

YEAR = '2021'
base_path = '/home/villares/GitHub/sketch-a-day'
# base_path = "/Users/villares/sketch-a-day" # 01046-10
year_path = join(base_path, YEAR)
folders = listdir(year_path)
readme_path = join(base_path, 'README.md')


def main():
    # open the readme markdown index
    with open(readme_path, 'rt') as readme:
        lines = readme.readlines()
    # find date of the first image
    imagens = (
        line[line.find(YEAR) : line.find(']')]
        for line in lines
        if '![' in line
    )
    last_done = next(imagens)[:10]
    print('Last entry: ' + last_done)
    # find folders after the last_done
    new_folders = []
    for f in reversed(sorted(folders)):
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
        imgs = get_image_names(year_path, folder)
        # insert entry if matching image found
        if imgs and imgs[0].split('.')[0] == folder:
            entry_text = build_entry(imgs[0], YEAR)
            lines.insert(insert_point - 3, entry_text)
            print('Adding: ' + folder)
    # overwrite the readme markdown index
    with open(readme_path, 'wt') as readme:
        content = ''.join(lines)
        readme.write(content)


def build_entry(image, year, kind='pyde'):
    """
    Return a string with markdown formated
    for the sketch-a-day index page entry
    of image (for a certain year).
    """
    name, ext = image.split('.')
    tools = {
        'pyde': '[[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]',
        'flat': '[[Python + flat](https://xxyxyz.org/flat)]',
        'pyp5js': '[[pyp5js](https://berinhard.github.io/pyp5js/)]',
        'py5': '[[py5](https://py5.ixora.io/)]',
        'shoebot': '[[shoebot](http://shoebot.net/)]',
        'pyxel': '[[pyxel](https://github.com/kitao/pyxel/blob/master/README.md)]',
    }
    tools_mentioned = matches = (t for t in tools.keys() if t in name)
    try:
        tool = next(tools_mentioned)
    except StopIteration:
        tool = 'pyde'
    return """
---

![{0}]({2}/{0}/{0}.{1})

[{0}](https://github.com/villares/sketch-a-day/tree/master/{2}/{0}) {3}
""".format(
        name, ext, year, tools[tool]
    )


if __name__ == '__main__':
    main()
