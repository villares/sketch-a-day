"""
['ACCENT', 'ACCENT_R', 'AFMHOT', 'AFMHOT_R', 'AUTUMN', 'AUTUMN_R', 'BINARY', 'BINARY_R',
'BLUES', 'BLUES_R', 'BONE', 'BONE_R', 'BRBG', 'BRBG_R', 'BRG', 'BRG_R', 'BUGN', 'BUGN_R',
'BUPU', 'BUPU_R', 'BWR', 'BWR_R', 'CIVIDIS', 'CIVIDIS_R', 'CMRMAP', 'CMRMAP_R', 'COOL',
'COOLWARM', 'COOLWARM_R', 'COOL_R', 'COPPER', 'COPPER_R', 'CUBEHELIX', 'CUBEHELIX_R',
'DARK2', 'DARK2_R', 'FLAG', 'FLAG_R', 'GIST_EARTH', 'GIST_EARTH_R', 'GIST_GRAY', 'GIST_GRAY_R',
'GIST_GREY', 'GIST_HEAT', 'GIST_HEAT_R', 'GIST_NCAR', 'GIST_NCAR_R', 'GIST_RAINBOW',
'GIST_RAINBOW_R', 'GIST_STERN', 'GIST_STERN_R', 'GIST_YARG', 'GIST_YARG_R', 'GIST_YERG',
'GNBU', 'GNBU_R', 'GNUPLOT', 'GNUPLOT2', 'GNUPLOT2_R', 'GNUPLOT_R', 'GRAY', 'GRAYS', 'GRAY_R',
'GREENS', 'GREENS_R', 'GREY', 'GREYS', 'GREYS_R', 'HOT', 'HOT_R', 'HSV', 'HSV_R', 'INFERNO',
'INFERNO_R', 'JET', 'JET_R', 'MAGMA', 'MAGMA_R', 'NIPY_SPECTRAL', 'NIPY_SPECTRAL_R',
'OCEAN', 'OCEAN_R', 'ORANGES', 'ORANGES_R', 'ORRD', 'ORRD_R', 'PAIRED', 'PAIRED_R',
'PASTEL1', 'PASTEL1_R', 'PASTEL2', 'PASTEL2_R', 'PINK', 'PINK_R', 'PIYG', 'PIYG_R', 'PLASMA',
'PLASMA_R', 'PRGN', 'PRGN_R', 'PRISM', 'PRISM_R', 'PUBU', 'PUBUGN', 'PUBUGN_R', 'PUBU_R',
'PUOR', 'PUOR_R', 'PURD', 'PURD_R', 'PURPLES', 'PURPLES_R', 'RAINBOW', 'RAINBOW_R', 'RDBU',
'RDBU_R', 'RDGY', 'RDGY_R', 'RDPU', 'RDPU_R', 'RDYLBU', 'RDYLBU_R', 'RDYLGN', 'RDYLGN_R',
'REDS', 'REDS_R', 'SEISMIC', 'SEISMIC_R', 'SET1', 'SET1_R', 'SET2', 'SET2_R', 'SET3', 'SET3_R',
'SPECTRAL', 'SPECTRAL_R', 'SPRING', 'SPRING_R', 'SUMMER', 'SUMMER_R', 'TAB10', 'TAB10_R',
'TAB20', 'TAB20B', 'TAB20B_R', 'TAB20C', 'TAB20C_R', 'TAB20_R', 'TERRAIN', 'TERRAIN_R',
'TURBO', 'TURBO_R', 'TWILIGHT', 'TWILIGHT_R', 'TWILIGHT_SHIFTED', 'TWILIGHT_SHIFTED_R',
'VIRIDIS', 'VIRIDIS_R', 'WINTER', 'WINTER_R', 'WISTIA', 'WISTIA_R',
'YLGN', 'YLGNBU', 'YLGNBU_R', 'YLGN_R', 'YLORBR', 'YLORBR_R', 'YLORRD', 'YLORRD_R']
"""


import py5
from py5 import sqrt, sin, cos, PI, TAU, HALF_PI

def setup():
    py5.size(600, 600)
    py5.color_mode(py5.CMAP, py5.mpl_cmaps.VIRIDIS, 6)
    py5.no_stroke()
    
def draw():
    py5.background('black')
    w = 50
    for x in range(11):
        for y in range(11):
            unit(w + x * w,
                 w + y * w, w)
        
def unit(x, y, w):
    # w = r * 2 + r * 2 / (1 + sqrt(2))
    r = w / (2 * sqrt(2))  # octagon inradius
    s = r * 2 / (1 + sqrt(2)) # sq side
    # squ(x, y, w)  # visual debug
    #py5.random_seed(int(x))
    offset = - r * sqrt(2) / 2
    rot = (y / w / 2) % 4 #py5.random_choice((0, 1, 2, 3))
    oct(x + offset, y + offset, r, rot)
    squ(x + r + s / 2 + offset, y + offset, s)
    oct(x + w / 2 + offset, y + w / 2 + offset, r, rot)
    squ(x - r - s / 2 + w / 2 + offset, y + w / 2 + offset, s)
    # py5.circle(x, y, 5)  # visual debug
    
def squ(x, y, s):
    py5.quad(
        x - s / 2, y - s / 2,
        x + s / 2, y - s / 2,
        x + s / 2, y + s / 2,
        x - s / 2, y + s / 2
    )

def oct(x, y, r, rot):
    s = r * 2 / (1 + sqrt(2)) # square side
    R = r / cos(PI / 8) # circumradius
    ang = TAU / 8
    vs = [(cos(i * ang + ang / 2) * R,
           sin(i * ang + ang / 2) * R)
           for i in range(8)]
    with py5.push_matrix():
        py5.translate(x, y)
        py5.rotate(rot * HALF_PI)
        x0, y0 = vs[0]    
        x2, y2 = vs[2]
        x7, y7 = vs[7]
        with py5.begin_closed_shape(py5.QUAD):
            py5.fill((x / 2) % 6)
            py5.vertices((vs[0], vs[1], vs[2], (x0-s, y0)))
            py5.fill((x / 2 + 1) % 6)
            py5.vertices((vs[0], (x0-s, y0), (x7-s, y7), vs[7]))
            py5.fill((x / 2+ 2) % 6)
            py5.vertices((vs[7], (x7-s, y7), vs[5], vs[6]))
            py5.fill((x / 2 + 3) % 6)
            py5.vertices((vs[2], vs[3], vs[4], (x2, y2-s)))
            py5.fill((x / 2 + 4) % 6)
            py5.vertices(((x2, y2-s), vs[4],vs[5], (x7-s, y7)))
            py5.fill((x / 2 + 5) % 6)
            py5.vertices(((x2, y2-s), (x7-s, y7), (x0-s, y0), vs[2]))
       

def key_pressed():
    if py5.key == 's':
        save_snapshot_and_code()
    
def save_snapshot_and_code():
    import shutil
    import datetime
    p = py5.sketch_path()
    stamp = str(datetime.datetime.now()).replace(' ', '-').replace(':', '').replace('.', '')    
    py5.save(p / stamp / (stamp + '.png')) 
    shutil.copyfile(__file__, p / stamp / (stamp + '.py'))
    #py5.save(stamp + '.png')

py5.run_sketch()