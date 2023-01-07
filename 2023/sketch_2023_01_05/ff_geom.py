import matplotlib.pyplot as plt
import matplotlib
import numpy as np

plt.ion()

def _expand_bounds(x0,x1):
  r = 0.05*(x1 - x0)
  x0 = x0 - r
  x1 = x1 + r
  return (x0,x1)

def setup_figure(glyph, figname='glyph'):
  bb      = glyph.boundingBox()
  fig     = plt.figure(figname)
  fig.clf()
  ax = fig.gca()
  xlim = _expand_bounds(*bb[::2])
  ylim = _expand_bounds(*bb[1::2])
  ax.set_xlim(xlim)
  ax.set_ylim(ylim)
  ax.set_aspect(1.)
  ax.set_title(glyph.codepoint)
  return ax

def point_collection(ax, points, **kwargs):
  import  matplotlib.markers      as mmarkers
  import  matplotlib.transforms   as mtransforms
  from    matplotlib.collections  import PathCollection

  marker      = matplotlib.rcParams['scatter.marker']
  marker_obj  = mmarkers.MarkerStyle(marker)
  path        = marker_obj.get_path().transformed( marker_obj.get_transform() )  
  offsets     = np.array(points)
  
  s           = matplotlib.rcParams['lines.markersize'] ** 2.0
  scales      = np.ma.ravel(s)

  collection  = PathCollection(
    (path,), 
    scales,
    transOffset = ax.transData,
    offsets     = offsets
  )
  collection.set_transform( mtransforms.IdentityTransform() )
  collection.update(kwargs)

  return collection


if __name__ == '__main__':

  import fontforge

  import numpy as np
  import matplotlib.patches     as patches
  from matplotlib.colors        import hex2color

  from ff_geom import *
  from partial_ordering import PartialOrdering

  blue    = hex2color("#1f77b4")
  orange  = hex2color("#ff7f0e")
  green   = hex2color("#2ca02c")
  gray    = hex2color("#D3D3D3")

  Fa  = fontforge.open('Inconsolata-ExtraBold.ttf')
  for k in ['A', 'a', 'W']:
    glyph       = Fa[k]
    contours    = glyph.layers['Fore']
    po          = PartialOrdering(contours)

    ax          = setup_figure(glyph,k)
    for pid,spe in po.bfs():
      if spe.is_ccw:
        # color = ax.get_facecolor()
        color         = ax.get_facecolor()
        on_pt_color   = ax.get_facecolor()
        off_pt_color  = green
      else:
        color         = blue
        on_pt_color   = blue
        off_pt_color  = orange

      patch_polygon = patches.Polygon( spe.coords, fc=color, ec='black', lw=0.5 )
      ax.add_patch(patch_polygon)

      on_curve_pts  = [(p.x,p.y) for p in contours[pid] if p.on_curve == True]
      if len(on_curve_pts) > 0:
        collection    = point_collection(ax, on_curve_pts, 
          facecolors  = on_pt_color, 
          edgecolors  = "black", 
          linewidth   = 0.5,
          zorder      = 2
        )
        ax.add_collection(collection)

      off_curve_pts = [(p.x,p.y) for p in contours[pid] if p.on_curve == False]
      if len(off_curve_pts) > 0:
        collection    = point_collection(ax, off_curve_pts, 
          facecolors  = off_pt_color, 
          edgecolors  = "black", 
          linewidth   = 0.5,
          zorder      = 2
        )
        ax.add_collection(collection)

    ax.figure.canvas.draw()
    filename = "{0}.png".format(k)    
    ax.figure.savefig(filename)


