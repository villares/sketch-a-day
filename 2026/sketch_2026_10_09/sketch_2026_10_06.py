"""
Getting data from https://s3.amazonaws.com/elevation-tiles-prod/
«The Mapzen terrain tiles provide basemap terrain coverage
of the world in a raster tile format.»

Visualizing the geotiff with py5
"""

from pathlib import Path

import mercantile
import rasterio
import requests
from rasterio.merge import merge
import py5
import numpy as np
import matplotlib

demgtf = "sp_dem.tif"

def setup():
    py5.size(1165, 1589)
    build_dem(-46.75, -23.70, -46.55, -23.45, zoom=12, out_path=demgtf)
    with rasterio.open(demgtf) as src:
        elev = src.read(1).astype(np.float64)
        nodata = src.nodata
    # guard against zeros and outliers    
    mask = np.zeros(elev.shape, dtype=bool)
    if nodata is not None:
        mask = elev == nodata
    mask |= ~np.isfinite(elev)
    valid = elev[~mask]
    lo, hi = np.percentile(valid, [0, 99])
    norm = np.clip((elev - lo) / (hi - lo), 0, 1)

    rgba = matplotlib.colormaps["viridis"](norm)
    rgba[mask] = [0, 0, 0, 0]   
    rgba = (rgba * 255).astype(np.uint8)
    h, w = rgba.shape[:2]
    img = py5.create_image_from_numpy(rgba, "RGBA")
    print(img.width, img.height, w, h)
    py5.image(img, 0, 0)
    py5.save('out.png')

def download_tiles(west, south, east, north, zoom, cache_dir="tiles"):
    URL = "https://s3.amazonaws.com/elevation-tiles-prod/geotiff/{z}/{x}/{y}.tif"
    cache = Path(cache_dir)
    paths = []
    session = requests.Session()
    for t in mercantile.tiles(west, south, east, north, zoom):
        path = cache / str(t.z) / str(t.x) / f"{t.y}.tif"
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            r = session.get(URL.format(z=t.z, x=t.x, y=t.y), timeout=60)
            r.raise_for_status()
            path.write_bytes(r.content)
        paths.append(path)
    return paths


def build_dem(west, south, east, north, zoom, out_path="dem.tif"):
    paths = download_tiles(west, south, east, north, zoom)
    srcs = [rasterio.open(p) for p in paths]
    try:
        x0, y0 = mercantile.xy(west, south)
        x1, y1 = mercantile.xy(east, north)
        mosaic, transform = merge(srcs, bounds=(x0, y0, x1, y1))
        profile = srcs[0].profile  # carries crs, dtype, nodata, etc.
    finally:
        for s in srcs:
            s.close()

    profile.update(
        driver="GTiff", height=mosaic.shape[1], width=mosaic.shape[2],
        transform=transform, compress="deflate", tiled=True,
        blockxsize=256, blockysize=256,
    )
    with rasterio.open(out_path, "w", **profile) as f:
        f.write(mosaic)
    return out_path

py5.run_sketch(block=False)