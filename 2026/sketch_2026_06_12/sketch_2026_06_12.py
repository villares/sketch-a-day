# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org
import py5

import calendar
import locale

ye = 2026
mo = 6

class CalComNomeDosDiasGrande(calendar.TextCalendar):
  
  def formatweekheader(self, width):
      return '|'.join(
          f"{calendar.day_name[(self.firstweekday + i) % 7]:^{width}}"
          for i in range(7)
      )
  
  def formatday(self, day, weekday, width):
      if day == 0:
          return ' ' * width
      return str(day).center(width)
  
  def formatweek(self, theweek, width):
      return '˙'.join(self.formatday(d, wd, width) for (d, wd) in theweek)
  
  def formatmonth(self, theyear, themonth, w=10, l=1):
      w = max(2, w)
      l = max(1, l)
      s = self.formatmonthname(theyear, themonth, 7 * (w + 1) - 1)
      s = s.rstrip()
      s += '\n' * l
      s += self.formatweekheader(w).rstrip()
      s += '\n' * l
      for week in self.monthdays2calendar(theyear, themonth):
          s += self.formatweek(week, w).rstrip()
          s += '\n' * l
      return s

def setup():
    global cal
    py5.size(1200, 400)
    locale.setlocale(locale.LC_TIME, 'pt_PT.UTF-8')
    cal = CalComNomeDosDiasGrande()
    cal.firstweekday = calendar.SUNDAY
    py5.text_font(
        py5.create_font('Source Code Pro Bold', 24))
    
def draw():
    py5.background(100, 200, 100)
    py5.fill(0)
    x = 48
    y = 48
    for i, li in enumerate(cal.formatmonth(ye, mo).splitlines()): 
        py5.fill(255 if i == 1 else 0)
        py5.text(li, x, y)
        y += 48

def key_pressed():
    if py5.key == 's':
        py5.save_frame(f'{ye}-{mo}.png')

py5.run_sketch(block=False)