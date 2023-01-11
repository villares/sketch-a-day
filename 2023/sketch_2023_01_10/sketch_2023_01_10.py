import math

import pyxel


class App:
    def __init__(self):
        pyxel.init(200, 150)

        pyxel.sound(0).set(
            "e2e2c2g1 g1g1c2e2 d2d2d2g2 g2g2rr" "c2c2a1e1 e1e1a1c2 b1b1b1e2 e2e2rr",
            "p",
            "6",
            "vffn fnff vffs vfnn",
            25,
        )

        pyxel.sound(1).set(
            "r a1b1c2 b1b1c2d2 g2g2g2g2 c2c2d2e2" "f2f2f2e2 f2e2d2c2 d2d2d2d2 g2g2r r ",
            "s",
            "6",
            "nnff vfff vvvv vfff svff vfff vvvv svnn",
            25,
        )

        pyxel.sound(2).set(
            "c1g1c1g1 c1g1c1g1 b0g1b0g1 b0g1b0g1" "a0e1a0e1 a0e1a0e1 g0d1g0d1 g0d1g0d1",
            "t",
            "7",
            "n",
            25,
        )

        pyxel.sound(3).set(
            "f0c1f0c1 g0d1g0d1 c1g1c1g1 a0e1a0e1" "f0c1f0c1 f0c1f0c1 g0d1g0d1 g0d1g0d1",
            "t",
            "7",
            "n",
            25,
        )

        pyxel.sound(4).set(
            "f0ra4r f0ra4r f0ra4r f0f0a4r", "p", "6622 6622 6622 6422", "f", 25
        )

        self.play_music(False, True, False)

        pyxel.run(self.update, self.draw)

    def play_music(self, ch0, ch1, ch2):
        if ch0:
            pyxel.play(0, [0, 1], loop=True)
        else:
            pyxel.stop(0)

        if ch1:
            pyxel.play(1, [2, 3], loop=True)
        else:
            pyxel.stop(1)

        if ch2:
            pyxel.play(2, 4, loop=True)
        else:
            pyxel.stop(2)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_1):
            self.play_music(True, True, True)

        if pyxel.btnp(pyxel.KEY_2):
            self.play_music(True, False, False)

        if pyxel.btnp(pyxel.KEY_3):
            self.play_music(False, True, False)

        if pyxel.btnp(pyxel.KEY_4):
            self.play_music(False, False, True)

        if pyxel.btnp(pyxel.KEY_5):
            self.play_music(False, False, False)

    def draw(self):
        pyxel.cls(1)

        pyxel.text(6, 6, "sound(snd).set(note,tone,volume,effect,speed)", 7)


        for i in range(3):
            x = 140 + i * 16
            y = 123 + math.sin(pyxel.frame_count * 0.1 + i * 2.1) * 5
            pyxel.text(x, y + i * 6, 'ha', 2 + i)

        pyxel.pal()


App()
