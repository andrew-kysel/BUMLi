import bpy

bpy.types.Scene.export_directory = bpy.props.StringProperty(
  name="Export Folder",
  description="Directory for exporting meshes",
  subtype='DIR_PATH'
)

class VIEW3D_PT_linter_panel(bpy.types.Panel):
  bl_space_type = "VIEW_3D"
  bl_region_type = "UI"
  bl_category = "BUMLi"
  bl_label = "Mesh Linter"

  def draw(self, context):
    layout = self.layout
    scene = context.scene
    
    layout.label(text="Rules", icon='GREASEPENCIL')
    row = layout.row()
    
    # Left Checkboxes
    col1 = row.column(align=True)
    col1.prop(scene, "should_apply_scale")
    col1.prop(scene, "should_apply_rotation")
    col1.prop(scene, "should_apply_modifiers")
    col1.prop(scene, "should_clear_materials")

    # Right Checkboxes
    col2 = row.column(align=True)
    col2.prop(scene, "should_rename")
    col2.prop(scene, "should_recalculate_normals")
    col2.prop(scene, "should_reset_origin")
    col2.prop(scene, "should_place_to_world_origin")
    
    row = self.layout.row()
    row.prop(scene, "should_duplicate")

    # Buttons
    row = self.layout.row()
    row.operator("mesh.fix", text="Fix")
    
    row = self.layout.row()
    row.operator("mesh.colliders_to_wire", text="Toggle Collider")
    
    layout.separator()
    
    # Export
    layout.label(text="Export", icon='FILE_FOLDER')

    row = layout.row()
    row.prop(scene, "export_directory", text="Destination")

    row = self.layout.row()
    row.operator("mesh.export", text="Export")
