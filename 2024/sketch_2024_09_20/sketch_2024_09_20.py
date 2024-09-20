from random import randint
import py5

records: list[tuple] = [
    ('agua', 50, []),
    ('ar', 75, []),
    ('fogo', 25, [
        ('fogo brando', 50, []),
        ('fogo alto', 50, [])
        ]),
    ('terra', 50, []),
    ]

def setup():  
    py5.size(900, 900)
    py5.text_align(py5.CENTER)
    py5.text_size(12)
    py5.color_mode(py5.HSB)
    
def draw():   
    py5.background(255 - 16 * len(records), 100, 200)
    # desenhar uma visulização dos dados na variável global records
    draw_records(records, 0, 0, py5.width, py5.height, margin=0)

def record_area(r):
    return r[1]
    
def sum_record_areas(areas):
    return sum(map(record_area, areas))

def draw_records(rcrds, xo, yo, wo, ho, **kwargs):
    """Desenha os dados como uma visualização de áreas"""
    margin = kwargs.pop('margin', 0)  # trata keyword argument margin=, default 0
    x, y = xo + margin, yo + margin  # aplica margem na posição da origem
    w, h = wo - 2 * margin, ho - 2 * margin  # aplica margem (subtrai) nas dimensões
    total_area = sum_record_areas(rcrds)  # calcula soma dos valores dos registros
    rcrds = sorted(rcrds, key=lambda r:r[0])  # by name
    if len(rcrds) == 1:
        name, _, sub = rcrds[0]
        if sub:  # se tiver sub-áreas, chama recursivamente a função
            py5.fill(255 - 16 * len(sub), 100, 200, 100)
            py5.rect(x, y, w, h)
            draw_records(sub, x, y, w, h, margin=5)
        else:
            py5.no_fill()
            py5.rect(x, y, w, h)
        with py5.push():
            py5.text_size(py5.remap(h, 0, py5.height, 6, 56))        
            py5.fill(0)
            py5.text(name, x + w / 2, y + h / 2)
    else:
        n = len(rcrds) // 2
        a = rcrds[:n]
        area_a = sum_record_areas(a)
        b = rcrds[n:]
        if w > h:  # para retângulos horizontais
            aw, ah = py5.remap(area_a, 0, total_area, 0, w), h
            draw_records(a, x, y, aw, ah)
            draw_records(b, x + aw, y, w - aw, h)
        else:      # para retângulos verticais
            aw, ah = w, py5.remap(area_a, 0, total_area, 0, h) 
            draw_records(a, x, y, aw, ah)
            draw_records(b, x, y + ah, w, h - ah)

def key_pressed():
    """Função invocade pelo py5 nos eventos de teclado"""
    py5.save_frame('###.png')
    set_records()  # novos dados aleatórios serão criados

def set_records():
    global records
    records = generate_record(3, min_elements=4) # inventa dados com potenciais 3 níveis aninhados
    
def generate_record(levels, name='', min_elements=2) -> list[tuple]:
    "Gera dados aleatórios para testar o desenho das áreas"
    if name:
        name += '.'  # nos sub-níveis acrescenta separador
    result: list[tuple] = []
    elements = py5.random_int(min_elements, 10)
    for i in range(elements):
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
    
    
    
