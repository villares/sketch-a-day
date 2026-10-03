from itertools import combinations, product

import numpy as np
import py5

W = 70
N = 30
P = 10000
RP = 150 
population = []

def setup():
    global seq, nodes
    py5.size(800, 810)
    py5.text_font(py5.create_font('Inconsolata ExtraBold', 14))
    py5.text_size(10)
    py5.stroke_join(py5.ROUND)
    seq = range(N) 
    #nodes = np.random.randint(0, 100, size=(N, 2))
    grid = list(product(range(5, W-4, 10), repeat=2))
    sample = py5.random_sample(range(len(grid)), N, replace=False)
    nodes = np.array(grid)[sample]
    gerar_population()
    
def gerar_population():
    population.clear()
    for i in range(P):
       p = py5.random_permutation(seq)
       d = distancia(p)
       population.append((p, d))
       
    population.sort(
        key=(lambda t: t[1]),
        #reverse=True
        )
    print(len(population))

def draw():
    py5.background(180)
    i = 0 
    grid_pos = list(product(range(5, py5.width, W + 10), repeat=2))
    for (x, y), (p, d) in zip(grid_pos, population):
        py5.stroke_weight(1)
        py5.stroke(0)
        py5.square(x, y, W)
        py5.fill(0)
        py5.text(d, x, y + W + 8)
        py5.no_fill()
        py5.stroke(0, 0, 200)
        with py5.push_matrix():
            py5.translate(x, y)
            with py5.begin_closed_shape():
                py5.vertices(nodes[p])
        py5.stroke_weight(3)
        py5.stroke(0)
        py5.points((x + vx, y + vy) for (vx, vy) in nodes[p])
 
def distancia(p):
    xys = nodes[p]
    xys_rolados = np.roll(xys, 1, axis=0)
    diferencas = xys - xys_rolados
    return np.sum(np.linalg.norm(diferencas, axis=1))
   
def cross_over(pa, pb):
    ia, ib = sorted(py5.random_sample(seq, 2, replace=False)) 
    prole = np.full(N, -1)
    prole[ia:ib] = pa[ia:ib]
    faltantes = prole == -1
    prole[faltantes] = [i for i in pb if i not in prole]
    return prole

def mutate(percentage=0.02):
    for i, (path, _) in enumerate(population):
        if py5.random(1) < percentage:
            ia, ib = sorted(py5.random_sample(seq, 2, replace=False)) 
            path[ia], path[ib] =  path[ib], path[ia]
            population[i] = (path, distancia(path))
    population.sort(
        key=(lambda t: t[1]),
    )

def evolve_pop():
    itens = range(RP)
    combos = list(combinations(itens, 2))
    nova = []
    amostra = py5.random_sample(combos, P, replace=False)
    for ipa, ipb in amostra:
        pa, da = population[ipa]
        pb, db = population[ipb]
        prole = cross_over(pa, pb)
        nova.append((prole, distancia(prole)))
    print(len(nova))
    return nova

def key_pressed():
    if py5.key == 'p':
        gerar_population()
    elif py5.key == 'm':
        mutate(0.05)
    elif py5.key == 'e':
        population[:] = evolve_pop()
        population.sort(
            key=(lambda t: t[1]),
        )
    elif py5.key == 's':
        py5.save_frame('####.png')

py5.run_sketch(block=False) 

