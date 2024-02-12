"""
Based on sketch 36 180205b - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day

Now for py5 imported mode - https://py5coding.org
"""

confeti = []
SIZE = 15
TEXTO = "carnahacking\nno garoa\nsegunda-feira 12/2\n15h — 20h"
MAXDIST = 150

def setup():    
    size(500, 500) 
    font = create_font("GaroaHackerClubeBold.otf", 24) # veja na pasta do sketch
    text_font(font)   # A fonte do Garoa tem uma licença livre
    text_align(CENTER, CENTER) # Alinhamento horizontal e vertical
    text_size(38)              # Tamanho do texto
    no_stroke()
    for _ in range(1200):
        confeti.append((
            [random(width),       # X
             random(height+20)],  # Y
            random(TWO_PI),  # screen plane rotation
            random(TWO_PI),  # fake "Z" rotation
            color(random(256), random(256), random(256))  # color
        ))

def draw():
    background(0)
    text(TEXTO, width/2, height/2);
    f = frame_count
    for pos, rot1, rot2, color_ in confeti:
        with push_matrix():
            x, y = pos            
            dis = dist(x, y, mouse_x, mouse_y)
            if dis < MAXDIST:
                ang = atan2(y - mouse_y, x - mouse_x)
                dd = remap(dis, 0, MAXDIST, 1, 0)
                dd = (dd ** 0.9) * dis * 2
                x += cos(ang) * dd
                y += sin(ang) * dd            

            translate(x, y)
            rotate(rot1 + float(f / 7))
            s = sin(rot2 + float(f / 11))

            fill(color_)
            ellipse(0, 0, SIZE, SIZE * s)

            pos[1] += 1 + random(0, 2) * s # update y (pos[1])
            if y > height + 20:
                pos[1] = -20
      
            
            
    
    
