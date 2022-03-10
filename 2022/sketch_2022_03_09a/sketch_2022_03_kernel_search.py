from itertools import product
import pickle

K = list(product(range(-1, 2), repeat=2))
input_file = 'b.png' #'image.png' 
output_file = 'b.k' # 'out3x3.k'

def setup():
    size(600, 600)
    img = load_image(input_file)
    #image(img, 0, 0)
    ks = set()
    for x in range(1, img.width - 1):
        for y in range(1, img.height - 1):
            k = tuple(img.get(x + xo, y + yo) for xo, yo in K)
            ks.add(k)        
    print(len(ks))
    
    with open(output_file, 'wb') as out:
        pickle.dump(ks, out)
    
    with open(output_file, 'rb') as inp:
        ks = pickle.load(inp)
        
    translate(50, 50)
    scale(5)
    x = y = 0
    for k in sorted(ks):
        for c, (xo, yo) in zip(k, K):
            stroke(c)
            point(x + xo, y + yo)
        x += 4
        if x > width // 5 - 20:
            x = 0
            y += 4
    save_frame('kernels3x3.png')
        
run_sketch()
    