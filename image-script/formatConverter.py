import os
import sys
from PIL import Image


def convert_images(input_folder, output_folder):

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)

            base_name = os.path.splitext(filename)[0]
            new_filename = base_name + ".png"
            output_path = os.path.join(output_folder, new_filename)

            img.save(output_path, "PNG")
            print(f"Converted: {filename} -> {new_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert.py <input_folder> <output_folder>")
    else:
        input_folder = sys.argv[1]
        output_folder = sys.argv[2]
        convert_images(input_folder, output_folder)
