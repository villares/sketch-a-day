import py5_tools
import py5
from shutil import copytree
from pathlib import Path

pp2i = py5_tools.translators.processingpy2imported

# Material aulas
#source_dir = '/home/villares/GitHub/material-aulas/Processing-Python'
#target_dir = '/home/villares/GitHub/material-aulas/Processing-Python-py5'
# Rosetta examples repo
#source_dir = '/home/villares/GitHub/rosetta_examples_p5/examples/Python/'
#target_dir = '/home/villares/GitHub/rosetta_examples_p5/examples/py5/'
# Python mode examples
#source_dir = '/home/villares/sketchbook/modes/PythonMode/examples/'
#target_dir = '/home/villares/GitHub/py5examples/examples-from-Processing-Python-mode/'

rules = {
#     'PVector()' : lambda s: s.replace('PVector()', 'Py5Vector()'), # 3D default
    'PVector()' : lambda s: s.replace('PVector()', 'Py5Vector(0, 0)'), # assuming 2D default
    'PVector.sub(' : lambda s: replace_pv_method(s, 'sub'),
    'PVector.add(' : lambda s: replace_pv_method(s, 'add'),
    'PVector.mult(' : lambda s: replace_pv_method(s, 'mult'),
    'PVector.div(' : lambda s: replace_pv_method(s, 'div'),
    '.add(' : lambda s: replace_method(s, 'add'),   # DANGEROUS, because sets!
    '.mult(' : lambda s: replace_method(s, 'mult'),
    '.sub(' : lambda s: replace_method(s, 'sub'),
    '.div(' : lambda s: replace_method(s, 'div'),
    'PVector.fromAngle(' : lambda s: s.replace('PVector.fromAngle(', 'Py5Vector.heading('),
    'PVector.random2D()' : lambda s: s.replace('PVector.random2D()', 'Py5Vector.random(2)'), 
    'PVector.random3D()' : lambda s: s.replace('PVector.random3D()', 'Py5Vector.random(3)'), 
    '.heading()':  lambda s: s.replace('.heading()', '.heading'),
    '.mag()':  lambda s: s.replace('.mag()', '.mag'),
    }

def modified_line(txt: str):
    for rule_key, func in rules.items():
        if rule_key in txt:
            txt = func(txt)
    return txt    

def replace_pv_method(txt: str, method: str):
    op = {'sub': ' -', 'add': ' +', 'mult': ' *', 'div': ' /'}
    pv_method = 'PVector.' + method + '('
    start = txt.find(pv_method)
    if start == -1:
        return txt
    end = txt.find(')', start)  # very dangerous... should improve this
    head = txt[:start]
    middle = txt[start + len(pv_method):end].replace(',', op[method])
    tail = txt[end+1:]
    return head + middle + tail 

def replace_method(txt: str, method: str):
    op = {'sub': ' -= ', 'add': ' += ', 'mult': ' *= ', 'div': ' /= '}
    dot_method = '.' + method + '('
    start = txt.find(dot_method)
    end = txt.find(')', start)  # very dangerous... should improve this
    head = txt[:start] + op[method]
    middle = txt[start + len(dot_method):end]
    tail = txt[end+1:]
    return head + middle + tail 
    
    
def in_place_dir_change(src, ext='.py', dry_run=True):
    src_path = Path(src)
    count = 0
    for src_file in src_path.glob('**/*' + ext):
        try:
            in_place_file_changes(src_file,dry_run)
            # print("translated " + str(src_file.relative_to(src)))
            count += 1
        except IsADirectoryError:
            pass
        except BaseException as e:
            print("error translating " + str(src_file.relative_to(src)))
            print(repr(e))

    print(
        "complete: ",
        count,
        "files modified in place" if not dry_run else "Dry run! No modifications made"
        )

            
def in_place_file_changes(path_to_text_file, dry_run=False):            
    with open(path_to_text_file,'r', encoding='utf-8') as txt:
        if not dry_run:
            new_lines = (modified_line(li) for li in txt.readlines())
        else:
            new_lines = txt.readlines()
            for li in new_lines:
                m = modified_line(li)
                if m !=li:
                    print('original: ', li, end='')
                    print('proposed: ', m, end='')

    with open(path_to_text_file,'w') as txt:
        txt.writelines(new_lines)

#src = '/home/villares/GitHub/py5examples/examples-from-Processing-Python-mode/'
src = '/home/villares/GitHub/processing-python/play/'
in_place_dir_change(src, dry_run=False)