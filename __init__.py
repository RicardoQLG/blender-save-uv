import bpy
from bpy.app.handlers import persistent

bl_info = {
    "name": "Save UV with project",
    "author": "Ricardo Godoy",
    "version": (1, 1),
    "blender": (2, 80, 0),
    "description": "Saves UV Texture with save command",
    "Category": "Save"
}

@persistent
def save_uv_on_save(bl_scene):
    bpy.ops.image.save_all_modified()

def register():
    bpy.app.handlers.save_post.append(save_uv_on_save)

def unregister():
    bpy.app.handlers.save_post.remove(save_uv_on_save)

def init ():
    bpy.app.handlers.save_post.append(save_uv_on_save)

if __name__ == "__main__":
    register()