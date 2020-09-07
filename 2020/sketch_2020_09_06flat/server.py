"""
Yeah I know, this is called sketch_2020-09-06flat but the URL is missing the -09

The base for this "glitch" is a fork of (@aparrish) Allison Parrish's amazing example using Flat + Bezmerizing to draw SVG.
Lot's of help from Marco Macarena adding the HTML inputs!
This version uses a single flask route, generates and inserts the SVG inside the HTML it serves. The other route is optional, to serve a single SVG
"""

from flask import Flask, send_file, request
import random

from flat_processing import *

sf = 1
sf_value = 10
sf_min = 1
sf_max = 40
colunas = 8
seed_value = 100

gliphs = (lambda x, y, s: rect(x, y, s, s),
          lambda x, y, s: ellipse(x, y, s, s),
          lambda x, y, s: triangle(x - s, y, x - s, y + s, x, y + s),
          lambda x, y, s: triangle(x + s, y, x + s, y - s, x, y - s),
         )

colors = ((0, 50, 150, 150),
          (200, 50, 0, 150)
          )

def draw():
    size(1400 / 8 * sf * colunas, 700 * sf)
    background(235, 235, 220)
    
    print(f"seed: {seed_value}")
    random.seed(seed_value)
    grid(width / 2, height / 2, (colunas, 4), 150 * sf, ensamble, 5)

    
def grid(x, y, order, spacing, function, *args):  
    if type(order) is tuple:
        cols, rows = order
    else:
        cols = rows = order
    xo, yo = (x - cols * spacing / 2 , y - rows * spacing / 2)
    for i in range(cols):
        gx = spacing / 2 + i * spacing
        for j in range(rows):
            gy = spacing/2 + j * spacing
            function(xo + gx, yo + gy, *args)


def ensamble(ex, ey, eo):
    noStroke()
    for i in range(eo):
        fill(*colors[i % len(colors)])
        order, spacing, side = random.randint(3, 6), 14, 7
        x = (1 + random.randint(-5, 4)) * side * sf
        y = (1 + random.randint(-5, 4)) * side * sf
        grid(ex+x,
             ey+y,
             order,
             spacing * sf,
             random.choice(gliphs),
             side * sf)
    
app = Flask(__name__)
        
def treat_request(request):
  global sf_value, sf
  global colunas_value, colunas
  global seed_value, seed_request  
  colunas_value = request.args.get('colunas') or colunas
  colunas = int(colunas_value)  
  sf_value = request.args.get('sf') or sf_value
  sf = int(sf_value) / 10
  
  seed_request = request.args.get('seed') or str(seed_value)
  seed_value = int(seed_request)
  
  if request.args.get('randomize'):
      seed_value = random.randint(1, 10e10)
  

  
@app.route('/sketch.svg', methods=['GET'])
def svg():
  treat_request(request)
  draw()
  svg = page.svg().decode("utf-8")
  license = """generated with https://glitch.com/~sketch-2020-06flat by Alexandre B A Villares\nlicensed under CC-BY-NC-SA 4.0 - donate at gumroad.com/villares"""
  
  return svg.replace("Untitled", license) 

@app.route('/', methods=['GET'])
def index():
  treat_request(request)
  draw()
  svg_link = request.url.replace('.me/', '.me/sketch.svg')
  svg_link = svg_link.replace('randomize=randomize&', '')
  if seed_request:
      svg_link = svg_link.replace(seed_request, str(seed_value))

  license = """ generated with <a rel="cc:attributionURL" property="dct:title"
href="https://glitch.com/~sketch-2020-06flat">sketch-2020-09-08flat</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://abav.lugaralgum.com">Alexandre B A Villares</a> licensed under <a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0">CC BY-NC-SA 4.0 <img style="height:12px!important;margin-left:3px;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" /><img style="height:12px!important;margin-left:3px;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" /><img style="height:12px!important;margin-left:3px;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1" /><img style="height:12px!important;margin-left:3px;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1" /></a> (<a href="https://gumroad.com/villares">keep this online, donate</a>)</p>
"""
  return f"""
  <html><head><title>sketch_2020-09-06flat by Alexandre B A Villares</title></head>
  <body>
  <form action="" method="GET">
  <font face="Source Code Pro, monospace">
  <label for="seed">seed </label>
  <input id="seed" name="seed" value="{seed_value}" />
  <input type="submit" name="randomize" value="randomize">
  <label for="colunas"> cols </label>
  <input id="colunas" name="colunas" value="{colunas_value}" />
  <label for="sf"> scale ({sf_value}) </label>
  <input id="sf" type="range" name="sf" min="{sf_min}" max="{sf_max}" value="{sf_value}" />
  <input type="submit" name="redraw" value="redraw">
  <br /><a href={svg_link}>sketch.svg</a> {license}
  </font>
  </form>
  <p style="font-family:Source Code Pro, monospace" xmlns:dct="http://purl.org/dc/terms/" xmlns:cc="http://creativecommons.org/ns#" class="license-text">
  {page.svg().decode("utf-8")}
  </body></html>"""  


if __name__ == '__main__':
    app.run()
