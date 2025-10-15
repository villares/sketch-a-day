# https://geopandas.org/en/stable/docs/user_guide/set_operations.html
# using >>> !py5-live-coding sketch_2025_10_13.py

import py5
import shapely
from shapely.geometry import Polygon
import geopandas
from geopandas import GeoDataFrame as GDF

polys1 = geopandas.GeoSeries([
    Polygon([(0,0), (2,0), (2,2), (0,2)]),
    Polygon([(2,2), (4,2), (4,4), (2,4)])
])

polys2 = geopandas.GeoSeries([
    Polygon([(1,1), (3,1), (3,3), (1,3)]),
    Polygon([(3,3), (5,3), (5,5), (3,5)])
])
df1 = GDF({'geometry': polys1, 'df1':[1,2]})
df2 = GDF({'geometry': polys2, 'df2':[1,2]})
res_symdiff = df1.overlay(df2, how='symmetric_difference')

def setup():
    py5.size(500, 500)
    py5.translate(50, 50)
    py5.scale(80)
    py5.stroke_weight(1/80)
    for s in res_symdiff.geometry:
        print(s)
        ps = py5.convert_shape(s)
        ps.disable_style()
        py5.fill(255, 200)
        py5.shape(ps)
    
py5.run_sketch()

