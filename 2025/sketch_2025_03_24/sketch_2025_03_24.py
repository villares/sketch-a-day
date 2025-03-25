from skimage.data import astronaut
from skimage.color import label2rgb
from skimage.segmentation import slic

astronaut_image = astronaut() 
astronaut_segments = slic(astronaut_image, 
                          n_segments=100, 
                          compactness=10)
colored_segments = label2rgb(astronaut_segments, astronaut_image, kind='avg')
# print(colored_segments)

def setup():
    global img
    size(512, 512)
    color_mode(HSB) # Matiz, Sat, Bri
    no_stroke()
    img = create_image_from_numpy(colored_segments, 'RGB')


def draw():
    background(0)
    num = 1 + int(mouse_y / 10)
    R = width / num
    largura = R * 1.5
    altura = R * sqrt(3)
    random_seed(int(R))
    
    for fila in range(num):
        for coluna in range(num):  # 0, 1, ... 9
            x = int(coluna * largura)
            y = int(fila * altura + altura / 2
                    + (altura / 2 if coluna % 2 else 0))
            D = R + R / 2 * sin(radians(x + frame_count * 10))
            fill(img.get_pixels(x, y), 200)
            d = random(D)
            poligono(x, y, d)

def poligono(xc, yc, ra, pontos=6):
    ang = TWO_PI / pontos
    begin_shape()
    for i in range(pontos):
        x = xc + cos(ang * i) * ra
        y = yc + sin(ang * i) * ra
        vertex(x, y)
    end_shape(CLOSE)

    
    
    
    

