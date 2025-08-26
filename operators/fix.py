import bpy
from ..helpers import names, origins, utils 

class MESH_OT_fix(bpy.types.Operator):
  bl_idname = "mesh.fix"
  bl_label = "Fix mesh"
  bl_description = "Apply changes to the mesh according to selected rules"
  bl_options = {"REGISTER", "UNDO"}
    
  def execute(self, context):
    scene = context.scene
    selected = bpy.context.active_object

    if len(selected.children) > 1:
      self.report({'WARNING'}, f"Mesh '{selected.name}' has more than 1 child. Collision naming may be broken")
    
    if (scene.should_duplicate):
      selected = utils.duplicate_hierarchy(selected)

    if (scene.should_rename):
      names.rename_hierarchy(selected)

    if (scene.should_recalculate_normals):
      utils.recalculate_normals(selected)
        
    if (scene.should_apply_modifiers):
      utils.apply_modifiers(selected)
    
    if (scene.should_apply_scale):
      utils.apply_scale(selected)
    
    if (scene.should_reset_origin):
      origins.reset_all(selected)
    
    if (scene.should_place_to_world_origin):
      utils.place_to_world_origin(selected)

    if (scene.should_clear_materials):
      selected = utils.remove_materials(selected)
    
    return {"FINISHED"}
