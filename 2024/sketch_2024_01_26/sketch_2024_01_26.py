"""
Inspired by Poor man's DLA by @deconbatch 
https://www.deconbatch.com/2019/10/the-poor-mans-dla-diffusion-limited.html
"""

S = 10
SQS = S * S

cluster = [Py5Vector(0, 0)]

def setup():
    global halo_canvas
    size(720, 720)
    halo_canvas = create_graphics(width, height)
    halo_canvas.begin_draw()
    halo_canvas.background(255)
    halo_canvas.fill(0)
    halo_canvas.no_stroke()
    start = cluster[0] 
    halo_canvas.circle(start.x + width / 2,
                       start.y + height / 2, S * 2)
    halo_canvas.end_draw()

def draw():
    image(halo_canvas, 0, 0)
    translate(width / 2, height / 2)
    no_stroke()
    fill(255, 0, 0)
    for x, y in cluster:
        circle(x, y, S)
    add_particle()
    if frame_count > 1000:
        no_loop()

def add_particle():
    new_particle = Py5Vector.random(2) * width # + cluster[0]
    move = -new_particle.norm
    while not collision(new_particle):
        new_particle += move
    cluster.append(new_particle)
    halo_canvas.begin_draw()
    halo_canvas.circle(new_particle.x + width/2,
                       new_particle.y + height/2, S * 2)
    halo_canvas.end_draw()    

def collision(p):
    if halo_canvas.get_pixels(int(p.x + width/2), int(p.y + height/2)) == color(0):
        return True
    return False
#     for x, y in cluster:
#         if (x - p.x) ** 2 + (y - p.y) ** 2 < SQS:
#             return True
#     return False    
    
    
        
        
        