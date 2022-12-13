# Using py5coding.org imported mode

"""
# After pip3 install Hershey-Fonts:
>>> from HersheyFonts import HersheyFonts
print(HersheyFonts().default_font_names)
['futural', 'astrology', 'cursive', 'cyrilc_1', 'cyrillic', 'futuram', 'gothgbt', 'gothgrt', 'gothiceng', 'gothicger',
'gothicita', 'gothitt', 'greek', 'greekc', 'greeks', 'japanese', 'markers', 'mathlow', 'mathupp', 'meteorology', 'music',
'rowmand', 'rowmans', 'rowmant', 'scriptc', 'scripts', 'symbolic', 'timesg', 'timesi', 'timesib', 'timesr', 'timesrb']
"""

from HersheyFonts import HersheyFonts

thefont = HersheyFonts()
print(
    thefont.load_default_font('timesr'),
   # thefont.load_default_font(thefont.default_font_names[0]),
   # thefont.load_default_font(),  # futural
)
def setup():
    size(500, 500)
    stroke_weight(1)
    thefont.normalize_rendering(50)
    translate(0, 250)
    line(0, 0, 500, 0)
    phrase = "\"Hello Hershey\"áñéï"
    for (x1, y1), (x2, y2) in thefont.lines_for_text(phrase):
        line(x1, -y1 ,x2 ,-y2)
    