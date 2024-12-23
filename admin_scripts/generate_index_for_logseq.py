#!/home/villares/thonny-env/bin/python

# Prepares page for logseq

from pathlib import Path

input_path = '/home/villares/GitHub/sketch-a-day/docs/{}.md'
output_path = '/home/villares/GitHub/logseq/pages/sketch-a-day-{}.md'


def main(min_year=2018, max_year=2024):
    for s_year in range(min_year, max_year + 1):
        s_year = str(s_year)
        # open the source markdown page from the sketch-a-day repo
        with open(input_path.format(s_year), 'rt') as readme:
            readme_as_lines = readme.readlines()
        # generate the target markdown page for logseq
        with open(output_path.format(s_year), 'wt') as readme:
            for line in readme_as_lines:
                if '![' in line:
                    line = line.replace('https://raw.githubusercontent.com/villares/sketch-a-day/main/',
                                        '/home/villares/GitHub/sketch-a-day/')
                if r'\| 2' in line: ### {}\n\n'.format(line[2:line.find(']')])
                    index_links = [] 
                    for y in range(min_year, max_year + 1):
                        if str(y) == s_year:
                            index_links.append(f"**{s_year}**")
                        else:
                            index_links.append(f"[{y}](sketch-a-day-{y})")
                    readme.write(r' \| '.join(index_links))
                else:
                    readme.write(line)

if __name__ == '__main__':
    main()