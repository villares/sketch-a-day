import py5
import shapely

def setup():
    py5.size(500, 500)
    py5.background(0)
    py5.translate(250, 250)
    py5.color_mode(py5.CMAP, py5.mpl_cmaps.VIRIDIS, 1)
    s = shapely.Polygon(
        ((-10, -10), (0, -5), (10, -10), (5, 0),
         (10, 10), (0, 5), (-10, 10), (-5, 0))
    )
    s = shapely.affinity.scale(s, 20, 20)
    s = s.buffer(30)
    base = s.area
    py5.no_stroke()
    py5.fill(0, 100)
    py5.shape(s)
    for _ in range(50):
        s = shapely.affinity.scale(s, 0.9, 0.9)
        s = shapely.affinity.rotate(s, 2)
        c = shapely.affinity.translate(
            s, #.buffer(10), #- s.buffer(5),
            py5.random_int(-250, 250), py5.random_int(-250, 250)
        )
        py5.fill(1 - c.area / base, 100)
        py5.shape(c)
        print(c.area)
    
py5.run_sketch(block=False)



"""
Help on method buffer in module shapely.geometry.base:

buffer(distance, quad_segs=16, cap_style='round', join_style='round', mitre_limit=5.0, single_sided=False, **kwargs) method of shapely.geometry.polygon.Polygon instance
    Get a geometry that represents all points within a distance
    of this geometry.
    
    A positive distance produces a dilation, a negative distance an
    erosion. A very small or zero distance may sometimes be used to
    "tidy" a polygon.
    
    Parameters
    ----------
    distance : float
        The distance to buffer around the object.
    resolution : int, optional
        The resolution of the buffer around each vertex of the
        object.
    quad_segs : int, optional
        Sets the number of line segments used to approximate an
        angle fillet.
    cap_style : shapely.BufferCapStyle or {'round', 'square', 'flat'}, default 'round'
        Specifies the shape of buffered line endings. BufferCapStyle.round ('round')
        results in circular line endings (see ``quad_segs``). Both BufferCapStyle.square
        ('square') and BufferCapStyle.flat ('flat') result in rectangular line endings,
        only BufferCapStyle.flat ('flat') will end at the original vertex,
        while BufferCapStyle.square ('square') involves adding the buffer width.
    join_style : shapely.BufferJoinStyle or {'round', 'mitre', 'bevel'}, default 'round'
        Specifies the shape of buffered line midpoints. BufferJoinStyle.ROUND ('round')
        results in rounded shapes. BufferJoinStyle.bevel ('bevel') results in a beveled
        edge that touches the original vertex. BufferJoinStyle.mitre ('mitre') results
        in a single vertex that is beveled depending on the ``mitre_limit`` parameter.
    mitre_limit : float, optional
        The mitre limit ratio is used for very sharp corners. The
        mitre ratio is the ratio of the distance from the corner to
        the end of the mitred offset corner. When two line segments
        meet at a sharp angle, a miter join will extend the original
        geometry. To prevent unreasonable geometry, the mitre limit
        allows controlling the maximum length of the join corner.
        Corners with a ratio which exceed the limit will be beveled.
    single_side : bool, optional
        The side used is determined by the sign of the buffer
        distance:
    
            a positive distance indicates the left-hand side
            a negative distance indicates the right-hand side
    
        The single-sided buffer of point geometries is the same as
        the regular buffer.  The End Cap Style for single-sided
        buffers is always ignored, and forced to the equivalent of
        CAP_FLAT.
    quadsegs : int, optional
        Deprecated alias for `quad_segs`.
    
    Returns
    -------
    Geometry
"""