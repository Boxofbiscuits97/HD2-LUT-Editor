import bpy
from bpy_extras.io_utils import ImportHelper, ExportHelper
from . import bl_info
from . import shader
from . import exr

class NODE_PT_MAINPANEL(bpy.types.Panel):
    bl_label = f"Helldivers 2 LUT Editor v{bl_info['version'][0]}.{bl_info['version'][1]}.{bl_info['version'][2]}"
    bl_idname = "NODE_PT_capecontrols"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = 'HD2 LUT Editor'

    def draw(self, context):
        layout = self.layout

        col = layout.column()
        col.operator('node.create_operator')
        col.operator('node.update_operator')
        col.operator('exr.open_file')

class CreateShader(bpy.types.Operator):
    bl_label = ("(Re)Build Shader")
    bl_idname = "node.create_operator"

    def execute(self, context):
        if shader.check_valid_material(self): return {'CANCELLED'}
        custom_node_name = ("HD2 Shader Template File Do Not Name Anything Else This Name")
        GroupNode = shader.create_HD2_Shader(self, context, custom_node_name)

        return {'FINISHED'}

class UpdateShader(bpy.types.Operator):
    bl_label = ("Update Images")
    bl_idname = "node.update_operator"

    def execute(self, context):
        if shader.check_valid_material(self): return {'CANCELLED'}
        material = bpy.context.active_object.active_material
        shader_template = material.node_tree.nodes["HD2 Shader Template"]
        node_tree = shader_template.node_tree
        #GroupNode = bpy.data.node_groups[custom_node_name]
        shader.update_images(node_tree, bpy.context.active_object.active_material)
        shader.add_bake_uvs(bpy.context.active_object)
        shader.update_slot_defaults(node_tree, bpy.context.active_object.active_material)
        return {'FINISHED'}

class OpenEXRFile(bpy.types.Operator, ImportHelper):
    bl_label = ("Open EXR File")
    bl_idname = "exr.open_file"

    def execute(self, context):
        print(self.raw_filepath)
        exr.OpenEXR(self.raw_filepath)
        return {'FINISHED'}