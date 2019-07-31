import bpy
import random

for obj in bpy.data.objects:
    if obj.type == 'MESH':
        bpy.context.scene.objects.active = obj
bpy.ops.object.mode_set(mode = 'EDIT')
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.edge_split()
bpy.ops.mesh.separate(type='LOOSE')
bpy.ops.object.mode_set(mode = 'OBJECT')
bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

for obj in bpy.data.objects:
    if obj.type == 'MESH':
        obj.location = (random.uniform(0,50),obj.location.y,obj.location.z)
        obj.select = True
        bpy.context.scene.objects.active = obj
    else:
        obj.select = False
bpy.ops.object.join()
bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
