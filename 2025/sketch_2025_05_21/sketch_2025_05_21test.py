from villares.geometry_helpers import hatch_poly

pts = [(100, 100), (300, 300), (400, 100), (300, 400), (150, 300)]

def setup():
    size(512, 512)
    color_mode(HSB)
     
def draw():
    background(240)
    ang = radians(frame_count * 10)
    hatch_poly(pts, ang, spacing=5)