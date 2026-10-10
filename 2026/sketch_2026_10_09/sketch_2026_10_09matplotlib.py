import numpy as np
import rasterio
from shapely.geometry import LineString, GeometryCollection
from skimage import measure
import matplotlib.pyplot as plt

# check sketch_2026_10_06.py to download the geotiff!
with rasterio.open("sp_dem.tif") as src:
    print(src.profile)
    print("bounds:", src.bounds)
    print("crs:", src.crs, "| size:", src.width, "x", src.height)
    z = src.read(1)
    b = src.bounds

def contours_from_dem(dem_path, interval=10):
    with rasterio.open(dem_path) as src:
        z = src.read(1)
        T = src.transform
    z = np.where(np.isnan(z), np.nanmin(z), z)  # find_contours dislikes NaN
    results = []  # list of (elevation, LineString)
    levels = np.arange(np.floor(z.min() / interval) * interval,
                       z.max() + interval, interval)
    for level in levels:
        for c in measure.find_contours(z, level):
            if len(c) < 2:
                continue
            rows, cols = c[:, 0], c[:, 1]
            # +0.5 shifts from pixel corner to pixel center
            xs, ys = T * (cols + 0.5, rows + 0.5)
            results.append((float(level), LineString(zip(xs, ys))))
    return results

shps = contours_from_dem("sp_dem.tif", interval=10)
print("number of contour lines:", len(shps))

fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(z, extent=(b.left, b.right, b.bottom, b.top), cmap="terrain", alpha=0.6)
for level, ls in shps:
    x, y = ls.xy
    ax.plot(x, y, lw=0.4, color="k")
plt.show()
