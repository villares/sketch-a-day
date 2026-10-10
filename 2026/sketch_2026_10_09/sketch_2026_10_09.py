import numpy as np
import rasterio
from shapely.geometry import LineString, Polygon
from shapely import affinity
from skimage import measure
import py5
from PIL import Image

H = 800

def contours_from_dem(dem_path, interval=50):
    """Extract contours from a GeoTIFF DEM."""
    with rasterio.open(dem_path) as src:
        z = src.read(1)
        T = src.transform
        bounds = src.bounds
    z = np.where(np.isnan(z), np.nanmin(z), z)
    results = []
    levels = np.arange(np.floor(z.min() / interval) * interval,
                       z.max() + interval, interval)
    for level in levels:
        for c in measure.find_contours(z, level):
            if len(c) < 3:
                continue 
            rows, cols = c[:, 0], c[:, 1]
            xs, ys = T * (cols + 0.5, rows + 0.5)
            results.append((float(level), LineString(zip(xs, ys))))
    return results, bounds, z

   
def setup():
    py5.size(586, H)
    py5.background('k')
    py5.color_mode(py5.CMAP, 'terrain', 255)

    shps, bounds, dem_data = contours_from_dem("sp_dem.tif", interval=10)
    print(f"contour lines: {len(shps)}")
    
    all_bounds = [ls.bounds for level, ls in shps]
    x_min_actual = min(b[0] for b in all_bounds)
    y_min_actual = min(b[1] for b in all_bounds)
    x_max_actual = max(b[2] for b in all_bounds)
    y_max_actual = max(b[3] for b in all_bounds)
    
    x_range = x_max_actual - x_min_actual
    y_range = y_max_actual - y_min_actual
    aspect_ratio = x_range / y_range    
    s = H / y_range
    canvas_width = int(s * x_range)
    canvas_height = H

    transformed_shps = []
    for level, ls in shps:
        # Translate to origin, then scale (with Y flip)
        ls_tx = affinity.translate(ls, -x_min_actual, -y_max_actual)
        ls_scaled = affinity.scale(ls_tx, xfact=s, yfact=-s, origin=(0, 0))
        poly = Polygon(ls_scaled.coords)
        transformed_shps.append((float(level), poly))
    
    transformed_shps.sort(key=lambda item: item[0])
    levels = [level for level, _ in transformed_shps]
    level_min, level_max = min(levels), max(levels)
    print(f"elevation range: {level_min} - {level_max}")

    py5.stroke_weight(0.5)
    py5.stroke('gray')
    py5.no_fill()
    for level, ls in transformed_shps:
        gray = py5.remap(level, level_min, level_max, 25, 255)
        py5.fill(int(gray))
        py5.shape(ls)
    
    py5.no_loop()
    py5.save_frame('out.png')

py5.run_sketch()
