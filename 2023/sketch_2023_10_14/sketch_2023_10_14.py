import py5

def setup():
    global gif
    py5.size(500, 500)
    gif = Py5Gif('a.gif')  # b.gif to test 1000 delay
    
def draw():
    gif.draw(50, 50, 400, 400)

class Py5Gif():

    def __init__(self, pil_img):
        from itertools import count
        from PIL import Image

        if isinstance(pil_img, (py5.Path, str)):
            pil_img = Image.open(pil_img)
        self.loc = 0
        self.frames = []
        self.previous = 0

        try:
            for i in count(1):
                self.frames.append(py5.convert_image(pil_img.copy()))
                pil_img.seek(i)
        except EOFError:
            pass

        try:
            self.delay = pil_img.info['duration']
            # print(f'{self.delay} delay from info')
        except:
            self.delay = 100
            # print(f'{self.delay} delay from default')

    def draw(self, x, y, w=None, h=None):
        if not self.previous:
            self.previous = py5.millis()
        elif py5.millis() - self.previous > self.delay:
            # print(py5.millis() - self.previous, py5.millis(), self. previous)
            self.loc = (self.loc + 1) % len(self.frames)
            self.previous = py5.millis()
        py5.image(self.frames[self.loc], x, y, w, h)
        # print(self.loc)
        
py5.run_sketch(block=False)