zen = u"""The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one—and preferably only one—obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea—let's do more of those!
"""
pos = 0

def setup():
    global zen_lines
    size(900, 600, P3D)
    textFont(createFont("Inconsolata Bold", 21))
    zen_lines = ["\n"] * 22 + zen.split('\n')
    
def draw():
    translate(0, 200, -60)
    rotateX(QUARTER_PI / 2,)
    translate(0, -250)
    background(0, 0, 100)
    x, y, lh = 75, 27, 27
    shown_lines = zen_lines[pos:(pos+22)]
    for a_line in shown_lines:
        text(a_line, x, y)
        y += lh
    
def mouseWheel(e):
    global pos
    pos += e.count
