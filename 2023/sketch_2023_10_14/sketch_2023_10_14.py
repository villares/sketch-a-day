from itertools import count
from PIL import Image
import py5

def setup():
    global gif
    py5.size(500, 500)
    gif = Py5Gif('a.gif')
    
def draw():
    gif.draw(50, 50, 400, 400)

class Py5Gif():
    def __init__(self, pil_img):
        if isinstance(pil_img, (py5.Path, str)):
            im = Image.open(pil_img)
        self.loc = 0
        self.frames = []
        self.previous = None

        try:
            for i in count(1):
                self.frames.append(py5.convert_image(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

    def draw(self, x, y, w=None, h=None):
        if not self.previous or py5.millis() - self.previous > self.delay:
            self.loc = (self.loc + 1) % len(self.frames)
            self.previous = py5.millis()
        py5.image(self.frames[self.loc], x, y, w, h)
        
py5.run_sketch(block=False)