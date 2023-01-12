import math
from random import shuffle
import pyxel

notes1 = "a1 b1 c1 d1 e1 f1 g1 r a2 b2 c2 d2 e2 f2 g2 r a1 b1 c1 d1 r"
bag = notes1.split(' ')
shuffle(bag)
notes1 = ' '.join(bag)

notes2 = "a2 b2 c2 d2 e2 f2 g2 r a2 b2 c2 d2 e2 f2 g2 r d2 c2 b2 a2 r"
bag = notes2.split(' ')
shuffle(bag)
notes2 = ' '.join(bag)


class App:
    def __init__(self):
        pyxel.init(300, 50)

        pyxel.sound(0).set(
            notes1,
            "p",
            "6",
            "nnnn nnn nnnn nnn nnnn",
            25,
        )

        pyxel.sound(1).set(
            notes2,
            "s",
            "6",
            "nnvv nnn nnvv nnn vvvv",
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
            "f0ra4r f0ra4r f0ra4r f0f0a4r", "t", "6622 6622 6622 6422", "f", 25
        )

        self.play_music(True, True, True)

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
            
#         if pyxel.btnp(pyxel.KEY_6):
#             notes = "a2b2c2d2 e2f2g2r a2b2c2d2 e2f2g2r d2c2b2a2r"
#             notes = "a2"
#             pyxel.sound(1).set(
#             notes,
#             "s",
#             "6",
#             "nnvv nnn nnvv nnn vvvv",
#             25,
#         )
# 
#             pyxel.sound(2).set(
#             notes,
#             "t",
#             "7",
#             "n",
#             25,
#         )
            

    def draw(self):
        pyxel.cls(1)

        pyxel.text(6, 6, notes1, 7)
        pyxel.text(6, 14, notes2, 8)


        for i in range(3):
            x = 40 + i * 16
            y = 25 + math.sin(pyxel.frame_count * 0.1 + i * 2.1) * 5
            pyxel.text(x, y + i * 6, 'ha', 2 + i)

        pyxel.pal()


App()
