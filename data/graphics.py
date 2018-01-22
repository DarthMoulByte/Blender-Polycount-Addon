import bpy

class DrawPropertyGroup(bpy.types.PropertyGroup):
    """
    Customizes how the data is displayed
    """
    # Scene data
    ObjPolycount = bpy.props.BoolProperty(default = True, description = 'Object Polycount')
    triangles = bpy.props.BoolProperty(default = True, description = 'Triangles*1 + Quads*2 + Ngons*(vertices - 2)')
    quads     = bpy.props.BoolProperty(default = True, description = '4-sided polygons')
    ngons     = bpy.props.BoolProperty(default = True, description = 'N-sided polygons')
    faces     = bpy.props.BoolProperty(default = True, description = 'Triangles + Quads + Ngons')

    # Edit Mode data
    EditModePolycount = bpy.props.BoolProperty(default = True, description = 'Edit Mode Polycount')
    selected_tris = bpy.props.BoolProperty(default = True, description="Triangles*1 + Quads*2 + Ngons*(vertices - 2)")
    selected_verts = bpy.props.BoolProperty(default = True, description="Selected Vertices Polycount")
    selected_edges = bpy.props.BoolProperty(default = True, description="Selected Edges Polycount")
    selected_faces = bpy.props.BoolProperty(default = True, description="Selected Faces Polycount")

    # Drawing settings
    hor_Offset = bpy.props.IntProperty(name = "HorOffset", default = 0)
    vert_Offset = bpy.props.IntProperty(name = "VertOffset", default = 0)
    font_size = bpy.props.IntProperty(name = "FontSize", default = 14, max= 20, min=12)
    title_color = bpy.props.FloatVectorProperty(name="title_color", subtype='COLOR', default=(1.0, 0.8, 0.1), min=0.0, max=1.0, description="color picker")
    data_color = bpy.props.FloatVectorProperty(name="data_color", subtype='COLOR', default=(1.0, 1.0, 1.0), min=0.0, max=1.0, description="color picker")
    sep_color = bpy.props.FloatVectorProperty(name="sep_color", subtype='COLOR', default=(0.5, 1.0, 0.5), min=0.0, max=1.0, description="color picker")