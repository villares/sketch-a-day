import PySimpleGUI as sg      

bg = True

def setup():
    global window
    size(600, 600)
    color_mode(HSB)
    text_size(30)
    layout = [[sg.Text('PySimpleGUI FTW!')],      
          [sg.Input(key='-Text-')],
          [sg.Slider(key='-Hue-', range=(0, 255), orientation='h')], 
          [sg.Button('Background')]]      
    window = sg.Window('Sketch controls!', layout)      

def draw():
    global bg
    event, values = window.read(timeout=20)
    if event == sg.WIN_CLOSED:        
        exit_sketch()
        return
    elif event == 'Background':
        bg = not bg
        background(200)
    
    if bg:
        background(50, 100, 100)
    fill(255)
    text(values['-Text-'], 50, 500)
    fill(values['-Hue-'], 200, 200)
    circle(100, 100, 50 + 50 * sin(frame_count / 10)) 
          
def exiting():
    window.close()
