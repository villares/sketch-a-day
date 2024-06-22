import re

ANSI = {  # ANSI code to style name
    '0': 'END',
    '1': 'BOLD',
    '2': 'FAINT',
    '3': 'ITALIC',
    '4' : 'UNDERLINE',
    '7' : 'REVERSE',
    '36' : 'DARKCYAN',
    '37' : 'LIGHTGRAY',
    '90' : 'DARKGRAY',
    '91' : 'RED', 
    '92': 'GREEN',
    '93': 'YELLOW',
    '94' : 'BLUE',
    '95' : 'PURPLE',
    '96' : 'CYAN',
    }
# Style name -> ANSI escape sequence 
STYLE = {v: f'\033[{k}m' for k, v in ANSI.items()}
    
def parse_ansi_strings(input_string):
    ansi_pattern = r'\033\[\d+m'  # ESC DIGITS m
    segments = []
    matches = re.split(f'({ansi_pattern})', input_string)
    style_code = ''
    for segment in matches:
        if segment and segment[0] == '\033':
            style_code = ANSI.get(segment[2:-1], '') 
        elif segment:
            segments.append((style_code, segment))
    split_segments = []
    for code_and_segment in segments:
        if '\n' in code_and_segment[1]:
             lis = code_and_segment[1].splitlines()
             style_code = code_and_segment[0]
             for i, li in enumerate(lis):
                 split_segments.append((style_code , li))
                 if i < len(lis) - 1:
                     split_segments.append(('NEWLINE' , ''))
                 style_code  = ''
                 if code_and_segment == ('', ''):
                    split_segments.append(('NEWLINE' , ''))
        else:
            split_segments.append(code_and_segment)
    return split_segments
    
if __name__ == '__main__':
    input_string = (
     "First part of the\n string. "
    f"{STYLE['PURPLE']}this part \nis purple. "
    f"{STYLE['UNDERLINE']}final \npart of string is not bold"
    f". {STYLE['END']} aaa" 
)
    result = parse_ansi_strings(input_string)
    print(input_string)
    print(result)

"""
Code   Effect     Note
0      Reset / Normal     all attributes off
1      Bold or increased intensity     
2      Faint (decreased intensity)     Not widely supported.
3      Italic     Not widely supported. Sometimes treated as inverse.
4      Underline     
5      Slow Blink      less than 150 per minute
6      Rapid Blink     MS-DOS ANSI.SYS; 150+ per minute; not widely supported
7      [[reverse video]]     swap foreground and background colors
8      Conceal         Not widely supported.
9      Crossed-out     Characters legible, but marked for deletion. Not widely supported.
10     Primary(default) font     
11–19  Alternate font     Select alternate font n-10
20     Fraktur            hardly ever supported
21     Bold off or Double Underline     Bold off not widely supported; double underline hardly ever supported.
22     Normal color or intensity        Neither bold nor faint
23     Not italic, not Fraktur     
24     Underline off       Not singly or doubly underlined
25     Blink off     
27     Inverse off     
28     Reveal                   conceal off
29     Not crossed out     
30–37  Set foreground color     See color table below
38     Set foreground color     Next arguments are 5;<n> or 2;<r>;<g>;<b>, see below
39     Default foreground color     implementation defined (according to standard)
40–47  Set background color     See color table below
48     Set background color     Next arguments are 5;<n> or 2;<r>;<g>;<b>, see below
49     Default background color     implementation defined (according to standard)
51     Framed     
52     Encircled     
53     Overlined     
54     Not framed or encircled     
55     Not overlined     
60     ideogram underline            hardly ever supported
61     ideogram double underline     hardly ever supported
62     ideogram overline             hardly ever supported
63     ideogram double overline      hardly ever supported
64     ideogram stress marking       hardly ever supported
65     ideogram attributes off       reset the effects of all of 60-64
90–97  Set bright foreground color      aixterm (not in standard)
100–107 Set bright background color     aixterm (not in standard)
"""