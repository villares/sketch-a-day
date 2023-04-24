fator_escala = 10
salvar_png = False

def setup():
    size(200, 200)  # com fator 10, vira 2000px x 2000px

def draw():
    if salvar_png:
        output_buffer.scale(fator_escala)   
    circle(mouse_x, mouse_y, width / 5)        
        
def key_pressed():
    global salvar_png, file_name, output_buffer
    if key == 'h':
        if not salvar_png:
            salvar_png = True
            background(200) # limpa a tela (mas não entra na gravação)
            output_buffer = create_graphics(width * fator_escala,
                                        height * fator_escala)
            begin_record(output_buffer)
            file_name = f'{frame_count}.png' 
            print(f'iniciando a gravação de {file_name}')
        else:
            salvar_png = False
            output_buffer.save(file_name, drop_alpha=False)
            end_record()
            print(f'{file_name} gravado.')




