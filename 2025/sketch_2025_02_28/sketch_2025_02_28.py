"""
Based on sketch 37 180206b
https://abav.lugaralgum.com/sketch-a-day
"""

confetti = []
SIZE = 15
TEXTO = """carnahacking\nvem aí""" # ainda não usei este texto...


def setup():
    size(500, 500)   # comment out se for usar com fundo
    no_stroke()
    font = create_font("GaroaHackerClubeBold.otf", 24); 
    text_font(font)
    text_align(CENTER, CENTER) # Alinhamento horizontal e vertical
    text_size(60)             # Tamanho do texto
    for _ in range(1500):
        confetti.append(([random(width),  # X
                         random(height+20)],  # Y
                        random(TWO_PI),  # screen plane rotation
                        random(TWO_PI),  # "Z" rotation
                        color(random(256), random(256), random(256))  # color
                        ))

def draw():
    #background(fundo)
    background(0) # comment out se for usar o fundo
    fill(255)
    text(TEXTO, width/2, height/2);

    for pos, rot1, rot2, color_ in confetti:
        with push_matrix():
            x, y = pos
            max_dist = width / 2
            dis = dist(x, y, mouse_x, mouse_y)
            ang = atan2(y - mouse_y, x - mouse_x)
            if (dis < max_dist):
                dd = remap(dis, 0, max_dist, 1, 0)
                df = dd ** 0.95 * dis * 2
                x += cos(ang) * df
                y += sin(ang) * df
            translate(x, y)
            rotate(rot1 + float(frame_count / 7))
            s = sin(rot2 + float(frame_count / 11))
            fill(color_)    
            ellipse(0, 0, SIZE, SIZE * s)
            pos[1] += 1 + random(0, 2) * s # update y (pos[1])
            if y > height + 20:
                pos[1] = -20
            if dist(x, y, mouse_x, mouse_y) < 100:
                  pos[1] += random(-5, 0)
                  pos[0] += random(-5, 5)
                  
                
#     if frame_count < 300 and not frame_count % 3:
#         save_frame("###.tga")

    