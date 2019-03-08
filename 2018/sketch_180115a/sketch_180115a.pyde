"""
s18015 - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day

Converting some of Maeda's Design by Number
dbnletters.dbn code -> Processing
"""

dbn_command = {} # Dict of functions

dbn_A = """
line h v h (v+7)
line (h) (v+7) (h+3) (v+10)
line (h+3) (v+10) (h+10) (v+3)
line (h+10) (v+3) (h+10) v
line h (v+3) (h+10) (v+3)
""".split("\n")

dbn_B = """
line h v h (v+10)
line h (v+10) (h+5) (v+10)
line (h+5) (v+10) (h+8) (v+7)
line h (v+6) (h+7) (v+6)
line (h+7) (v+6) (h+10) (v+3)
line (h+10) (v+3) (h+10) (v+1)
line h v (h+9) v
""".split("\n")

dbn_C = """
line (h+4) v (h+10) v
line (h+4) v h (v+4)
line h (v+4) h (v+9)
line (h+1) (v+10) (h+9) (v+10)
""".split("\n")

def setup():
    size(200, 200)
    strokeCap(SQUARE)
    noSmooth()
    parse_dbn(dbn_A, "A")
    parse_dbn(dbn_B, "B")
    parse_dbn(dbn_C, "C")

def draw():
    scale(2, -2)
    translate(0, -100)
    dbn_command["A"](10, 10)
    dbn_command["B"](25, 10)
    dbn_letterC(40, 10)


def parse_dbn(dbn_block, func_key):
    p_block = []
    for dbn_line in dbn_block:
        if dbn_line:
            p_block.append(dbn_line
                       .replace("line ", "line(")
                       .replace(" ", ",")
                       + ")")
    def func(h, v):
        for l in p_block: eval(l)
        
    dbn_command[func_key] = func
    globals()["dbn_letter"+func_key]= func