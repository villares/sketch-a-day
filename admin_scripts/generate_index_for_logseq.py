#!/home/villares/thonny-env/bin/python

# Prepara versão das páginas índice de cada ano do sketch-a-day para o logseq
# Tem várias referências "hard coded" das pastas no meio, só vai funcionar no meu Linux...
# ...com uma estrutura de pastas muito específica.

import re
from pathlib import Path

input_path_template = '/home/villares/GitHub/sketch-a-day/docs/{}.md'
output_path_template = '/home/villares/GitHub/logseq/pages/sketch-a-day-{}.md'


def sketch_date(line):
    # Define the regex patterns 
    p6 = r'sketch_\d{6}' # sketch_NNNNNN
    p8 = r'sketch_\d{4}_\d{2}_\d{2}' # sketch_NNNN_NN_NN
    # If a match is found, return the matched string
    if match := re.search(p6, line):
        d = match.group(0)[7:]
        return '20' + d[0:2], d[2:4], d[4:6]
    elif match := re.search(p8, line):
        d = match.group(0)[7:7+10]
        return d.split('_')   
    else:
        return None

def generate_sketch_a_day_index(min_year=2018, max_year=2030):
    for s_year in range(min_year, max_year + 1):
        s_year = str(s_year)
        # open the source markdown page from the sketch-a-day repo
        input_path = Path(input_path_template.format(s_year))
        output_path = Path(output_path_template.format(s_year))        
        if not input_path.is_file():
            continue
        with open(input_path, 'rt') as readme:
            readme_as_lines = readme.readlines()
        # Gera uma página em markdown para usar com o logseq
        with open(output_path, 'wt') as readme:
            writing = False # até a linha com os links dos anos, as linhas ignoradas
            for line in readme_as_lines:
                if r'.md) \| [<b>2' in line : # se for a linha com links dos anos
                    index_links = []  # monta uma nova lista de links
                    for y in range(min_year, max_year + 1):
                        if str(y) == s_year: # ano deste arquivo não é link
                            index_links.append(f"**{s_year}**") 
                        else: # muda link para página logseq/local do ano
                            index_links.append(f"[{y}](sketch-a-day-{y})")
                    readme.write(r' \| '.join(index_links))
                    writing = True # liga o processamento de linhas daqui por diante
                elif writing:
                    # Títulos ganham o [[ ]] para linkar no Journal
                    if line.startswith('###') and (date_tuple := sketch_date(line)):
                        line = line[:-1] + ' [[{}-{}-{}]]\n'.format(*date_tuple)
                    # Imagens passam a referenciar as imagens locais
                    elif '![' in line:
                        line = '' + line.replace(
                            'https://raw.githubusercontent.com/villares/sketch-a-day/main/',
                            '/home/villares/GitHub/sketch-a-day/')
                    # Linha com link para o github passa a referenciar pasta local
                    elif 'https://github.com/villares/sketch-a-day/tree/' in line:
                        line = '' + (line.replace('https://github.com/villares/',
                                            'file:///home/villares/GitHub/')
                                            .replace('tree/main/', '')
                                            .replace('tree/master/', ''))
                    readme.write(line)

if __name__ == '__main__':
    generate_sketch_a_day_index()