import bpy
from bpy.types import Scene

def register_properties():
  Scene.should_duplicate = bpy.props.BoolProperty(
    name="Non-Destructive",
    description="Duplicates mesh with collider to allow non-destructive approach",
    default=True
  )
  Scene.should_rename = bpy.props.BoolProperty(
    name="Update Name",
    description="Adds SM_ prefix to mesh name and renames collider to UBX_/UCX_SM_[MeshName]",
    default=True
  )
  Scene.should_clear_materials = bpy.props.BoolProperty(
    name="Clear Materials",
    description="Removes all materials from selected mesh. Helps to avoid creating Material Slot in Unreal with improper naming",
    default=True
  )
  Scene.should_apply_modifiers = bpy.props.BoolProperty(
    name="Apply Modifiers",
    description="Applies all modifiers used within a mesh",
    default=True
  )
  Scene.should_recalculate_normals = bpy.props.BoolProperty(
    name="Recalculate Normals",
    description="Recalculates Normals with inside flag as false",
    default=True
  )
  Scene.should_apply_scale = bpy.props.BoolProperty(
    name="Apply Scale",
    description="I have nothing to add here...",
    default=True
  )
  Scene.should_reset_origin = bpy.props.BoolProperty(
    name="Reset Origin",
    description="Sets origin of mesh and colliders to the lowest center point",
    default=True
  )
  Scene.should_place_to_world_origin = bpy.props.BoolProperty(
    name="Place to World Origin",
    description="Places mesh at the center of the world (0, 0, 0)",
    default=True
  )

def unregister_properties():
  del Scene.should_duplicate
  del Scene.should_rename
  del Scene.should_apply_modifiers
  del Scene.should_recalculate_normals
  del Scene.should_apply_scale
  del Scene.should_reset_origin
  del Scene.should_place_to_world_origin
