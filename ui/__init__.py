import bpy
from . main import VIEW3D_OT_polycount_display, VIEW3D_PT_polycount_main, VIEW3D_PT_polycount_object, VIEW3D_PT_polycount_edit_mode
from . settings import VIEW3D_PT_polycount_settings
from . list_Objs import DATA_OT_polycount_obj_list_add, DATA_OT_polycount_obj_list_remove, DATA_UL_polycount_obj_list
from . list_Lists import DATA_OT_polycount_lists_list_add, DATA_OT_polycount_lists_list_remove, DATA_UL_polycount_lists_list


def register():
    """
    All interface-related classes are explicitly registered.
    """
    bpy.utils.register_class(VIEW3D_OT_polycount_display)

    bpy.utils.register_class(DATA_OT_polycount_obj_list_add)
    bpy.utils.register_class(DATA_OT_polycount_obj_list_remove)
    bpy.utils.register_class(DATA_UL_polycount_obj_list)

    bpy.utils.register_class(DATA_OT_polycount_lists_list_add)
    bpy.utils.register_class(DATA_OT_polycount_lists_list_remove)
    bpy.utils.register_class(DATA_UL_polycount_lists_list)


    bpy.utils.register_class(VIEW3D_PT_polycount_main)
    bpy.utils.register_class(VIEW3D_PT_polycount_object)
    bpy.utils.register_class(VIEW3D_PT_polycount_edit_mode)
    bpy.utils.register_class(VIEW3D_PT_polycount_settings)


def unregister():
    bpy.utils.unregister_class(VIEW3D_OT_polycount_display)

    bpy.utils.unregister_class(VIEW3D_PT_polycount_main)
    bpy.utils.unregister_class(VIEW3D_PT_polycount_object)
    bpy.utils.unregister_class(VIEW3D_PT_polycount_edit_mode)
    bpy.utils.unregister_class(VIEW3D_PT_polycount_settings)

    bpy.utils.unregister_class(DATA_OT_polycount_obj_list_add)
    bpy.utils.unregister_class(DATA_OT_polycount_obj_list_remove)
    bpy.utils.unregister_class(DATA_UL_polycount_obj_list)

    bpy.utils.unregister_class(DATA_OT_polycount_lists_list_add)
    bpy.utils.unregister_class(DATA_OT_polycount_lists_list_remove)
    bpy.utils.unregister_class(DATA_UL_polycount_lists_list)