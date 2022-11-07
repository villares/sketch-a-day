
import PySimpleGUI as sg

layout = [[sg.Graph(canvas_size=(400, 400),
                    graph_bottom_left=(0, 0),
                    graph_top_right=(400, 400),
                    background_color='red', key='graph')],
#           [sg.T('Change circle color to:'),
#            sg.Button('Red'),
#            sg.Button('Blue'),
#            sg.Button('Move')],
           [sg.Slider(range=(0.0,99.9), default_value=50.0, resolution=.5,enable_events=True,
                      size=(40,15), orientation='horizontal', key='slider')]
          ]

window = sg.Window('Graph test', layout)
window.Finalize()

graph = window['graph']
circle = graph.DrawCircle((75, 75), 25, fill_color='black', line_color='white')
point = graph.DrawPoint((75, 75), 10, color='green')
oval = graph.DrawOval((25, 300), (100, 280),
                      fill_color='purple', line_color='purple')
rectangle = graph.DrawRectangle((25, 300), (100, 280), line_color='purple')
line = graph.DrawLine((0, 0), (100, 100))

while True:
    event, values = window.read()
    print(event, values)
    if event is None:
        break
    p = values['slider']
    graph.RelocateFigure(point, p, p)
    graph.RelocateFigure(circle, 50, p)
    graph.RelocateFigure(oval, p, 50)
    graph.RelocateFigure(rectangle, p, p + 100)

