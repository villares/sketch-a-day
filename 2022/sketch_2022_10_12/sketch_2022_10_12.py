def setup():
    size(500, 500)
    background(100)
    no_stroke()
    
def ponto_deslocado(xo, yo, raio, angulo):
    """ Devolve coordenadas a uma certa distância (raio)
    e em uma certa direção (ângulo) de um ponto xo, yo. """
    return (xo + cos(angulo) * raio,
            yo + sin(angulo) * raio)

def draw():
    a = atan2(mouse_y - 250, mouse_x - 250) # ang mouse centro
    d = dist(mouse_x, mouse_y, 250, 250) # distância mouse centro
    fill(d % 255)  # cinza que varia com a distância
    for i in range(6):
        a_rot = a + i * TWO_PI / 6  # soma i * 60° no ângulo
        x, y = ponto_deslocado(250, 250, d, a_rot)
        if is_mouse_pressed:
            circle(x, y, 5)  # desenha círculo
        
def key_pressed(e=None):
    background(100)  # aperte qualquer tecla para apagar

"""
https://berinhard.github.io/pyp5js/pyodide/?sketch=ZGVmJTIwc2V0dXAoKSUzQSUwQSUyMCUyMCUyMCUyMHNpemUoNTAwJTJDJTIwNTAwKSUwQSUyMCUyMCUyMCUyMGJhY2tncm91bmQoMTAwKSUwQSUyMCUyMCUyMCUyMG5vU3Ryb2tlKCklMEElMjAlMjAlMjAlMjAlMEFkZWYlMjBwb250b19kZXNsb2NhZG8oeG8lMkMlMjB5byUyQyUyMHJhaW8lMkMlMjBhbmd1bG8pJTNBJTBBJTIwJTIwJTIwJTIwJTIyJTIyJTIyJTIwRGV2b2x2ZSUyMGNvb3JkZW5hZGFzJTIwYSUyMHVtYSUyMGNlcnRhJTIwZGlzdCVDMyVBMm5jaWElMjAocmFpbyklMEElMjAlMjAlMjAlMjBlJTIwZW0lMjB1bWElMjBjZXJ0YSUyMGRpcmUlQzMlQTclQzMlQTNvJTIwKCVDMyVBMm5ndWxvKSUyMGRlJTIwdW0lMjBwb250byUyMHhvJTJDJTIweW8uJTIwJTIyJTIyJTIyJTBBJTIwJTIwJTIwJTIwcmV0dXJuJTIwKHhvJTIwJTJCJTIwY29zKGFuZ3VsbyklMjAqJTIwcmFpbyUyQyUwQSUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMHlvJTIwJTJCJTIwc2luKGFuZ3VsbyklMjAqJTIwcmFpbyklMEElMEFkZWYlMjBkcmF3KCklM0ElMEElMjAlMjAlMjAlMjBhJTIwJTNEJTIwYXRhbjIobW91c2VZJTIwLSUyMDI1MCUyQyUyMG1vdXNlWCUyMC0lMjAyNTApJTIwJTIzJTIwYW5nJTIwbW91c2UlMjBjZW50cm8lMEElMjAlMjAlMjAlMjBkJTIwJTNEJTIwZGlzdChtb3VzZVglMkMlMjBtb3VzZVklMkMlMjAyNTAlMkMlMjAyNTApJTIwJTIzJTIwZGlzdCVDMyVBMm5jaWElMjBtb3VzZSUyMGNlbnRybyUwQSUyMCUyMCUyMCUyMGZpbGwoZCUyMCUyNSUyMDI1NSklMjAlMjAlMjMlMjBjaW56YSUyMHF1ZSUyMHZhcmlhJTIwY29tJTIwYSUyMGRpc3QlQzMlQTJuY2lhJTBBJTIwJTIwJTIwJTIwZm9yJTIwaSUyMGluJTIwcmFuZ2UoNiklM0ElMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjBhX3JvdCUyMCUzRCUyMGElMjAlMkIlMjBpJTIwKiUyMFRXT19QSSUyMCUyRiUyMDYlMjAlMjAlMjMlMjBzb21hJTIwaSUyMColMjA2MCVDMiVCMCUyMG5vJTIwJUMzJUEybmd1bG8lMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjB4JTJDJTIweSUyMCUzRCUyMHBvbnRvX2Rlc2xvY2FkbygyNTAlMkMlMjAyNTAlMkMlMjBkJTJDJTIwYV9yb3QpJTBBJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwY2lyY2xlKHglMkMlMjB5JTJDJTIwNSklMjAlMjAlMjMlMjBkZXNlbmhhJTIwYyVDMyVBRHJjdWxvJTBBJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTBBZGVmJTIwa2V5UHJlc3NlZChlJTNETm9uZSklM0ElMEElMjAlMjAlMjAlMjBiYWNrZ3JvdW5kKDEwMCklMjAlMjAlMjMlMjBhcGVydGUlMjBxdWFscXVlciUyMHRlY2xhJTIwcGFyYSUyMGFwYWdhciUwQQ%3D%3D
"""