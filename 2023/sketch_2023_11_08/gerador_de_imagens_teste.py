from pathlib import Path

def setup():
    size(600, 600)
    
def tri(x, y, w):
    hw = w / 2
    triangle(x - hw, y - hw, x + hw, y - hw, x - hw, y + hw)
    
def draw():
    for n, f in ((1, square), (2, tri), (3, circle)):
        gr = create_graphics(600, 600)
        begin_record(gr)
        gr.rect_mode(CENTER)
        fill(random(255), random(255), random(255))
        f(random(100, width-100), random(100, height-100), 200)
        end_record()
        gr.save(f'{n}/{frame_count}.png', drop_alpha=False)
        if frame_count >= 20:
            exit_sketch()
