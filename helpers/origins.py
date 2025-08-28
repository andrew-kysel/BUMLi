import bpy 
from mathutils import Vector

def reset_all(obj, context):
  _hierarchy_origin_to_geometry(obj, context)
  _snap_origins_to_lowest_z(obj)
    
  # Add 3D cursor to parents origin and align its children with it
  bpy.ops.view3d.snap_cursor_to_active()
  bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)

  _snap_children_to_cursor(obj, context)

  bpy.ops.view3d.snap_cursor_to_center()
  bpy.ops.object.select_all(action='DESELECT')
  obj.select_set(True)
  context.view_layer.objects.active = obj

def _hierarchy_origin_to_geometry(parent, context):
  hierarchy = {parent}
  hierarchy.update(parent.children_recursive)

  bpy.ops.object.select_all(action='DESELECT')

  for obj in hierarchy:
    obj.select_set(True)
  context.view_layer.objects.active = parent

  bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')       

def _snap_origins_to_lowest_z(parent):
  hierarchy = {parent}
  hierarchy.update(parent.children_recursive)

  # Find lowest Z coordinate of parent vertices
  lowest_z = min(
    (parent.matrix_world @ v.co).z for v in parent.data.vertices
  )

  for obj in hierarchy:
    world_origin = obj.matrix_world.translation
    target_point = Vector((world_origin.x, world_origin.y, lowest_z))

    # Find local offset
    local_offset = obj.matrix_world.inverted() @ target_point

    if (obj.type == 'MESH'):
      for vertex in obj.data.vertices:
        vertex.co -= local_offset

    # Move child origin to target point
    obj.location += obj.matrix_world.to_quaternion() @ local_offset 

def _snap_children_to_cursor(parent, context):
  children = parent.children_recursive
  for child in children:
    bpy.ops.object.select_all(action='DESELECT')

    child.select_set(True)
    context.view_layer.objects.active = child

    bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)       
