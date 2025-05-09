import argparse
from text_to_3d import generate_3d_from_text
from image_to_3d import generate_3d_from_image

def main():
    parser = argparse.ArgumentParser(description="Generate 3D models from text or image")
    parser.add_argument('--text', type=str, help='Text input to generate 3D model')
    parser.add_argument('--image', type=str, help='Image input to generate 3D model')
    args = parser.parse_args()

    if args.text:
        print(f"Generating 3D model from text: {args.text}")
        generate_3d_from_text(args.text)
    elif args.image:
        print(f"Generating 3D model from image: {args.image}")
        generate_3d_from_image(args.image)
    else:
        print("Please provide either --text or --image argument")

if __name__ == "__main__":
    main()
