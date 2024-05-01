import py5_tools  #!REMOVE

# setup: configurações iniciais #0given
def setup(): #0given
    size(400, 400) #1given
    #!REMOVE code to capture animation
    py5_tools.animated_gif(file + '.gif', #!REMOVE
                           duration=0.2,  #!REMOVE 
                           frame_numbers=range(10,140,2)) #!REMOVE
# draw: código que repete #0given    
def draw(): #0given
    fill(255) # preenchimento branco
    no_stroke() # desliga traço
    circle(mouse_x, mouse_y, 50) #1given
    fill(0, 0, 255) # preenchimento azul
    stroke_weight(3) # traço mais espesso
    stroke(255, 255, 0) # traço amarelo
    square(200, 250, 50)
    
# END OF PUZZLE - GENERATING METADATA
file = Path(__file__).stem
name = 'Desenho, cor e a interação com o mouse'
subt = 'Formas básicas, preenchimento, traço e interação usando draw()'
dcat = '100 Primeiros passos'
desc = (
f"""<h6>{name}</h6></br>"""
f"""<img src="parsons_probs/{file}.gif"></br>"""
f"""<code>{name}</code></br>"""
f"""Organize os blocos para fazer um sketch como este."""
f"""Note que o círculo, com a posição controlada pela ponta do mouse"""
f""" não tem traço de contorno, e que o quadrado, sempre redesenhado"""
f""" no mesmo lugar, tem um traço de contorno amarelo mais espesso."""
    )

def format_source():
    with open(__file__) as f:
        code_lines = ''
        for lin in f.readlines():
            if lin.startswith('# END'):
                break
            elif '!REMOVE' in lin:
                continue
            elif '!BLANK' in lin:
                lin.lstrip('#')  # to add comments with !BLANK to puzzle
            lin = lin.strip(' ') # this preserves \n
            if lin.strip(): # skip empty lines as .strip() removes \n
                code_lines += '  ' + lin
    return code_lines

def exiting():
    #save(file + '.png')  # save image result
    print(file)
    code_lines = format_source()
    yaml = f"""\
problem_name: {name} 

problem_subtitle: {subt}

problem_category: {dcat}

problem_description: |
  {desc}
   
code_lines: |
{code_lines}
  
test_fn: setup
"""
    with open(file + '.yaml', 'w') as f:
        f.write(yaml)
    
