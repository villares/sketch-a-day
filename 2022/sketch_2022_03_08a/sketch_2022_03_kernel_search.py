from itertools import product
import py5
import pickle

K = list(product(range(-1, 1), repeat=2))

def setup():
    py5.size(600, 600)
    img = py5.load_image('image.png')
    #py5.image(img, 0, 0)
    ks = set()
    offx, offy = 1, 1
    for x in range(offx, offx + 99):
        for y in range(offy, offy + 99):
            k = tuple(img.get(x + xo, y + yo) for xo, yo in K)
            ks.add(k)        
    print(len(ks))
    
    with open('out2x2.k', 'wb') as out:
        pickle.dump(ks, out)
    
    with open('out2x2.k', 'rb') as inp:
        ks = pickle.load(inp)
        
    py5.translate(50, 50)
    py5.scale(10)
    x = y = 0
    for k in sorted(ks):
        for c, (xo, yo) in zip(k, K):
            py5.stroke(c)
            py5.point(x + xo, y + yo)
        x += 3
        if x > py5.width // 10 - 10:
            x = 0
            y += 3
    py5.save_frame('kernels2x2.png')
        
py5.run_sketch()
    