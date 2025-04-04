
from py5_tools import animated_gif

n = 10

def setup():
    size(500, 500)
    no_stroke()
    frame_rate(16)
    # nome, numero de frames, tempo entre amostras, duração do frame na animação
    animated_gif('teste.gif', count=n, period=0.05, duration=1)
    
    
def draw():
    background(100)
    fill(255)
    text_size(40)
    text(frame_count, 200, 200)
    
    
    if frame_count > n + 5:
        exit_sketch()