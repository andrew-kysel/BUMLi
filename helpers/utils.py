from bpy import ops, context
from .names import _strip_suffix

def place_to_world_origin(obj):
  ops.object.select_all(action='DESELECT')

  obj.select_set(True)
  context.view_layer.objects.active = obj

  ops.object.rotation_clear(clear_delta=False)
  ops.object.location_clear(clear_delta=False)

def recalculate_normals(obj):
  ops.object.mode_set(mode='OBJECT')
  ops.object.select_all(action='DESELECT')

  obj.select_set(True)
  context.view_layer.objects.active = obj

  ops.object.mode_set(mode='EDIT')
  ops.mesh.select_all(action='SELECT')
  ops.mesh.normals_make_consistent(inside=False)
  ops.object.mode_set(mode='OBJECT')

def apply_modifiers(obj):
  context.view_layer.objects.active = obj
  ops.object.convert(target='MESH')

def apply_scale(obj):
  context.view_layer.objects.active = obj
  ops.object.transform_apply(location=False, rotation=False, scale=True)

def remove_materials(obj):
  obj.data.materials.clear()

def duplicate_hierarchy(parent):
  hierarchy = {parent}
  hierarchy.update(parent.children_recursive)

  ops.object.select_all(action='DESELECT')

  for obj in hierarchy:
    obj.select_set(True)
  context.view_layer.objects.active = parent

  ops.object.duplicate()
  duplicates = list(context.selected_objects)

  # Find duplicated parent by name. Quite dumb approach, but it works...
  for duplicate in duplicates:
    if _strip_suffix(duplicate.name) == _strip_suffix(parent.name):
      return duplicate

  return None

def toggle_display_type(colliders):
  for collider in colliders:
    if collider.type == 'MESH':
      if collider.display_type == 'TEXTURED':
        collider.display_type = 'WIRE'
      else:
        collider.display_type = 'TEXTURED'

# TODO: refactor these two methods, I think they are unnecessary complicated
def select_hierarchy():
  active_object = context.active_object

  ops.object.select_all(action='DESELECT')
  active_object.select_set(True)
  
  for obj in active_object.children:
    _select_children_recursive(obj)
  
  # Set the active object back to the original active object.
  context.view_layer.objects.active = active_object

def _select_children_recursive(parent):
  parent.select_set(True)

  for child in parent.children:
    _select_children_recursive(child)
