
# setup: configurações iniciais
def setup(): #0given
    size(400, 400) #1given
    n = 8
    s = width / n
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                fill(255)
            else:
                fill(0)
            square(i * s,  j * s, s)
    
# END OF PUZZLE - GENERATING METADAA
file = Path(__file__).stem
name = 'Tabuleiro de xadrez'
subt = 'Grade com cores alternadas'
dcat = '130 - laços de repetição'
desc = (
f"""<h6>{name}</h6></br>"""
f"""<img src="parsons_probs/{file}.png"></br>"""
f"""<code>{subt}</code></br>"""
f"""Organize os blocos para o obter um desenho como este."""
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
    save(file + '.png')  # save image result
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
