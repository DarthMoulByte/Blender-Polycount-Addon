import bpy
from . main import \
    VIEW3D_OT_polycount_display, \
    VIEW3D_PT_polycount_main

from . settings import VIEW3D_PT_polycount_settings, \
                       VIEW3D_OT_polycount_save_prefs, \
                       VIEW3D_OT_polycount_reset_prefs

from . misc import VIEW3D_PT_polycount_misc

from . list_Objs import \
    DATA_OT_polycount_obj_list_add, \
    DATA_OT_polycount_obj_list_remove, \
    DATA_UL_polycount_obj_list, \
    DATA_OT_polycount_obj_list_select, \
    DATA_OT_polycount_obj_list_hide, \
    DATA_OT_polycount_obj_list_clear

from . list_Lists import \
    DATA_OT_polycount_lists_list_add, \
    DATA_OT_polycount_lists_list_remove, \
    DATA_UL_polycount_lists_list

from bpy.utils import register_class, unregister_class


def register():
    """
    All interface-related classes are explicitly registered.
    """
    register_class(VIEW3D_OT_polycount_display)

    register_class(DATA_OT_polycount_obj_list_add)
    register_class(DATA_OT_polycount_obj_list_remove)
    register_class(DATA_OT_polycount_obj_list_select)
    register_class(DATA_OT_polycount_obj_list_hide)
    register_class(DATA_OT_polycount_obj_list_clear)
    register_class(DATA_UL_polycount_obj_list)

    register_class(DATA_OT_polycount_lists_list_add)
    register_class(DATA_OT_polycount_lists_list_remove)
    register_class(DATA_UL_polycount_lists_list)

    register_class(VIEW3D_PT_polycount_main)
    register_class(VIEW3D_OT_polycount_save_prefs)
    register_class(VIEW3D_OT_polycount_reset_prefs)
    register_class(VIEW3D_PT_polycount_settings)
    register_class(VIEW3D_PT_polycount_misc)


def unregister():
    unregister_class(VIEW3D_OT_polycount_display)

    unregister_class(VIEW3D_PT_polycount_main)
    unregister_class(VIEW3D_PT_polycount_settings)
    unregister_class(VIEW3D_OT_polycount_save_prefs)
    unregister_class(VIEW3D_OT_polycount_reset_prefs)
    unregister_class(VIEW3D_PT_polycount_misc)

    unregister_class(DATA_OT_polycount_obj_list_add)
    unregister_class(DATA_OT_polycount_obj_list_remove)
    unregister_class(DATA_OT_polycount_obj_list_select)
    unregister_class(DATA_OT_polycount_obj_list_hide)
    unregister_class(DATA_OT_polycount_obj_list_clear)
    unregister_class(DATA_UL_polycount_obj_list)

    unregister_class(DATA_OT_polycount_lists_list_add)
    unregister_class(DATA_OT_polycount_lists_list_remove)
    unregister_class(DATA_UL_polycount_lists_list)
