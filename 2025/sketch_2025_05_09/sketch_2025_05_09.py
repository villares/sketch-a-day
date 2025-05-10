import py5

V = py5.Py5Vector
u = 75
right = V(u, 0)
up60d = V(u, 0).rotate(py5.radians(-60))
down30d = V(u, 0).rotate(py5.radians(+30))
down = V(0, u)

a = V(u * 2, u * 2)
b = a + up60d
c = a + right
d = c + up60d
e = d + down30d
f = c + down30d
g = c + down
h = g + down30d
i = a + down

def setup():
    py5.size(450, 450)
    py5.triangle(*a, *b, *c)
    py5.triangle(*b, *d, *c)
    py5.quad(*c, *d, *e, *f)
    py5.triangle(*c, *f, *g)
    py5.triangle(*f, *g, *h)
    py5.quad(*a, *c, *g, *i)
    
py5.run_sketch()    

# def draw():
#    
#     no_fill()
#     w = base * 3
#     h = base * 1.5
#     for i in range(3):
#         for j in range(5):
#             if j % 2 == 0:
#                 x = i * w
#             else:
#                 x = i * w + w / 2
#             y = j * h
#             grupo(x, y, base)    
    
# def grupo(x, y, base):
#     desc = base * 1.5
#     fill(150, 0, 0)
#     pentagono(x, y, base, rot=False)
#     fill(250, 50, 50)
#     pentagono(x, y, base, rot=False, flip=True)
#     fill(0, 0, 150)
#     pentagono(x + desc, y, base, rot=True)
#     fill(50, 50, 250)
#     pentagono(x - desc, y, base, rot=True, flip=True)
# 
# def pentagono(xb, yb, lado_base, rot=False, flip=False):
#     k = remap(mouse_x, 0, width, -4, 2)
#     vs = [
#         (-2 + k,  0),
#         (-3, -3),
#         ( 0, -4 - k),
#         ( 3, -3),
#         ( 2 - k,  0)
#     ]
#     u = lado_base / 4
#     with begin_closed_shape():
#         for i, j in vs:
#             if flip:
#                 j = -j
#             if rot:
#                i, j = j, -i
#             x = xb + i * u
#             y = yb + j * u
#             vertex(x, y)
    
def key_pressed():
    save_frame('###.png')
    