import bpy
import sys

# Lê argumentos da linha de comando
args = sys.argv[sys.argv.index("--") + 1:]

# Função para criar modelo 3D
def create_model(width, length, height):
    # Limpa a cena
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

    # Cria as paredes (cubos básicos)
    bpy.ops.mesh.primitive_cube_add(location=(0, 0, height / 2))
    wall = bpy.context.object
    wall.scale = (width / 2, length / 2, height / 2)

    # Exporta o modelo 3D
    bpy.ops.export_scene.gltf(filepath="model_output.glb")

# Converte os argumentos
params = {arg.split('=')[0]: float(arg.split('=')[1]) for arg in args}
create_model(params.get('width', 10), params.get('length', 10), params.get('height', 3))
def add_door(x, y, width, height):
    bpy.ops.mesh.primitive_cube_add(location=(x, y, height / 2))
    door = bpy.context.object
    door.scale = (width / 2, 0.1, height / 2)

def add_window(x, y, width, height):
    bpy.ops.mesh.primitive_cube_add(location=(x, y, height / 2))
    window = bpy.context.object
    window.scale = (width / 2, 0.1, height / 2)

# Adiciona uma porta e uma janela
add_door(0, -4, 1, 2)
add_window(3, 5, 1.5, 1.5)
