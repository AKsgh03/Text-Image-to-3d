import trimesh
import pyrender

def visualize_3d_model(file_path):
    # Load the 3D model
    mesh = trimesh.load_mesh(file_path)

    # Visualize the mesh using pyrender
    scene = pyrender.Scene()
    mesh_node = pyrender.Node(mesh=mesh)
    scene.add_node(mesh_node)
    
    # Create a viewer to show the model
    viewer = pyrender.Viewer(scene, use_raymond_lighting=True)
