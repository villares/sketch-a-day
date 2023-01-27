
M = 15
rs = 1

def setup():
    size(800, 800)

def draw():
    background(250, 250, 240)
    random_seed(rs)
    margin = M * 3
    interrupt = 0
    vertical_match = -1
    for y in range(margin, height - margin, M):
        for x in range(margin, width - margin, M):
            with push_matrix():
                translate(x, y)
                VM = vertical_match == x
                if VM: circle(0, 0, 5)
                if random(abs(15 - interrupt * 3)) < 1 or VM:
                     interrupt += 2
                elif interrupt >= 8:
                    interrupt = 0
                r = random(-PI * 0.30, PI * 0.30)
                rotate(r)
                if interrupt <= 4 or abs(r) > PI * 0.25:
                    line(0,-M, 0, +M)
                else:
                    vertical_match = x

                    
def key_pressed():
    global rs
    rs += 1
