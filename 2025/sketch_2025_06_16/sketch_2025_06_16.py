from itertools import product

from shapely.geometry import LineString, LinearRing
import py5
from py5_tools import animated_gif

MARGIN = 64
SPACING = 128 + 64
seed = 10

def setup():
    global grid
    py5.size(512, 512, py5.P3D)
    grid = list(product(range(MARGIN, py5.width, SPACING), repeat=2))
    make_polys()
    py5.hint(py5.ENABLE_STROKE_PERSPECTIVE)
    animated_gif(f'{seed}.gif', duration=0.1, frame_numbers=range(1, 361, 5))
    
def make_polys():
    global poly_a, poly_b
    py5.random_seed(seed)
    poly_a = make_simple_poly(grid)
    poly_b = make_simple_poly(grid)
    
def make_simple_poly(grid, grid_pts= 5):
    simple = False
    while not simple:
        poly = LineString(py5.random_sample(grid, grid_pts)).buffer(32).exterior
        simple = poly.is_simple
    return poly
    
def draw():
    py5.background(200)
    py5.translate(256, 256, -256)
    py5.rotate_y(py5.radians(py5.frame_count))
    py5.translate(-256, -256)
    py5.stroke_weight(5)
    #py5.stroke(0, 0, 200)
    #py5.points(grid)
    py5.stroke(255)
    Z_OFFSET = 256
    with py5.push_matrix():
        py5.translate(0, 0, -Z_OFFSET)
        py5.shape(poly_a)
        py5.translate(0, 0, Z_OFFSET * 2)
        py5.shape(poly_b)
    
    py5.stroke(0)
    py5.stroke_weight(1)
    points_a = get_poly_points(poly_a, 100)
    points_b = get_poly_points(poly_b, 100)
    py5.lines((xa, ya, -Z_OFFSET, xb, yb, Z_OFFSET) for (xa, ya), (xb, yb)
              in zip(points_a, points_b))
    
def get_poly_points(poly, num = 100):
    d = poly.length / (num - 1)
    return [(p.x, p.y) for p in
            (poly.interpolate(i * d)
             for i in range(num))]

# from typing import Sequence
# def lerp_sequence(a: Sequence, b: Sequence, t: float) -> Sequence:
#     return tuple(lerp_sequence(ca, cb, t) if isinstance(ca, Sequence)
#                  else py5.lerp(ca, cb, t)             
#                  for ca, cb in zip(a, b))

def key_pressed():
    global seed
    py5.save_frame('###.png')
    seed += 1
    make_polys()

    

py5.run_sketch(block=False)

"""
hint(which: 'int', /) -> 'None'
    This function is used to enable or disable special features that control how
    graphics are drawn.
    
    Underlying Processing method: PApplet.hint
    
    Parameters
    ----------
    
    which: int
        hint to use when rendering Sketch
    
    Notes
    -----
    
    This function is used to enable or disable special features that control how
    graphics are drawn. In the course of developing Processing, the developers had
    to make hard decisions about tradeoffs between performance and visual quality.
    They put significant effort into determining what makes most sense for the
    largest number of users, and then use functions like `hint()` to allow people to
    tune the settings for their particular Sketch. Implementing a `hint()` is a last
    resort that's used when a more elegant solution cannot be found. Some options
    might graduate to standard features instead of hints over time, or be added and
    removed between (major) releases.
    
    Hints used by the Default Renderer
    ----------------------------------
    
    * `ENABLE_STROKE_PURE`: Fixes a problem with shapes that have a stroke and are
    rendered using small steps (for instance, using `vertex()` with points that are
    close to one another), or are drawn at small sizes.
    
    Hints for use with `P2D` and `P3D`
    --------------------------------------
    
    * `DISABLE_OPENGL_ERRORS`: Speeds up the `P3D` renderer setting by not checking
    for errors while running.
    * `DISABLE_TEXTURE_MIPMAPS`: Disable generation of texture mipmaps in `P2D` or
    `P3D`. This results in lower quality - but faster - rendering of texture images
    when they appear smaller than their native resolutions (the mipmaps are scaled-
    down versions of a texture that make it look better when drawing it at a small
    size). However, the difference in performance is fairly minor on recent desktop
    video cards.
    
    
    Hints for use with `P3D` only
    -------------------------------
    
    * `DISABLE_DEPTH_MASK`: Disables writing into the depth buffer. This means that
    a shape drawn with this hint can be hidden by another shape drawn later,
    irrespective of their distances to the camera. Note that this is different from
    disabling the depth test. The depth test is still applied, as long as the
    `DISABLE_DEPTH_TEST` hint is not called, but the depth values of the objects are
    not recorded. This is useful when drawing a semi-transparent 3D object without
    depth sorting, in order to avoid visual glitches due the faces of the object
    being at different distances from the camera, but still having the object
    properly occluded by the rest of the objects in the scene.
    * `ENABLE_DEPTH_SORT`: Enable primitive z-sorting of triangles and lines in
    `P3D`. This can slow performance considerably, and the algorithm is not yet
    perfect.
    * `DISABLE_DEPTH_TEST`: Disable the zbuffer, allowing you to draw on top of
    everything at will. When depth testing is disabled, items will be drawn to the
    screen sequentially, like a painting. This hint is most often used to draw in
    3D, then draw in 2D on top of it (for instance, to draw GUI controls in 2D on
    top of a 3D interface). When called, this will also clear the depth buffer.
    Restore the default with `hint(ENABLE_DEPTH_TEST)`, but note that with the depth
    buffer cleared, any 3D drawing that happens later in will ignore existing shapes
    on the screen.
    * `DISABLE_OPTIMIZED_STROKE`: Forces the `P3D` renderer to draw each shape
    (including its strokes) separately, instead of batching them into larger groups
    for better performance. One consequence of this is that 2D items drawn with
    `P3D` are correctly stacked on the screen, depending on the order in which they
    were drawn. Otherwise, glitches such as the stroke lines being drawn on top of
    the interior of all the shapes will occur. However, this hint can make rendering
    substantially slower, so it is recommended to use it only when drawing a small
    amount of shapes. For drawing two-dimensional scenes, use the `P2D` renderer
    instead, which doesn't need the hint to properly stack shapes and their strokes.
    * `ENABLE_STROKE_PERSPECTIVE`: Enables stroke geometry (lines and points) to be
    affected by the perspective, meaning that they will look smaller as they move
    away from the camera.

"""

