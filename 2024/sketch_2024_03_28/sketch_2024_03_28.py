tamanho = 10  # global
tam_letra = 10 

# ascii = """ `.-'~_,!+^:><=*;")/(?|7i[]}{vcLTlxY1zstyJfn2oCFIuej#3aV%5Z4k$XE6SPh9AwU80GqpKbdmO@HD&NgRMWBQ"""

lorem = """Lorem ipsum dolor sit amet. Non voluptatum sequi et officia recusandae aut fugit"""
"""similique non dicta omnis sed Quis sint! Vel ducimus nobis eos placeat repellat et deserunt nemo non reiciendis perferendis a porro sint est similique quia. Ad officia nulla ab fugit quas qui reiciendis dolor sed delectus eligendi. Qui quis unde ut accusantium omnis et ducimus nobis.
Rem galisum veritatis sit harum voluptas eos minus quas. Ab impedit natus sit quaerat nesciunt ut enim provident est iste repudiandae! Sit nihil obcaecati At suscipit autem et magni cumque non nisi aliquam! Ut aliquid consequatur et illo provident est beatae maxime?"""


def setup():
    #global img
    global osb  # offscreen buffer 
    size(800, 795)
    #img = load_image('imagem.jpg')        
    f = create_font('Source Code Pro Bold', 24)
    text_font(f)
    osb = create_graphics(width, height)
    osb.begin_draw()
    osb.background(255)
    #osb.clear()
    osb.text_size(250)
    osb.text_align(CENTER, CENTER)
    osb.fill(0)
    for _ in range(20):
        osb.fill(random(255), random(255), random(255))
        osb.text('HELLO', random(width), random(height))
    osb.end_draw()
    
def draw():
    no_stroke()
    background(0)
    colunas = int(width / tamanho)
    filas = int(height / tamanho)
    i = 0
    for num_fila in range(filas):
        y = tamanho / 2 + tamanho * num_fila
        for num_col in range(colunas):  # num_col 0, 1, 2 ... 19
            x = tamanho / 2 + tamanho * num_col
            cor = conta_gotas(x, y, osb)
            fill(cor)
            b = brightness(cor) # 0 ... 255
            d = remap(b, 0, 255, tamanho, 0)
            text_size(tam_letra)
            if b < 250:
                text(lorem[i % len(lorem)], x, y)
                i += 1
   
def conta_gotas(x, y, img_source):
    xi = int(remap(x, 0, width, 0, img_source.width))
    yi = int(remap(y, 0, height, 0, img_source.height))
    return img_source.get_pixels(xi, yi)
    
def key_pressed():
    global tamanho, tam_letra
    if key == '-' and tamanho > 1:
        tamanho -= 1
    elif key == '+' or key == '=':
        tamanho += 1
    elif key_code == DOWN and tam_letra > 1:
        tam_letra -= 1
    elif key_code == UP:
        tam_letra += 1
    elif key == 's':
        save_frame('####.png')
    print(f'tam célula:{tamanho}  tam letra:{tam_letra}')
    #print('tam célula:{}  tam letra:{}'.format(tamanho, tam_letra))
               