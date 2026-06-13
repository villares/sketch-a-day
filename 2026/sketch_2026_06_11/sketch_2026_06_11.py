# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org
import py5

import calendar
import locale

ye = 2026
mo = 6

class SingleLetterCalendar(calendar.TextCalendar):
    
    def formatweekheader(self, width):
        weekdays = (calendar.day_name[(self.firstweekday + i) % 7][0].ljust(width)
                    for i in range(7))
        return ' '.join(weekdays).upper()

    def formatday(self, day, weekday, width):
        if day == 0:
            #return ' ' * width
            return '-'.ljust(width)
        else:
            return str(day).ljust(width) #.ljust(width, '-')

    def formatmonthname(self, theyear, themonth, width=0, withyear=False):
            s = calendar.month_name[themonth]
            if withyear:
                s = f"{s} {theyear}"
            if width:
                return s.center(width)
            return s

def setup():
    global cal
    py5.size(800, 800)
    locale.setlocale(locale.LC_TIME, 'pt_PT.UTF-8')
    cal = SingleLetterCalendar()
    cal.firstweekday = calendar.SUNDAY
    py5.text_font(
        py5.create_font('Source Code Pro Bold', 48))
    
def draw():
    py5.background(100, 200, 100)
    py5.fill(0)
    x = 120
    y = 300 + 48 * 2
    for li in cal.formatmonth(ye, mo).splitlines(): 
        py5.fill(255 - (y - 396) / 2 )
        py5.text(li, x, y)
        y += 48

def key_pressed():
    if py5.key == 's':
        py5.save_frame(f'{ye}-{mo}.png')

py5.run_sketch(block=False)