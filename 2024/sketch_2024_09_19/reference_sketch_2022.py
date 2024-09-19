from random import randint
import py5

def setup():  
    py5.size(900, 900)
    py5.text_align(py5.CENTER, py5.CENTER)
    py5.text_size(8)
    set_records()  # inventa uns dados aleatórios para testar na global "records"
    
def draw():   
    py5.background(0)
    # desenhar uma visulização dos dados na variável global records
    draw_records(records, 0, 0, py5.width, py5.height, margin=0)

def draw_records(records, xo, yo, wo, ho, **kwargs):
    """Desenha os dados como uma visualização de áreas"""
    margin = kwargs.pop('margin', 5)  # trata keyword argument margin=, default 5
    x, y = xo + margin, yo + margin,  # aplica margem na posição da origem
    w, h = wo - 2 * margin, ho - 2 * margin  # aplica margem (subtrai) nas dimensões 
    total_area = sum(map(lambda r: r[1], records))  # calcula soma dos valores dos registros
    rx = ry = 0
    for i, (name, area, sub) in enumerate(records):
        py5.color_mode(py5.HSB) # matiz, saturação, brilho
        py5.fill(py5.color(255.0 * area / total_area, 200, 200))
        if w > h:  # para retângulos horizontais
            rw, rh = py5.remap(area, 0, total_area, 0, w), h
        else:      # para retângulos verticais
            rw, rh = w, py5.remap(area, 0, total_area, 0, h)       
        py5.rect(x + rx, y + ry, rw, rh)
        if sub:  # se tiver sub-áreas, chama recursivamente a função
            draw_records(sub, x + rx, y + ry, rw, rh)
        else:
            py5.fill(0)
            py5.text(name, x + rx + rw /2 , y + ry + rh / 2)
        if w > h:  # para retângulos horizontais
            rx += rw
        else:      # para retângulos verticais
            ry += rh

def key_pressed():
    """Função invocade pelo py5 nos eventos de teclado"""
    py5.save_frame('###.png')
    set_records()  # novos dados aleatórios serão criados

def set_records():
    global records
    records = generate_record(3) # inventa dados com potenciais 3 níveis aninhados
    
def generate_record(levels, name='', max_elements=5):
    "Gera dados aleatórios para testar o desenho das áreas"
    if name:
        name += '.'  # nos sub-níveis acrescenta separador
    result = []
    for i in range(max_elements):
        # decide aleatoriamente se faz um registro simples ou com sub-registros
        if py5.random_choice((True, False)) or levels == 1:
            # ramo que gera um registro simples
            valor = randint(1, 5) # valor aleatório, vira área
            result.append(
                (name + chr(65+i), valor, [])
            )
        else:  # ramo que gera sub-registros
            valor = randint(2, 5) # valor aleatório, vira área
            result.append(
                (
                name + chr(65+i), valor,
                generate_record(levels - 1, name + chr(65+i)) # sub-registros
                )
            )
    return result                
 
py5.run_sketch()
    
    
    
