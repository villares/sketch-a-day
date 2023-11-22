def setup():
    global shp
    size(500, 500, P3D)
    textures = []
    tex = create_graphics(200, 200)  # A Py5Graphics "canvas"
    for _ in range(6):
        tex.begin_draw()
        tex.background(random(255), random(255), random(255))
        tex.no_stroke()
        for _ in range(100):
            tex.circle(random(200), random(200), 10)
        tex.end_draw()
        textures.append(tex.copy()) # a Py5Image is appended
    print(len(textures))
    shp = textured_cube(200, textures)

    
def draw():
    background(200)
    translate(width / 2, height / 2, -width / 2)
    rotate_y(radians(frame_count))
    rotate_x(radians(frame_count * 2))
    shape(shp, 0, 0)
    
#     if frame_count % 2 and frame_count <= 360:
#         save_frame('###.png')
    

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

