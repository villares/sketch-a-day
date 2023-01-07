
import collections
import shapely.geometry
from to_polygon import *

class PartialOrdering(object):
  class PoPoly(object):
    def __init__(self, contour, pid):
      self.pid            = pid
      self.parent         = None
      self.children       = set()
      self.descendent_idx = set()
      self.ancestor_idx   = set()
      self.ignored_idx    = set()
      self.sh_poly        = shapely.geometry.Polygon( to_polygon(contour) )

    def intersects(self, pop):
      return self.sh_poly.intersects(pop.sh_poly)

    def contains(self, pop):
      return self.sh_poly.contains(pop.sh_poly)

  def __init__(self, contours):
    self.polygons     = [ self.PoPoly(c,i) for i,c in enumerate(contours) ]
    self.construct()

  def construct(self):
    for i,pi in enumerate(self.polygons):
      for j,pj in enumerate(self.polygons[(i+1):], start=i+1):
        if not pi.intersects(pj):
          pi.ignored_idx.add(j)
          pj.ignored_idx.add(i)
          continue

        if pi.contains(pj):
          pi.descendent_idx.add(j)
          pj.ancestor_idx.add(i)
        elif pj.contains(pi):
          pj.descendent_idx.add(i)
          pi.ancestor_idx.add(j)
        else:
          raise NotImplementedError("polygons intersect but no proper subset relation exists")
    self.reduce()

  def reduce(self):
    polygon_idx = list(range(len(self.polygons)))

    while any(polygon_idx):
      for i in polygon_idx:
        if i is None:
          continue
        pi  = self.polygons[i]
        dmi = pi.descendent_idx - pi.ignored_idx
        if len(dmi) == 0:
          polygon_idx[i]  = None

          for j in pi.ancestor_idx:
            self.polygons[j].ignored_idx.add(i)

          for j in pi.descendent_idx:              
            pj        = self.polygons[j]
            if pj.parent is not None:
              continue

            pj.parent = pi
            self.polygons[i].children.add( pj )

  def roots(self):
    return [p for p in self.polygons if p.parent is None]

  def bfs(self):
    for r in self.roots():
      q = collections.deque()
      q.append(r)
      while len(q) > 0:
        n = q.popleft()
        yield (n.pid, n.sh_poly.exterior)
        for c in n.children:
          q.append(c)

  def debug(self):
    for i,pi in enumerate(self.polygons):
      print("\n\n")
      print("pid: {0}".format(pi.pid))
      if pi.parent is not None:
        print("\tparent-pid:     {0}".format(pi.parent.pid))
      for pj in pi.children:
        print("\tchild-pid:      {0}".format(pj.pid))
      for j in pi.ancestor_idx:
        print("\tancestor:       {0}".format(j))
      for j in pi.descendent_idx:
        if j in pi.ignored_idx:
          print("\tdescendent:     {0}*".format(j))
        else:
          print("\tdescendent:     {0}".format(j))
