
def setup():
    global shp, osb
    size(500, 500, P3D)
    textures = []
    tex = create_graphics(200, 200)  # A Py5Graphics "canvas"
    for _ in range(6):
        tex.begin_draw()
        tex.stroke_weight(10)
        tex.fill(random(255), random(255), random(255))
        tex.rect(0, 0, 200, 200)
        tex.end_draw()
        textures.append(tex.copy()) # a Py5Image is appended
    print(len(textures))
    shp = textured_cube(200, textures)
    osb = create_graphics(500, 500, P3D)
    
    
def draw():
    background(255)
    with osb.begin_draw():
        osb.background(0, 0, 200)
        osb.no_fill()
        osb.stroke(0)
        osb.stroke_weight(2)
        #osb.rect(1, 1, width - 10, height -10)
        #osb.lights()
        osb.translate(width / 2, height / 2, -width / 2)
        osb.rotate_y(radians(frame_count))
        osb.rotate_x(radians(frame_count * 2))
        osb.shape(shp, 0, 0)
    pxs = osb.get_np_pixels()
    for x in range(0, width, 10):
        for y in range(0, height, 10):
            p = pxs[x, y]
            fill(*p[1:])
            no_stroke()
            square(x, y, 9)
    #image(osb, 0, 0)

def key_pressed():
    global shp, b
    textures = [convert_image(to_pil().resize((200, 200)))] * 6
    shp = textured_cube(200, textures)




def textured_cube(extent, textures):
    A = ((-1, -1, 1, 0, 0),  # +Z "front" face.
         (1, -1, 1, 1, 0), 
         (1, 1, 1, 1, 1),
         (-1, 1, 1, 0, 1))
    B = ((-1, -1, -1, 0, 0), # -Z "back" face. 
         (1, -1, -1, 1, 0),
         (1, -1, 1, 1, 1),
         (-1, -1, 1, 0, 1))
    C = ((1, -1, -1, 0, 0),  # +Y "bottom" face.
         (-1, -1, -1, 1, 0),
         (-1, 1, -1, 1, 1),
         (1, 1, -1, 0, 1))
    D = ((-1, 1, 1, 0, 0),   # -Y "top" face.
         (1, 1, 1, 1, 0),
         (1, 1, -1, 1, 1),
         (-1, 1, -1, 0, 1))
    E = ((1, -1, 1, 0, 0),   # +X "right" face.
         (1, -1, -1, 1, 0),
         (1, 1, -1, 1, 1),
         (1, 1, 1, 0, 1))
    F = ((-1, -1, -1, 0, 0), # -X "left" face.
         (-1, -1, 1, 1, 0),
         (-1, 1, 1, 1, 1),
         (-1, 1, -1, 0, 1))
    tc = create_shape(GROUP)
    tc.scale(extent)    
    for face, tex in zip((A, B, C, D, E, F), textures):
        tf = create_shape()
        with tf.begin_shape(QUADS):
            # textureMode() can only be called between beginShape()
            # and endShape()
            tf.texture_mode(NORMAL)
            tf.no_stroke()
            tf.texture(tex)
            tf.vertices(face)
        tc.add_child(tf)
    return tc


