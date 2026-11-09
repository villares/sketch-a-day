"""
This is an "imported mode" py5 sketch, to run it you'll need to have py5
installed then use `py5-run-sketch`, or `python -m py5_tools run-sketch`
(or the thonny-py5mode plug-in on Thonny). Learn more at <https://py5coding.org>

An L-System example made during class.
"""
from py5_tools import animated_gif

axioma = '-X'
regras = {
 'X': 'F+[[X]-X]-F[-FX]+X0',
 'F' : 'FF',   
}
passo = 2
angulo = 33  # em graus

def setup():
    global frase
    size(800, 800, P3D)
    frase_inicial = axioma
    for i in range(6):
        frase = ''
        for simbolo in frase_inicial:
            frase = frase + regras.get(simbolo, simbolo)
        frase_inicial = frase
    print(len(frase))
    animated_gif(
        'out.gif',
        frame_numbers=range(1, 361, 10),
        duration=0.1,   
    )
    
def draw():
    background(200, 200, 255)
    translate(400, 400)
    rotate_y(radians(frame_count))
    desenha_frase(angulo)
    desenha_frase(-angulo)
    scale(1, -1)
    desenha_frase(angulo)
    desenha_frase(-angulo)
        
    #circle(0, 0, 10)
    
def desenha_frase(angulo):
    push_matrix()
    for simbolo in frase:
        if simbolo == 'F':
            line(0, 0, 0, -passo)
            translate(0, -passo)
            rotate_y(angulo)
        elif simbolo == '-':
            rotate(radians(angulo))
        elif simbolo == '+':
            rotate(radians(-angulo))
        elif simbolo == '[':
            push_matrix()
        elif simbolo == ']':
            pop_matrix()
        elif simbolo == '0':
            no_stroke()
            circle(0, 0, passo * 2)
            stroke(0)
    pop_matrix()
            
def key_pressed():
    global angulo, passo
    if key == 'a':
        angulo = angulo + 5
    elif key == 'z':
        angulo = angulo - 5
    elif key == 's' or key_code == UP:
        passo = passo + 1
    elif  key == 'x' or key_code == DOWN:
        passo = passo - 1         
    elif key == 'p':
        save_frame('####.png')



