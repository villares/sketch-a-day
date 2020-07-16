# LerpVectorsSimplified
# 2019-04 Processing 3.4 - based on LerpVectorsExample by Jeremy Douglass
# 2020-07 ported to Python Mode by Alexandre Villares

vecs = []

def setup():
    size(200, 200)
    # mark path points
    vecs.append(PVector(10, 10))
    vecs.append(PVector(width - 10, 10))
    vecs.append(PVector(width - 10, height - 10))
    vecs.append(PVector(10, height - 10))
    vecs.append(PVector(width / 2, height / 2))
    fill(0, 0, 255)


def draw():
    background(255)
    time = millis() / 2 % 4000    # a clock that counts up to 4000 and starts over
    # from -1 to 1, then starts over
    sawtoothWave = map(time, 0, 3999, -1, 1)
    triangleWave = abs(sawtoothWave)    # bounces 0-1-0-1-0
    # find our location in 2D path based on 0-1
    loc = lerpVectors(triangleWave, vecs)
    ellipse(loc.x, loc.y, 20, 20)    # draw at the location


# based on an amount, find the location along a path made of points
def lerpVectors(amt, vecs):
    if len(vecs) == 1:
        return vecs[0]
    cunit = 1.0 / (len(vecs) - 1)
    return PVector.lerp(vecs[floor(amt / cunit)],
                        vecs[ceil(amt / cunit)],
                        amt % cunit / cunit)
