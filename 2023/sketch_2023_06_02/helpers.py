def draw_shapely(shp):
    """Tries to draw a shapely object with py5."""
    from shapely import Polygon, MultiPolygon
    from shapely import LineString, MultiLineString
    from shapely import Point, MultiPoint
    from py5 import begin_closed_shape, begin_shape, begin_contour
    from py5 import  vertex, push_style, no_fill, point
    
    if isinstance(shp, (MultiPolygon, MultiLineString, MultiPoint)):
        for p in shp.geoms:
            draw_shapely(p)
    elif isinstance(shp, Polygon):
        with begin_closed_shape():
            for x, y in shp.exterior.coords:
                vertex(x, y)
            for hole in shp.interiors:
                with begin_contour():
                    for x, y in hole.coords:
                        vertex(x, y)
    elif isinstance(shp, LineString):
        with push_style():
            no_fill()
            with begin_shape():
                for x, y in shp.coords:
                    vertex(x, y)
    elif isinstance(shp, Point):
        point(*shp.coords[0])
    else:
        print(f"Unable to draw: {shp}")
        
def draw_circle_on_canvas_center():
    import py5
    s = py5.get_current_sketch()
    py5.circle(s.width / 2, s.height / 2, s.width / 20)