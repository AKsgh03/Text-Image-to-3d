import cv2
import rembg
import open3d as o3d
import numpy as np
import os
from pathlib import Path

def generate_3d_from_image(image_path):
    # Read the input image
    img = cv2.imread(image_path)

    # Remove background using rembg
    img_no_bg = rembg.remove(img)

    # Convert image to depth map (dummy for this prototype, replace with proper model)
    depth_map = cv2.cvtColor(img_no_bg, cv2.COLOR_BGR2GRAY)

    # Generate a point cloud from depth map (using Open3D for simplicity)
    depth_image = o3d.geometry.Image(depth_map)
    pcd = o3d.geometry.PointCloud.create_from_depth_image(depth_image, o3d.camera.PinholeCameraIntrinsic())

    # Save the point cloud as a .ply file
    output_dir = Path("models")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "generated_3d.ply"
    o3d.io.write_point_cloud(str(output_file), pcd)

    print(f"3D model generated and saved to {output_file}")
