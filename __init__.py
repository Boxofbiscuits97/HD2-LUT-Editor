# Original shader created by @thejudsub on The Helldivers Archive Discord Server
# Shader post can be found here: https://discord.com/channels/1210541115829260328/1222290154409033889

# Modified slightly for use with filediver
# Modified quite a bit to add cape support

# Shader bundled with filediver with permission from @thejudsub

# Continued Integrations with Blender workflow by Boxofbiscuits97

bl_info = {
    "name": "Helldivers 2 LUT Editor",
    "version": (0, 0, 1),
    "blender": (4, 0, 0),
    "category": "Import-Export",
}

import bpy
from . import ui

classes = (
    ui.NODE_PT_MAINPANEL,
    ui.CreateShader,
    ui.UpdateShader,
    ui.OpenEXRFile,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()