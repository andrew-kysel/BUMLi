import bpy
import os
from ..helpers import exports, utils

class MESH_OT_export(bpy.types.Operator):
  bl_idname = "mesh.export"
  bl_label = "Export mesh"
  bl_description = "Exports the mesh with its collider"
  bl_options = {'REGISTER', 'UNDO'}

  def execute(self, context):
    active = context.view_layer.objects.active   # safer than context.active_object
    selected = context.selected_objects

    if active is None or not selected:
      self.report({'ERROR'}, "No active object is selected")
      return {'CANCELLED'}

    if context.mode != 'OBJECT':
      bpy.ops.object.mode_set(mode='OBJECT')

    bpy.ops.object.select_all(action='DESELECT')
    utils.select_hierarchy()

    export_dir = getattr(context.scene, "export_directory", None)
    if not export_dir:
      self.report({'ERROR'}, "Export directory is not selected")
      return {'CANCELLED'}

    export_path = os.path.join(export_dir, f"{active.name}.fbx")
    os.makedirs(export_dir, exist_ok=True)  # check if folder exists

    exports.as_static_mesh(export_path)
    self.report({'INFO'}, f"Exported FBX to: {export_path}")

    return {'FINISHED'}
