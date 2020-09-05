"""
The base for this "glitch" is a fork of (@aparrish) Allison Parrish's amazing example using Flat + Bezmerizing to draw SVG.
I'm using a bizarre set of functions in flat_processing.py to make flat look like Processing Python mode I'm more used to.

Many thanks to Marco Aurelio "Macarena"
"""

import random
from flask import Flask, send_file, request
from flat_processing import *

sf = 1
sf_value = 10
sf_min = 1
sf_max = 20
colunas = 8
seed_value = 1

gliphs = [lambda x, y, s: rect(x, y, s, s),
          lambda x, y, s: ellipse(x, y, s, s),
          lambda x, y, s: triangle(x - s, y, x - s, y + s, x, y + s),
          lambda x, y, s: triangle(x + s, y, x + s, y - s, x, y - s),
          ]


def ensamble(ex, ey, eo):
    noStroke()
    for i in range(eo):
        if i % 2:
            fill(150, 0, 150, 150)
        else:
            fill(0, 50, 150, 150)
        order, spacing, side = random.randint(3, 6), 14, 7
        x = (1 + random.randint(-5, 4)) * side * sf
        y = (1 + random.randint(-5, 4)) * side * sf
        grid(ex+x,
             ey+y,
             order,
             spacing * sf,
             random.choice(gliphs),
             side * sf)

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


app = Flask(__name__)

@app.route('/draw.svg', methods=['GET'])
def draw():
    global colunas, sf_value, sf, seed_value
    query = request.url[len(request.base_url):]
    colunas_value = request.args.get('colunas') or colunas
    sf_value = request.args.get('sf') or sf_value
    sf = int(sf_value) / 10
    seed = request.args.get('seed') or seed_value
    seed_value = int(seed)
    
    size(1400 * sf, 700 * sf)
    background(240, 240, 200)
    
    print(f"seed: {seed_value}")
    random.seed(seed_value)  
    grid(width / 2, height / 2, (colunas, 4), 150 * sf, ensamble, 5)
    
    page.svg('temp.svg')
    return send_file("temp.svg", mimetype='image/svg+xml')

@app.route('/', methods=['GET'])
def index():
  global sf_value, colunas, sf, seed_value  
  query = request.url[len(request.base_url):]
  colunas_value = request.args.get('colunas') or colunas
  colunas = int(colunas_value)  
  sf_value = request.args.get('sf') or sf_value
  sf = int(sf_value) / 10
  seed = request.args.get('seed') or seed_value
  seed_value = int(seed)
  
  return f"""<html>
  <head><link href="https://fonts.googleapis.com/css2?family=Source+Code+Pro:wght@200&display=swap" rel="stylesheet"></head> 
  <body>
  <form action="" method="GET">
  <font face="Source Code Pro, monospace">
  <label for="colunas"> cols </label>
  <input id="colunas" name="colunas" value="{colunas_value}" />
  <label for="seed">seed </label>
  <input id="seed" name="seed" value="{seed_value}" />
  <label for="sf"> scale ({sf_value}) </label>
  <input id="sf" type="range" name="sf" min="{sf_min}" max="{sf_max}" value="{sf_value}" />
  <input type="submit" value="redraw">
  </font>
  </form>
  <img src="draw.svg{query}">
  </body>
  </html>
"""   

if __name__ == '__main__':
    app.run()
