# [sketch-a-day](https://abav.lugaralgum.com/sketch-a-day)

#### coding a visual idea a day

Welcome! My name is [Alexandre Villares](https://abav.lugaralgum.com) and since January, 2018 I have been coding *sketches* everyday, publishing the source code in the same repository that stores this page, [github.com/villares/sketch-a-day](https://github.com/villares/sketch-a-day).

The results are mostly tentative, exploratory, and I don’t feel like they need to be relevant or meaningful on any particular day. The everyday practice leads to the emergence of ideas that I consider interesting, worthy of further exploration. Some of those have been added to [selected work](https://abav.lugaralgum.com/selected-work/index-EN.html), this collection itself became valuable for me, and it is my pleasure to share it with anyone willing to explore coding as a creative and expressive medium.

Please do not hesitate to [contact me](http://contato.lugaralgum.com) regarding licenses to use my work, teaching opportunities, consulting or other projects. Moreover, I kindly invite you to subscribe to my newsletter, [[sketch-mail](https://abav.lugaralgum.com/sketch-mail)]. If you appreciate what I have been doing, you may support my artistic work, research and open educational resources I publish on-line using [gumroad.com/villares](https://gumroad.com/villares), [PayPal](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=HCGAKACDMVNV2) or PIX at `46c37783-5edb-4f1c-b3a8-1309db11488c`.

Here are listed some of the tools I have been using:

- [[py5](https://py5coding.org/)] A new Processing Java + Python 3 amazing tool
- [[pyp5js](https://berinhard.github.io/pyp5js/)] initially a Python to p5js trancriptor, now a pyodide + p5js tool
- [[pyscript](https://pyscript.net)] A new Python in the browser tool.
- [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)] Processing Python mode
- [[Processing Java](https://processing.org]) Processing Java or "standard" mode
- [[p5.js](https://p5js.org)] JavaScript library from the Processing Foundation
- [[shoebot](https://shoebot.github.io/shoebot/)] Generate 2D vector graphics with Python
- [[FreeCAD](https://freecadweb.org)] A wonderful 3D modeling tool, CAD & more, Python infused.
- [[p5py](https://github.com/p5py/p5)] A Python 3 implementation of Processing ideas (no Java needed)
- [[flat](https://xxyxyz.org/flat)] A generative infrastructure library for Python (via Allison Parrish's [Bezmerizing](https://github.com/aparrish/bezmerizing))
- [[VPython](https://vpython.org/)] Python + glowscript gives you 3D on the browser
- [[PySimpleGUI](https://PySimpleGUI.org)] Python GUIs for Humans

<link
  rel="alternate"
  type="application/rss+xml"
  href="https://raw.githack.com/villares/sketch-a-day/main/rss.xml"
  title="RSS Feed">

---

## 2023 | [2022](2022.md) | [2021](2021.md) | [2020](2020.md) | [2019](2019.md) | [2018](2018.md)

---

### sketch_2023_01_02

![sketch_2023_01_02](2023/sketch_2023_01_02/sketch_2023_01_02.gif)

[sketch_2023_01_02](https://github.com/villares/sketch-a-day/tree/main/2023/sketch_2023_01_02) [[py5](https://py5coding.org/)]

Genuary 2 - 10 minutes

```python
def setup():
    size(600, 600)
    color_mode(HSB)
    no_stroke()
    rect_mode(CENTER)
    
def draw():
    background(0)
    m = frame_count #1 + mouse_x // 10
    for x in range(100):
        cx = 50 + x * 5
        for y in range(100):
            cy = 50 + y * 5
            c = (x ^ y) ** 13 % m
            fill(c * (255 / m), 255, 255)
#             print(c, cx, cy)
            square(cx, cy, 5)

    if frame_count % 10 == 0 and frame_count <= 100:
        save_frame('###.png')
```

---

### sketch_2023_01_01

![sketch_2023_01_01](2023/sketch_2023_01_01/sketch_2023_01_01.gif)

[sketch_2023_01_01](https://github.com/villares/sketch-a-day/tree/main/2023/sketch_2023_01_01) [[py5](https://py5coding.org/)]

Genuary 1 - loop

```python
def setup():
    size(600, 600)
    blend_mode(ADD)
    no_stroke()
    
def draw():
    background(0)
    xc = yc = 300
    r = 250
    for i in range(6):
        m = cos(radians(frame_count / 2)) ** 2
        a = radians(frame_count / 2 + 60 * i)
        x = xc + r * cos(a)
        y = yc + r * sin(a)
        fill(0, 0, 255)
        circle(x, y, 50)
        x = xc + r * cos(a * m)
        y = yc + r * sin(a * m)
        fill(0, 255, 0)
        circle(x, y, 50)
        x = xc + r * cos(a * -m)
        y = yc + r * sin(a * -m)
        fill(255, 0, 0)
        circle(x, y, 50)
```

---

## 2023 | [2022](2022.md) | [2021](2021.md) | [2020](2020.md) | [2019](2019.md) | [2018](2018.md)

---

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/">The <a property="dct:title" rel="cc:attributionURL" href="https://abav.lugaralgum.com/sketch-a-day">sketch-a-day</a> project, images and code repository, by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://abav.lugaralgum.com">Alexandre B A VIllares</a> are licensed under <a href="http://creativecommons.org/licenses/by-nc-nd/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution-NonCommercial-NoDerivatives 4.0 International <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nd.svg?ref=chooser-v1"></a>, except if marked/attributed otherwise in a file or code section. Please contact for licensing questions.</p>

