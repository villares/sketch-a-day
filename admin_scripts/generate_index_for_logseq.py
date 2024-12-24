#!/home/villares/thonny-env/bin/python

# Prepares page for logseq

import re
from pathlib import Path

input_path = '/home/villares/GitHub/sketch-a-day/docs/{}.md'
output_path = '/home/villares/GitHub/logseq/pages/sketch-a-day-{}.md'


def sketch_date(line):
    # Define the regex patterns 
    p6 = r'sketch_\d{6}' # sketch_NNNNNN
    p8 = r'sketch_\d{4}_\d{2}_\d{2}' # sketch_NNNN_NN_NN
    # If a match is found, return the matched string
    if match := re.search(p6, line):
        d = match.group(0)[7:]
        return '20' + d[0:2], d[2:4], d[4:6]
    elif match := re.search(p8, line):
        d = match.group(0)[7:7+10]
        return d.split('_')   
    else:
        return None

def generate_sketch_a_day_index(min_year=2018, max_year=2024):
    for s_year in range(min_year, max_year + 1):
        s_year = str(s_year)
        # open the source markdown page from the sketch-a-day repo
        with open(input_path.format(s_year), 'rt') as readme:
            readme_as_lines = readme.readlines()
        # generate the target markdown page for logseq
        with open(output_path.format(s_year), 'wt') as readme:
            writing = False
            for line in readme_as_lines:
                if r'.md) \| [<b>2' in line : ### {}\n\n'.format(line[2:line.find(']')])
                    index_links = [] 
                    for y in range(min_year, max_year + 1):
                        if str(y) == s_year:
                            index_links.append(f"**{s_year}**")
                        else:
                            index_links.append(f"[{y}](sketch-a-day-{y})")
                    readme.write(r' \| '.join(index_links))
                    writing = True
                elif writing:
                    if line.startswith('###') and (date_tuple := sketch_date(line)):
                        line = line[:-1] + ' [[{}-{}-{}]]\n'.format(*date_tuple)
                    elif '![' in line:
                        line = '' + line.replace(
                            'https://raw.githubusercontent.com/villares/sketch-a-day/main/',
                            '/home/villares/GitHub/sketch-a-day/')
                    elif 'https://github.com/villares/sketch-a-day/tree/' in line:
                        line = '' + (line.replace('https://github.com/villares/',
                                            'file:///home/villares/GitHub/')
                                            .replace('tree/main/', '')
                                            .replace('tree/master/', ''))
                    readme.write(line)

if __name__ == '__main__':
    generate_sketch_a_day_index()