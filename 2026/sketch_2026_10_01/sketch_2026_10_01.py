from itertools import combinations

import numpy as np
import py5

N = 20
P = 1000
populacao = []

def setup():
    global seq, coordenadas
    py5.size(600, 600)
    py5.stroke_join(py5.ROUND)
    seq = range(N) 
    coordenadas = np.random.randint(0, 100, size=(N, 2))
    gerar_populacao()
    
def gerar_populacao():
    populacao.clear()
    for i in range(P):
       p = py5.random_permutation(seq)
       d = distancia(p)
       populacao.append((p, d))
       
    populacao.sort(
        key=(lambda t: t[1]),
        #reverse=True
        )
    print(len(populacao))

def draw():
    py5.background(250)
    i = 0 
    for x in range(0, 600, 100):
        for y in range(0, 600, 100):
            p, d = populacao[i]
            py5.push_matrix()
            py5.translate(x, y)
            py5.no_fill()
            py5.stroke_weight(3)
            py5.stroke(0, 0, 255, 100)
            py5.begin_shape()
            py5.vertices(coordenadas[p])
            py5.end_shape(py5.CLOSE)
            py5.fill(0, 0, 255)
            py5.text(d, 20, 110)
            # desenha nós
            py5.stroke_weight(5)
            py5.stroke(0)
            py5.points(coordenadas)        
            py5.pop_matrix()
            i += 1
    
def distancia(p):
    xys = coordenadas[p]
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

def nova_pop():
    itens = range(100)
    combos = list(combinations(itens, 2))
    nova = []
    amostra = py5.random_sample(combos, 1000, replace=False)
    for ipa, ipb in amostra:
        pa, da = populacao[ipa]
        pb, db = populacao[ipb]
        prole = cross_over(pa, pb)
        nova.append((prole, distancia(prole)))
    nova.sort(
        key=(lambda t: t[1]),
        )
    return nova

def key_pressed():
    if py5.key == 'p':
        gerar_populacao()
    elif py5.key == 'e':
        populacao[:] = nova_pop()

py5.run_sketch(block=False) 

