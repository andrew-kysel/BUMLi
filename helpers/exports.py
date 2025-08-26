from bpy import ops
        
def as_static_mesh(filepath: str):
  ops.export_scene.fbx(
    filepath=filepath,
    check_existing=True,
    use_selection=True,
    object_types={'MESH'},
    use_custom_props=False,
    global_scale=1.0,
    apply_scale_options='FBX_SCALE_ALL',
    axis_forward='-Z',
    axis_up='Y',
    apply_unit_scale=True,
    use_space_transform=True,
    mesh_smooth_type='FACE',
    use_subsurf=False,
    use_mesh_modifiers=False,
    use_tspace=False,
    colors_type='SRGB',
    primary_bone_axis='Y',
    secondary_bone_axis='X',
    armature_nodetype='NULL',
    add_leaf_bones=False,
    bake_anim=False
  )
