import os
from PIL import Image

input_folder = 'images'
output_folder = 'resized_images'
resize_size = (800, 800)

os.makedirs(input_folder, exist_ok=True)
os.makedirs(output_folder, exist_ok=True)

found = False
for filename in os.listdir(input_folder):
    ext = os.path.splitext(filename)[1].lower().strip()
    if ext in ('.png', '.jpg', '.jpeg'):
        found = True
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        img_resized = img.resize(resize_size)
        output_path = os.path.join(output_folder, filename)
        img_resized.save(output_path)
        print(f"Resized and saved: {output_path}")

if not found:
    print("No image files found in the 'images' folder.")
