import PySimpleGUI as sg

bg = True
values = {'-Text-': '', '-Hue-': 0}

def setup():
    global window
    size(600, 600)
    color_mode(HSB)
    text_size(30)
    layout = [
        [sg.Text('PySimpleGUI FTW!')],
        [sg.Input(key='-Text-', enable_events=True)],
        [sg.Slider(key='-Hue-', range=(0, 255), orientation='h', enable_events=True)],
        [sg.Button('Background')]]
    window = sg.Window('Sketch controls!', layout)
    launch_repeating_thread(controls, name='controls')  

def controls(first=False):
    global bg, event, values
    if first:
       event, values = window.read(timeout=0)
       return
    else:
        event, values = window.read()
    print(millis())
    if event == sg.WIN_CLOSED:
        exit_sketch()
    elif event == 'Background':
        bg = not bg
        # background(200) # doesn't work here
        
def draw():
    if bg:
        background(50, 100, 100)
    fill(255)
    text(values['-Text-'], 50, 500)
    fill(values['-Hue-'], 200, 200)
    circle(100, 100, 50 + 50 * sin(frame_count / 10))

def exiting():
    stop_thread('controls')
    window.close()
