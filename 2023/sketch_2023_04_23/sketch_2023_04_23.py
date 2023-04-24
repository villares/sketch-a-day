fator_escala = 10
salvar_svg = False

def setup():
    size(200, 200)  # com fator 10, vira 2000px x 2000px
    
def draw():
#    if salvar_svg:
#        svg_output.scale(fator_escala)
    fill(255, 32)
    if is_mouse_pressed:    
        circle(mouse_x, mouse_y, width / 10)        
        
def key_pressed():
    global salvar_svg, file_name, svg_output
    if key == 'h':
        if not salvar_svg:
            salvar_svg = True
            background(200) # limpa a tela (mas não entra na gravação)
            file_name = f'{frame_count}.svg' 
            svg_output = create_graphics(
                width * fator_escala, height * fator_escala, SVG, file_name)
            begin_record(svg_output)
            print(f'iniciando a gravação de {file_name}')
        else:
            salvar_svg = False
            end_record()
            print(f'{file_name} gravado.')




