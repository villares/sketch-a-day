from itertools import product
import py5
import pickle

K = list(product(range(-1, 1), repeat=2))

def setup():
    py5.size(500, 500)
    img = py5.load_image('image.png')
    #py5.image(img, 0, 0)
    ks = set()
    offx, offy = 200, 200
    for x in range(offx + 1, offx + 101):
        for y in range(offy + 1, offy + 101):
            k = tuple(img.get(x + xo, y + yo) for xo, yo in K)
            ks.add(k)        
    print(len(ks))
    
    with open('out2x2.k', 'wb') as out:
        pickle.dump(ks, out)
    
    with open('out2x2.k', 'rb') as inp:
        ks = pickle.load(inp)
        
    py5.translate(5, 5)
    x = y = 0
    for k in sorted(ks):
        for c, (xo, yo) in zip(k, K):
            py5.stroke(c)
            py5.point(x + xo, y + yo)
        x += 5
        if x > py5.width:
            x = 0
            y += 5
    py5.save_frame('kernels2x2.png')
        
py5.run_sketch()
    