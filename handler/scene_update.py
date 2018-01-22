import bpy, bmesh
from bpy.app.handlers import persistent


# scene_update_post
def edit_mode_count(act_obj):
    """
    In Edit Mode, the polycount for the active object will be updated
    when the number of selected vertices changes
    :param obj: The active object
    """
    # If it is not in Edit Mode goes out
    if bpy.context.mode != 'EDIT_MESH' or act_obj.mode != 'EDIT': return
    bm = bmesh.from_edit_mesh(act_obj.data)
    if bm is not None:
        if hasattr(bm.verts, "ensure_lookup_table"): bm.verts.ensure_lookup_table()
        verts_sel = [v for v in bm.verts if v.select]
        if bpy.context.scene.Polycount.temp.selected_verts != len(verts_sel):
            # If the number of selected vertices of the active object has changed,
            # the polycount will be updated in this object
            bpy.context.scene.Polycount.temp.selected_verts = len(verts_sel)
            act_obj.Polycount.Updated = False


@persistent
def polycount_scene_update_post(scene):
    """
    Called on after updating scene data
    :param scene: At appending this function to the scene_update_post, it receives the scene as a parameter.
    """
    obj = scene.objects.active
    if obj is None or not hasattr(obj, 'Polycount') or not hasattr(obj.Polycount, 'Updated'): return

    # "is_updated_data" is True when an object changes.
    if obj.is_updated_data:
        obj.Polycount.Updated = False
        if obj.mode != 'EDIT' and scene.Polycount.temp.selected_verts != 0:
            # When the active object is not in Edit mode selected_verts should be 0
            scene.Polycount.temp.selected_verts = 0

    # In Edit Mode
    if scene.Polycount.Draw.EditModePolycount: edit_mode_count(obj)



