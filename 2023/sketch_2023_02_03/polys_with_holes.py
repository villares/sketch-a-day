from shapely import Polygon

# https://stackoverflow.com/questions/59106740/substracting-inner-rings-from-a-list-of-polygons
from rtree.index import Index # you need to install rtree

def process_polys(polygons):
    # create an rtree for efficient spatial queries
    rtree = Index((i, p.bounds, None) for i, p in enumerate(polygons))
    results = []
    for i, this_poly in enumerate(polygons):
        # loop over indices of approximately intersecting polygons
        for j in rtree.intersection(this_poly.bounds):
            # ignore the intersection of this polygon with itself
            if i == j:
                continue
            other_poly = polygons[j]
            # ensure the polygon fully contains our match
            if this_poly.contains(other_poly):
                result = this_poly.difference(other_poly)
                results.append(donut)
                break  # quit searching
    return results