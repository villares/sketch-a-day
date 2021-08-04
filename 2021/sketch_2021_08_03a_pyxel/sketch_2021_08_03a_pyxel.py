
import pyxel


class App:
    def __init__(self):
        pyxel.init(60, 90, caption="Hello Pyxel")
        #pyxel.image(0).load(0, 0, "assets/pyxel_logo_38x16.png")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(pyxel.frame_count % 2)
        for y in range(16):
            pyxel.text(5, 5 + 5 * y, "Hello, Pyxel!", y)
        pyxel.blt(61, 66, 0, 0, 0, 38, 16)


App()