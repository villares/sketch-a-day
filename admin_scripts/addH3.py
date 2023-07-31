#!/usr/bin/env python
# Adds ### titles (markdown for <h3> on sketch-a-day pages

from os.path import join

base_path = '/home/villares/GitHub/sketch-a-day'
    
def main(file):
    readme_path = join(base_path, file)
    # open the readme markdown index
    with open(readme_path, 'rt') as readme:
        readme_as_lines = readme.readlines()

    # overwrite the readme markdown index
    with open(readme_path, 'wt') as readme:
        for line in readme_as_lines:
            if '![' in line:
                readme.write('### {}\n\n'.format(line[2:line.find(']')]))
            readme.write(line)

if __name__ == '__main__':
    pass # main('FILE.md') # beware running this again will duplicates ### titles!
    # I tested with README.md (2022) first!
    # for year in (2018, 2019, 2020, 2021):
    #    main(str(year) + '.md')