from skimage.data import astronaut
from skimage.color import label2rgb
from skimage.segmentation import slic
import py5

astronaut_image = astronaut() 
astronaut_segments = slic(astronaut_image, 
                          n_segments=300, 
                          compactness=100)
colored_segments = label2rgb(astronaut_segments, astronaut_image, kind='avg')
# print(colored_segments)

def setup():
    global img, seg_img, edges_shader, canvas, strokes
    py5.size(512, 512, py5.P2D)
    py5.color_mode(py5.HSB) # Matiz, Sat, Bri
    py5.no_stroke()
    seg_img = py5.create_image_from_numpy(colored_segments, 'RGB')
    img = py5.create_image_from_numpy(astronaut_image, 'RGB')
    #original_image.apply_filter(py5.POSTERIZE, 2)
    edges_shader = py5.load_shader("edges.glsl")
    edges = py5.create_graphics(img.width, img.height, py5.P2D)
    edges.begin_draw()
    edges.shader(edges_shader)
    edges.image(img, 0, 0)
    edges.apply_filter(py5.INVERT)
    edges.end_draw()
    strokes = edges.copy()
    strokes.apply_filter(py5.ERODE)
    canvas = py5.create_graphics(img.width, img.height, py5.P2D)
    canvas.begin_draw()
    canvas.image(seg_img, 0, 0)
    canvas.blend_mode(py5.MULTIPLY)
    canvas.image(strokes, 0, 0)
    canvas.end_draw()
    
#     strokes = canvas.copy()
#     strokes.load_np_pixels()
#     strokes.np_pixels[:, :, :] = 255 - strokes.np_pixels
#     strokes.update_np_pixels()
    
def draw():
    #background(0)
    #py5.shader(edges_shader)
    py5.image(canvas, 0, 0)
    #py5.apply_filter(py5.INVERT)
    py5.no_loop()
    py5.save('out.png')
    
py5.run_sketch()  
#     num = 1 + int(mouse_y / 10)
#     R = width / num
#     largura = R * 1.5
#     altura = R * sqrt(3)
#     random_seed(int(R))
#     
#     for fila in range(num):
#         for coluna in range(num):  # 0, 1, ... 9
#             x = int(coluna * largura)
#             y = int(fila * altura + altura / 2
#                     + (altura / 2 if coluna % 2 else 0))
#             D = R + R / 2 * sin(radians(x + frame_count * 10))
#             fill(img.get_pixels(x, y), 200)
#             d = random(D)
#             poligono(x, y, d)
# 
# def poligono(xc, yc, ra, pontos=6):
#     ang = TWO_PI / pontos
#     begin_shape()
#     for i in range(pontos):
#         x = xc + cos(ang * i) * ra
#         y = yc + sin(ang * i) * ra
#         vertex(x, y)
#     end_shape(CLOSE)

    
    
    
    

