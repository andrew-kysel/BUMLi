import bpy
from ..helpers.utils import toggle_display_type

class MESH_OT_collider_toggle(bpy.types.Operator):
  bl_idname = "mesh.colliders_to_wire"
  bl_label = "Set colliders to wire"
  bl_description = "Changes collider (child with name prefix UCX_ or UBX_) display type to Wire or Textured"
  bl_options = {"REGISTER", "UNDO"}

  def execute(self, context):
    selected = bpy.context.object

    if not selected.children or not any(child.name.startswith(("UBX", "UCX")) for child in selected.children):
      self.report({'WARNING'}, f"Mesh '{selected.name}' does not have proper collider")
    else:
      toggle_display_type(selected.children)

    return {"FINISHED"}   
