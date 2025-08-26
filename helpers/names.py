import re

def rename_hierarchy(parent):
  if parent.name.startswith("SM_"):
    parent_name = parent.name
  else:
    parent_name = f"SM_{_strip_suffix(parent.name)}"
    parent.name = parent_name

  children = list(parent.children_recursive)
    
  if len(children) == 1:
    child = children[0]

    if _is_box(child):
      child.name = f"UBX_{parent_name}"
    else:    
      child.name = f"UCX_{parent_name}"

  elif len(children) > 1:
    # Add UBX_ with numbering in case there're multiple children
    for idx, child in enumerate(children, start=1):
      child.name = f"UBX_{parent_name}_{idx:02d}"

def _strip_suffix(name):
    """Remove Blender's .001, .002 suffixes."""
    return re.sub(r'\.\d+$', '', name)

def _is_box(obj, ndigits=6):
  """True if mesh is exactly a rectangular box (8 unique corner verts only)."""
  if not obj or obj.type != 'MESH':
    return False

  # unique vertex positions in *local* space (tolerant rounding)
  pts = {(round(v.co.x, ndigits), round(v.co.y, ndigits), round(v.co.z, ndigits))
    for v in obj.data.vertices}

  if len(pts) != 8:
    return False  # extra verts (e.g., two joined boxes) or not enough

  xs = {p[0] for p in pts}; ys = {p[1] for p in pts}; zs = {p[2] for p in pts}
  if not (len(xs) == len(ys) == len(zs) == 2):
    return False  # not exactly two distinct coords per axis

  # ensure extents are non-zero
  if min(xs) == max(xs) or min(ys) == max(ys) or min(zs) == max(zs):
    return False

  # corners must be exactly the Cartesian product of the two values per axis
  expected = {(x, y, z) for x in xs for y in ys for z in zs}
  return pts == expected
