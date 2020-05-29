import bpy
from bpy import context

context.scene.cursor.location = [0.0, 0.0, 0.0]
bpy.ops.object.rotation_clear(clear_delta=False)
bpy.ops.object.location_clear(clear_delta=False)
bpy.ops.object.scale_clear(clear_delta=False)

obj = context.active_object
v = obj.data.vertices

highest = [v[0].co[0], v[0].co[1], v[0].co[2]]
lowest = [v[0].co[0], v[0].co[1], v[0].co[2]]

for v in obj.data.vertices:
    c = v.co
    
    if c[0] > highest[0]:
        highest[0] = c[0]
    
    if c[0] < lowest[0]:
        lowest[0] = c[0]
    
    if c[1] > highest[1]:
        highest[1] = c[1]
    
    if c[1] < lowest[1]:
        lowest[1] = c[1]
    
    if c[2] > highest[2]:
        highest[2] = c[2]
    
    if c[2] < lowest[2]:
        lowest[2] = c[2]


bpy.ops.transform.translate(
    value=(-0.5*(highest[0]+lowest[0]), -0.5*(highest[1]+lowest[1]), -0.5*(highest[2]+lowest[2])),
    orient_type='GLOBAL',
    orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
    orient_matrix_type='GLOBAL',
    mirror=True,
    use_proportional_edit=False,
    proportional_edit_falloff='SMOOTH',
    proportional_size=1,
    use_proportional_connected=False,
    use_proportional_projected=False
)

bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')

size = [highest[0]-lowest[0], highest[1]-lowest[1],highest[2]-lowest[2]]

s = 2/sorted(size)[2]

bpy.ops.transform.resize(
    value=(s, s, s),
    orient_type='GLOBAL',
    orient_matrix=((1, 0, 0),(0, 1, 0), (0, 0, 1)),
    orient_matrix_type='GLOBAL',
    mirror=True,
    use_proportional_edit=False,
    proportional_edit_falloff='SMOOTH',
    proportional_size=1,
    use_proportional_connected=False,
    use_proportional_projected=False
)
