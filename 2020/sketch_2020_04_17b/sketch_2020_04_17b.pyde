from caneta_automatica import *

size(400, 400)
inicie_caneta()
strokeWeight(3)

fib = [1, 1]
for _ in range(10):
    fib.append(fib[-1] + fib[-2])
print(fib)

def quadrado(tam):
    for _ in range(4):
        ande(tam)
        esquerda()

for t in fib:
    quadrado(5 * t)
    ande(5 * t)
    direita()



saveFrame('fib.png')
