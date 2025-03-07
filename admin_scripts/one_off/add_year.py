from pathlib import Path

base_path = Path('/home/villares/GitHub/sketch-a-day/docs/')

# Basic form of the new index of year links
template = (  
r"[<b>2025</b>](README.md) "
r"\| [<b>2024</b>](2024.md) "
r"\| [<b>2023</b>](2023.md) "
r"\| [<b>2022</b>](2022.md) "
r"\| [<b>2021</b>](2021.md) "
r"\| [<b>2020</b>](2020.md) "
r"\| [<b>2019</b>](2019.md) "
r"\| [<b>2018</b>](2018.md) "
"\n"
)
# String used to find the year of the page being processed
year_format = "[<b>{0}</b>]({0}.md)".format
   
def main(n):
    page = base_path / f'{n}.md'
    if not page.is_file():
        print(f'{page} not there.')
        return
    # read page
    with open(page, 'rt') as readme:
        readme_as_lines = readme.readlines()
    # overwrite with modifications
    with open(page, 'wt') as readme:
        for line in readme_as_lines:
            if is_year_links_line(line):
                line = template.replace(year_format(n), str(n))
                line = line.replace(f'[<b>{n}</b>](README.md)', str(n))  # current year case
            readme.write(line)
    print(f'{page} processed.') 

def is_year_links_line(line: str) -> bool:
    """A dirty check to find the index-links line instances."""
    return (r'\| [<b>' in line and
            '2018' in line and
            '2019' in line)

if __name__ == '__main__':
    for y in range(2018, 2029):
        main(y)
