#! /usr/bin/python3

# Generate rss.xml for sketch-a-day - WIP

from pathlib import Path

base_path = Path('/home/villares/GitHub/sketch-a-day')
  
rss_header = """<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0">
<channel>
<title>Alexandre Villares - sketch-a-day</title>
<link>http://abav.lugaralgum.com/sketch-a-day</link>
<description>One visual idea a day, made with code</description>"""

rss_footer = """</channel>\n</rss>"""

rss_item_format = """<item>
<title>{0}</title>
<link>{1}</link>
<guid>{1} </guid>
<pubDate>{2}</pubDate>
<description>{3}</description>
</item>
""".format  # use rss_item_format(title, link, date, description)
  
def main(file_name):
    readme_path = base_path / file_name
    # open the readme markdown index
    with open(readme_path, 'rt') as readme:
        readme_as_lines = readme.readlines()

    # open output file
    output_path = base_path / 'rss.xml'
    with open(output_path, 'wt') as output:
        output.write(rss_header)
        for line in readme_as_lines:
            if '![' in line:
                title = date = line[2:line.find(']')]
                link = 'http://'
                description = line
                item = rss_item_format(title, link, date, description)
                output.write(item)
        output.write(rss_footer)
        
if __name__ == '__main__':
    main('README.md')
    # for year in (2018, 2019, 2020, 2021):
    #    main(str(year) + '.md')
    

# example 
"""
<item>
<title>$title/title>
<link>$link</link>
<guid>example.com/3</guid>
<pubDate>Wed, 27 Nov 2013 13:20:00 GMT</pubDate>
<description>My newest article.</description>
</item>

<item>
<title>Article 2</title>
<link>example.com/2</link>
<guid>example.com/2</guid>
<pubDate>Tue, 26 Nov 2013 12:15:12 GMT</pubDate>
<description>My second article.</description>
</item>

<item>
<title>Article 1</title>
<link>example.com/1</link>
<guid> example.com/1</guid>
<pubDate>Mon, 25 Nov 2013 15:10:45 GMT</pubDate>
<description>My first article.</description>
</item>

</channel>
</rss>
"""
