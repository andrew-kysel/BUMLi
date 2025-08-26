bl_info = {
  "name": "BUMLi",
  "author": "Knight of Gamedevalry",
  "version": (1, 0, 0),
  "blender": (4, 3, 0),
  "location": "3D Viewport > Sidebar > BUMLi",
  "description": "Blender-Unreal Mesh Linter. Allows to properly prepare mesh before export it to Unreal",
  "category": "Development",
}

import bpy
from .panels import classes as panel_classes
from .operators import classes as operator_classes
from .properties import register_properties, unregister_properties

classes = operator_classes + panel_classes

def register():
  register_properties()
  for cls in classes:
    bpy.utils.register_class(cls)

def unregister():
  unregister_properties()
  for cls in classes:
    bpy.utils.unregister_class(cls)
