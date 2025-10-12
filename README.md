Blender to Unreal Mesh Linter
==========
Current supported version `4.3.0^`

## Installation
Download .zip file from [latest releases](https://github.com/andrew-kysel/BUMLi/releases/latest).

Go to `Edit` -> `Preferences` -> `Addons` -> `Install` and select downloaded archive.

Or drag-and-drop it straight into Blender window.

## Location
`3D Viewport` -> `N Panel` -> `BUMLi`

# Addon Overview
Addon allows you to prepare your _static mesh_ for export to Unreal Engine and fix some common errors beforehand.
Each mesh can be updated using list of customizable rules. It is possible to apply changes non-destructively without changing original mesh.

Addon provides a simplified way to export FBX files using slightly changed default Blender presets with focus on Unreal Engine.

## Available Rules

### Clear Materials
Removes all materials from Mesh. Allows to avoid default Unreal Engine behaviour with creation of unnecessary Material Slots.

### Update Name
Updates Mesh name according to default [Unreal Engine Naming Convention](https://dev.epicgames.com/documentation/en-us/unreal-engine/recommended-asset-naming-conventions-in-unreal-engine-projects). 

Adds `SM_` prefix to Mesh name. E.g. `Chair` -> `SM_Chair`.

Renaming also changes Collider names. But to make it work you need to setup Collider as a child of your main Mesh (`ctrl+P` -> `Object (Keep Transform)`). 
In this case Collider will have `UBX_` (in case Collider is rectangular) prefix or `UCX_` (if it's convex). 

E.g. Collider for `SM_Chair` will be automatically renamed to `UBX_SM_Chair`. Using this prefix Unreal Engine automatically will treat such Mesh as Collider.  

### Recalculate Normals
Recalculates all inverted normals (the red ones) if any. 

**Disclaimer**: does not work in 100% of cases, so it's always a good idea to double check it manually. 

### Reset Origin
Puts Mesh origin to the lowest middle point of the Mesh.

### Place to World Origin
Places Mesh to the `0,0,0` coordinates. Unreal Engine treats Blender's World Origin as Mesh origin for imported models.

Works very well with **Reset Origin** rule for Models which should be located on the ground.

**Disclaimer**: in some cases it can dislocate Collider a bit. I'm trying to fix it, but without success so far. 

### Apply Modifiers
Applies modifiers in case one forgot.  

### Apply Scale and Rotation
Basically it...

### Non-Destructive
Creates duplicate of the Mesh and applies selected rule on that duplicate.

## Export
Allows to select Export folder and export selected Mesh with its Colliders in one-click as FBX.

No need to setup any presets. Addon preset uses typical setup for Unreal Engine FBX format file.

## Additional functionality
I've added `Toggle Collider` button to help myself review Meshes faster. It changes `Viewport Display` -> `Display As` Collider property from `Solid` to `Wire` and vice versa.

It works only if your Colliders are children of original Mesh and have proper Naming Convention (`UBX_`/`UCX_`).






