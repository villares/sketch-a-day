
import PySimpleGUI as sg

bg = True
values = {}

def setup():   # py5 calls this once as the sketch starts
    global window, event, values 
    size(600, 600)
    color_mode(HSB)
    text_size(30)
    layout = [
        [sg.Text('PySimpleGUI FTW!')],
        [sg.Input(key='-Text-', enable_events=True)],
        [sg.Slider(key='-Hue-', range=(0, 255), orientation='h', enable_events=True)],
        [sg.CB('Background', key='-BG-', default=True, enable_events=True)]
    ]
    window = sg.Window('Sketch controls!', layout)
    launch_repeating_thread(controls, name='controls')  

def controls():
    global event, values
    if frame_count == 0:
        event, values = window.read(timeout=0)
    else:
        event, values = window.read()
    if event == sg.WIN_CLOSED:
      exit_sketch()  # triggers py5 exiting cleanup
    
def draw():   # py5 calls this in a loop (it is the "main" py5 drawing/animation loop)
    if values:
        if values['-BG-']:
            background(50, 100, 100)
        fill(255)
        text(values['-Text-'], 50, 500)
        fill(values['-Hue-'], 200, 200)
        circle(100, 100, 50 + 50 * sin(frame_count / 10))

def exiting():   # called by py5 on exit
    stop_thread('controls')
    window.close()