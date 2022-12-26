#! /usr/bin/python3

# Generate rss.xml for sketch-a-day - WIP

import re
from datetime import datetime
from pathlib import Path

import markdown as md

BASE_PATH = Path('/home/villares/GitHub/sketch-a-day')
BASE_URL = 'http://abav.lugaralgum.com/sketch-a-day' 
 
rss_header = f"""<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0">
<channel>
<title>Alexandre Villares - sketch-a-day</title>
<link>{BASE_URL}</link>
<description>One visual idea a day, made with code</description>
"""

rss_footer = """</channel>\n</rss>"""

rss_item_format = """<item>
<title>{0}</title>
<link>{1}</link>
<guid>{1}</guid>
<pubDate>{2}</pubDate>
<description>{3}</description>
<content>{4}</content>
</item>
""".format  # use rss_item_format(title, link, date, description, full_content)
  
def extract_date(line):
    date_match = re.search(r"(\d{4}_\d{2}_\d{2})", line)
    if date_match:
        date = datetime.strptime(date_match.group(1), "%Y_%m_%d")
        return date.replace(hour=12).strftime("%a, %d %b %Y %H:%M:%S %z")
    else:
        return ''

def sanitize_anchor(text):
    text = text.replace(' ', '-')       # Replace spaces with dashes
    text = re.sub(r'[^\w-]', '', text)  # Remove all special characters
    return text

def escape_xml(text):
    return (text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace("'", "&apos;")
                .replace('"', "&quot;")
            )

# def extract_url(line):
#     url_match = re.search(r"\((https://.*)\)", line)
#     return url_match.group(1) if url_match else ''

def main(file_name):
    readme_path = BASE_PATH / file_name
    
    with open(readme_path, 'rt') as readme:
        readme_as_lines = readme.readlines()
    
    output_path = BASE_PATH / 'rss.xml'
    with open(output_path, 'wt') as output:
        output.write(rss_header)
        content_lines = None  # no lines get added before the first H3
        for i, line in enumerate(readme_as_lines):
            end_of_file = i == len(readme_as_lines) - 1
            if line.startswith('### ') or end_of_file:
                if content_lines:
                    contents = md.markdown(''.join(content_lines)
                                           + (line if end_of_file else ''))
                    item = rss_item_format(title, link, date, description, contents)
                    output.write(item)
                # prepare next item 
                name = line[4:].strip()
                title = escape_xml(name)
                date = extract_date(line)
                link = f'{BASE_URL}#{sanitize_anchor(name)}'
                description = md.markdown(''.join(readme_as_lines[i+2:i+5])
                                            .replace('\n\n', '')
                                            .replace(f'![{title}]', '[image]')
                                            .replace(f'[{title}]', '[source]'))
                content_lines = [] # empty list for next item's content
            elif line.strip() and content_lines is not None:
                content_lines.append(line)
        output.write(rss_footer)
        
if __name__ == '__main__':
    main('README.md')
    # for year in (2018, 2019, 2020, 2021):
    #    main(str(year) + '.md')
    
