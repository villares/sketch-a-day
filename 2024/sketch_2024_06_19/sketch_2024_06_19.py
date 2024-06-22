
import py5

margem_h = 20
cols = 5
rows = 5

def setup():
    py5.size(int(297 * 1.8), int(420 * 1.8))
    py5.rect_mode(py5.CENTER)
    tam = (py5.width - 2 * margem_h) / cols
    margem_v = (py5.height - tam * rows) / 2
    py5.no_stroke()
    py5.background(0)
    py5.fill(200, 0, 200, 150)
    grade(margem_h, margem_v, py5.width - 2 * margem_h, cols, rows)
    py5.fill(0, 200, 200, 150)
    grade(margem_h, margem_v, py5.width - 2 * margem_h, cols, rows)
    py5.save('out.png')

def grade(margem_h, margem_v, largura_grade, cols, rows):
    tam = largura_grade / cols
    for j in range(rows):
        y = margem_v + j * tam
        for i in range(cols):
            x = margem_h + i * tam
            sorteio = py5.random_choice((0, 1, 2))
            if  sorteio == 0 and tam > 10:
                grade(x, y, tam, 3, 3)
            elif sorteio == 1:
                py5.circle(x + tam / 2, y + tam / 2, tam)
            else:
                py5.square(x + tam / 2, y + tam / 2, tam * 0.80)
                

    
py5.run_sketch()
