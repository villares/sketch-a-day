from matplotlib.path import Path
from enum import Enum
import fontforge

_State = Enum('_State', 'INIT START Q C I')

class ShapeError(Exception):
  pass

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

# ----

def _segment_linear(curve, verts, codes):
  _verts = [(p.x, p.y) for p in curve]
  if len(_verts) == 2:
    _codes = [Path.MOVETO, Path.LINETO]
  else:
    raise ValueError("_segment_linear")

  codes.extend( _codes )
  verts.extend( _verts )  
  curve[:] = curve[-1:]

# ----

def _segment_quadratic(curve, verts, codes):
  _verts = [(p.x, p.y) for p in curve]
  if len(_verts) == 3:
    _codes = [Path.MOVETO, Path.CURVE3, Path.CURVE3]
  else:
    raise ValueError("_segment_quadratic")

  codes.extend( _codes )
  verts.extend( _verts )  
  curve[:] = curve[-1:]

# ---- 

def _segment_interpolate(curve, verts, codes):
  a,b,c = curve
  mbc   = fontforge.point((b.x+c.x)/2., (b.y+c.y)/2., 1)
  _segment_quadratic([a,b,mbc], verts, codes)
  curve[:] = [mbc,c]

# ---- 

def _segment_cubic(curve, verts, codes):
  raise NotImplementedError("review this function before using")
  _verts = [(p.x, p.y) for p in curve]
  if len(_verts) == 4:
    _codes = [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4]
  else:
    raise ValueError("_segment_cubic")

  codes.extend( _codes )
  verts.extend( _verts )  


# ---- 

def to_polygon(contour):
  verts,codes = _verts_codes(contour)

  # Remove MOVETO codes for all but the first point
  cs = []
  vs = []
  for i,(c,v) in enumerate(zip(codes,verts)):
    if i == 0:
      cs.append(c)
      vs.append(v)
    elif c != Path.MOVETO:
      cs.append(c)
      vs.append(v)

  pgon = Path(vs,cs).to_polygons()

  if len(pgon) > 1:
    raise NotImplementedError("not expecting multiple polygons")

  return pgon[0]

# ---- 

def _verts_codes(contour):
  if contour.closed == 0 or contour.isEmpty():
    raise ValueError("contour must be closed and non-empty")

  first_pt_on_curve = None
  for i,pt in enumerate(contour):
    if pt.on_curve == 1:
      first_pt_on_curve = i
      break

  if first_pt_on_curve is None:
    raise NotImplementedError("handle the quadratic-only, all-interpolated case")

  pts = list(contour)
  if first_pt_on_curve > 0:
    pts = pts[i:] + pts[:i]
  pts.append(pts[0])

  if contour.is_quadratic:
    verts,codes = _quadratic_verts_codes(pts)
  else:
#    verts,codes = _quadratic_verts_codes(pts)
    raise NotImplementedError("handle the non-quadratic / cubic spline case")

  return (verts, codes)

# ---- 

def _quadratic_verts_codes(pts):
  """
  Extract the components of a matplotlib.Path from a list of (x,y) coordinates.
  """
  curve = []
  codes = []
  verts = []

  state = _State.INIT  
  for i,pt in enumerate(pts):
    curve.append( pt )
    if state == _State.INIT:
      if pt.on_curve:
        state = _State.START
      else:
        raise ShapeError("contour should start with a point on the curve")
    elif state == _State.START:
      if pt.on_curve:
        _segment_linear(curve, verts, codes)
        state = _State.START
      else:
        state = _State.Q
    elif state == _State.Q:
      if pt.on_curve:
        _segment_quadratic(curve, verts, codes)
        state = _State.START
      else:
        _segment_interpolate(curve, verts, codes)
        state = _State.Q

  return (verts, codes)
