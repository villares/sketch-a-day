# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org

import py5

import calendar
import locale

year = 2026
month = 6
cell_width = 80
cell_height = 80
margin = 20
header_height = 140

def setup():    
    py5.size(600, 600)
    locale.setlocale(locale.LC_TIME, 'pt_PT.UTF-8')
    py5.text_font(
        py5.create_font('Source Code Pro Bold', 24))

def draw():
    py5.background(255)
    
    weeks = calendar.monthcalendar(year, month)
    #weeks.firstweekday = calendar.SUNDAY
    num_weeks = len(weeks)
    cal_width = (7 * cell_width) + (2 * margin)
    cal_height = header_height + (num_weeks * cell_height) + (2 * margin)
    py5.window_resize(cal_width, cal_height)
    
    title = f'{calendar.month_name[month]} {year}'
    py5.fill(0)
    py5.text_size(36)
    py5.text_align(py5.CENTER)
    py5.text(title, cal_width / 2, header_height / 2)
    
    # Day headers (Mon-Sun)
    day_names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    for i, day_name in enumerate(day_names):
        x = margin + (i * cell_width)
        y = margin + header_height - 10 - cell_height
        
        if i >= 5:
            is_weekend = i >= 5  # Saturday = 5, Sunday = 6
            if is_weekend:
                py5.fill(200, 100, 100)
            else:
                py5.fill(100)
        py5.text_size(24)
        py5.text_align(py5.CENTER, py5.CENTER)
        py5.text(day_name, x + cell_width / 2, y + cell_height / 2)
    
    y_offset = margin + header_height    
    for week_num, week in enumerate(weeks):
        for day_num, day in enumerate(week):
            x = margin + (day_num * cell_width)
            y = y_offset + (week_num * cell_height)
            py5.no_fill()
            py5.stroke(0)
            py5.stroke_weight(1)
            py5.rect(x, y, cell_width, cell_height)
            if day != 0:
                is_weekend = day_num >= 5  # Saturday = 5, Sunday = 6
                if is_weekend:
                    py5.fill(200, 0, 0)
                else:
                    py5.fill(0) 
                py5.text_size(24)
                py5.text_align(py5.CENTER, py5.CENTER)
                py5.text(str(day), x + cell_width / 2, y + cell_height / 2)
    

def key_pressed():
    global month
    if py5.key == 's':
        py5.save_frame(f'{year}-{month}.png')
        return
    elif py5.key_code == py5.LEFT:
        month -= 1
    elif py5.key_code == py5.RIGHT:
        month += 1
        
    if month == 13:
        month = 1
    elif month == 0:
        month = 12
        

py5.run_sketch(block=False)