# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org

import py5
import calendar
import locale

year = 2026
month = 6
cell_width = 100
cell_height = 80
margin = 20
header_height = 140
first_weekday = calendar.SUNDAY  # calendar.MONDAY

def setup():    
    py5.size(600, 600)
    locale.setlocale(locale.LC_TIME, 'pt_PT.UTF-8') # nomes em Português
    py5.text_font(
        py5.create_font('Source Code Pro Bold', 24))

def draw():
    py5.background(200, 255, 200)
    calendar.setfirstweekday(first_weekday)
    weeks = calendar.monthcalendar(year, month)
    num_weeks = len(weeks)
    cal_width = 7 * cell_width + 2 * margin
    cal_height = header_height + num_weeks * cell_height + 2 * margin
    py5.window_resize(cal_width, cal_height)
    
    title = f'{calendar.month_name[month]} {year}'
    py5.fill(0)
    py5.text_size(36)
    py5.text_align(py5.CENTER)
    py5.text(title, cal_width / 2, header_height / 2)
    
    day_names = [calendar.day_name[(first_weekday + i) % 7] for i in range(7)]
    
    for i, day_name in enumerate(day_names):
        x = margin + i * cell_width
        y = margin + header_height - 10 - cell_height
        if is_weekend_day(i):
            py5.fill(200, 100, 100)
        else:
            py5.fill(100)
        py5.text_size(18)
        py5.text_align(py5.CENTER, py5.CENTER)
        py5.text(day_name, x + cell_width / 2, y + cell_height / 2)
    
    y_offset = header_height    
    for week_i, week in enumerate(weeks):
        for day_i, day in enumerate(week):
            x = margin + day_i * cell_width
            y = y_offset + week_i * cell_height
            py5.no_fill()
            py5.stroke(0)
            py5.stroke_weight(1)
            py5.rect(x, y, cell_width, cell_height)
            
            if day != 0:
                if is_weekend_day(day_i):
                    py5.fill(200, 0, 0)
                else:
                    py5.fill(0) 
                    
                py5.text_size(24)
                py5.text_align(py5.CENTER, py5.CENTER)
                py5.text(str(day), x + cell_width / 2, y + cell_height / 2)


def is_weekend_day(day_index):
    return (first_weekday + day_index) % 7 >= 5  # Saturday=5, Sunday=6


def key_pressed():
    global month, first_weekday
    if py5.key == 's':
        py5.save_frame(f'{year}-{month}.png')
        return
    elif py5.key == 'w':
        first_weekday = calendar.SUNDAY if first_weekday == calendar.MONDAY else calendar.MONDAY
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
