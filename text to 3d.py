import shap_e
import torch
import os
import trimesh
from pathlib import Path

def generate_3d_from_text(text_prompt):
    # Load the pre-trained model
    model = shap_e.ShapE()

    # Generate the 3D model from text
    generated_3d = model.generate(text_prompt)
    
    # Save the 3D model as .obj
    output_dir = Path("models")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "generated_3d.obj"
    trimesh.exchange.obj.export_mesh(generated_3d, str(output_file))

    print(f"3D model generated and saved to {output_file}")
